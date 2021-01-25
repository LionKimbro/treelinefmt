"""injectionspec.py  -- working with injection specifications


read(path)  -- read an injection .txt file
reset()  -- reset content & collected data

g[CONTENT]  -- list of lines from raw text of the .trln file


Collected data:

formats -- list of formats collected


Format Dictionaries:

  NAME:  name of format (str)
  TITLELINE:  title line (str: substitutions like so {*...*})
  FIELDS:  list of fields


Field Dictionaries:

  NAME:  name of field (str)
  TYPE:  type (str: valid TreeLine field type identifier)
  NLINES:  number of lines (int/None)
  CHOICES:  list of selection choices (str)


Raw-Data Insertion Dictionaries:
  NAME:  name of field (str: starts with "$", all capital)
  CODE:  raw code (mixed data: JSON-compatible)
  INSERTIONS:  list of targetted insertion dictionaries


Targeted Insertion Dictionaries:
  ** NOT USED YET; ADD IF YOU NEED IT **
  KEY:  data source, from within source format or field dictionary
  PATH:  specific path of replacement to follow

"""

import inject.line as line
import inject.treeline as treeline
import inject.icons as icons
from inject.line import WORD0, WORD1, BRACKETED, PARENTHESIS, REST, INDENT


#region Injection Spec Constants

INJSPEC_TITLEKEY = "title:"

INJSPEC_ONELINETEXT = "1"
INJSPEC_SPACEDTEXT = "spaced"
INJSPEC_EXTERNALLINK = "url"


#endregion
#region Format Dictionary Keys

NAME = "NAME"
ICON = "ICON"
TITLELINE = "TITLELINE"
FIELDS = "FIELDS"


#endregion
#region Field Dictionary Keys

NAME = "NAME"
TYPE = "TYPE"
NLINES = "NLINES"  # optional
CHOICES = "CHOICES"  # optional


#endregion
#region Built-Ins

builtin_fields = {
    "$NAME": {NAME: "Name", TYPE: treeline.FTYPE_ONELINETEXT},
    "$HOOK": {NAME: "Hook", TYPE: treeline.FTYPE_ONELINETEXT},
    "$TAGS": {NAME: "Tags", TYPE: treeline.FTYPE_ONELINETEXT},
    "$DESC": {NAME: "Desc", TYPE: treeline.FTYPE_SPACEDTEXT, NLINES: 4},
    "$URL": {NAME: "URL", TYPE: treeline.FTYPE_EXTERNALLINK}
}


#endregion
#region Global Variables

CONTENT = "CONTENT"

g = {CONTENT: None}


formats = []  # formats scanned from content


#endregion
#region Basic Manipulation

def code_for_format(D):  # D is a format dictionary
    fields = []
    R = {treeline.JSON_FORMATNAME: D[NAME],
         treeline.JSON_OUTPUTLINES: [D[TITLELINE]],
         treeline.JSON_TITLELINE: D[TITLELINE],
         treeline.JSON_FIELDS: fields,
         treeline.JSON_ICON: D[ICON]}
    for D2 in D[FIELDS]:
        fields.append({treeline.JSON_FIELDNAME: D2[NAME],
                       treeline.JSON_FIELDTYPE: D2[TYPE]})
        if D2[TYPE] in {treeline.FTYPE_SPACEDTEXT,}:
            fields[-1][treeline.JSON_LINES] = D2[NLINES]
    return R


#endregion
#region Reading Injection Specification Files

def read(path):
    """Read an injection .txt file into .content."""
    reset()
    g[CONTENT] = open(path, encoding="utf-8").read().splitlines()
    scan()


def reset():
    g[CONTENT] = None


#endregion
#region Scanning

w0 = lambda: line.g[WORD0]
w1 = lambda: line.g[WORD1]
rest = lambda: line.g[REST]
bra = lambda: line.g[BRACKETED]

def start_format():
    formats.append({NAME: w0(),
                    ICON: icons.resolve_icon(bra()),
                    TITLELINE: "",
                    FIELDS: []})

def set_format_title(s):
    formats[-1][TITLELINE] = s

def finish_format():
    pass


def try_builtin_field():
    found = builtin_fields.get(w0())
    if found is None:
        return False
    formats[-1][FIELDS].append(found)
    return True


def try_specified_field():
    field_name = w0()
    field_type = w1()
    fields = formats[-1][FIELDS]
    if field_type == INJSPEC_ONELINETEXT:  # "1"
        fields.append({NAME: field_name,
                       TYPE: treeline.FTYPE_ONELINETEXT})
    elif field_type == INJSPEC_SPACEDTEXT:  # "spaced"
        fields.append({NAME: field_name,
                       TYPE: treeline.FTYPE_SPACEDTEXT,
                       NLINES: int(bra())})  # ex: [4]
    elif field_type == INJSPEC_EXTERNALLINK:  # "url"
        fields.append({NAME: field_name,
                       TYPE: treeline.FTYPE_EXTERNALLINK})
    else:
        return False
    return True


def scan():
    """Scan .contents into global tables."""
    for i, ln in enumerate(g[CONTENT]):
        if not ln.strip():  # ignore a blank line
            continue
        if ln[0] == "#":  # ignore a comment line
            continue
        line.read(ln)
        if line.g[INDENT] == 0:
            finish_format()
            start_format()
        elif line.g[INDENT] == 2:
            if w0() == INJSPEC_TITLEKEY:
                set_format_title(rest())
            elif try_builtin_field():
                pass  # work was done in the function
            elif try_specified_field():
                pass
            else:
                raise ValueError("can't read line", i)


#endregion
