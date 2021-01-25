"""treeline.py  -- utility functions for working with .trln files

read(path)  -- read a .trln file
new(path)  -- create a blank, new .trln file
save()  -- save the .trln file

g[PATH]  -- path of file, used when writing
g[CONTENT]  -- the raw JSON content of the .trln file


Indexed fields:

.clear()  -- clear indexed fields
.scan()  -- (re-)scan .content to populate indexed fields

g[FORMATS]  -- the raw formats content of the trln file
g[NODES]  -- the raw nodes content of the trln file
g[PROPERTIES]  -- the raw properties content of the trln file

g[CHILDREN]  -- map from node UID -> children
g[DATA]  -- map from node UID -> raw data for the node
g[FORMAT]  -- map from node UID -> string name of format for the node

g[TLVERSION]  -- version string from .properties
g[TOPNODES]  -- list of node UIDs for top-level nodes
"""

import random
import json
import copy


#region Structure Constants

JSON_FORMATS = "formats"
JSON_FORMATNAME = "formatname"
JSON_ICON = "icon"
JSON_OUTPUTLINES = "outputlines"
JSON_TITLELINE = "titleline"

JSON_FIELDS = "fields"
JSON_FIELDNAME = "fieldname"
JSON_FIELDTYPE = "fieldtype"
JSON_LINES = "lines"

JSON_NODES = "nodes"
JSON_CHILDREN = "children"
JSON_DATA = "data"
JSON_FORMAT = "format"
JSON_UID = "uid"

JSON_PROPERTIES = "properties"
JSON_TLVERSION = "tlversion"
JSON_TOPNODES = "topnodes"


#endregion
#region Field Type Constants

FTYPE_TEXT = "Text"
FTYPE_HTMLTEXT = "HtmlText"
FTYPE_ONELINETEXT = "OneLineText"
FTYPE_SPACEDTEXT = "SpacedText"
FTYPE_NUMBER = "Number"
FTYPE_MATH = "Math"
FTYPE_NUMBERING = "Numbering"
FTYPE_DATE = "Date"
FTYPE_TIME = "Time"
FTYPE_DATETIME = "DateTime"
FTYPE_BOOLEAN = "Boolean"
FTYPE_CHOICE = "Choice"
FTYPE_AUTOCHOICE = "AutoChoice"
FTYPE_COMBINATION = "Combination"
FTYPE_AUTOCOMBINATION = "AutoCombination"
FTYPE_EXTERNALLINK = "ExternalLink"
FTYPE_INTERNALLINK = "InternalLink"
FTYPE_PICTURE = "Picture"
FTYPE_REGULAREXPRESSION = "RegularExpression"


#endregion
#region Other Constants

NATIVE_VERSION = "3.1.3"  # the version that this code assumes


#endregion
#region Utility Functions

def cite(s):
    return "{*"+s+"*}"

def randhex():
    """Return 32 random hex characters."""
    return random.randrange("%032x" % random.getrandbits(4*32))


#endregion
#region Global Variables

CONTENT = "CONTENT"  # the raw JSON content
PATH = "PATH"  # the path the JSON defaults to save to

FORMATS = "FORMATS"  # shortcut to formats section of CONTENT
NODES = "NODES"  # shortcut to nodes section of CONTENT
PROPERTIES = "PROPERTIES"  # shortcut to properties section of CONTENT

CHILDREN = "CHILDREN"  # children sections, indexed by node UID
DATA = "DATA"  # data sections, indexed by node UID
FORMAT = "FORMAT"  # format names, indexed by node UID

TLVERSION = "TLVERSION"  # tlversion info, as found in properties
TOPNODES = "TOPNODES"  # topnodes UID list, as found in properties

INDENT = "INDENT"  # number spaces to indent when saving JSON

g = {CONTENT: None,
     PATH: None,

     FORMATS: None,
     NODES: None,
     PROPERTIES: None,

     CHILDREN: None,
     DATA: None,
     FORMAT: None,

     TLVERSION: None,
     TOPNODES: None,

     INDENT: 2}


#endregion
#region Naked Treeline

naked = {
    JSON_FORMATS: [
        {JSON_FIELDS: [{JSON_FIELDNAME: "Name",
                        JSON_FIELDTYPE: FTYPE_TEXT}],
         JSON_FORMATNAME: "DEFAULT",
         JSON_OUTPUTLINES: ["{*Name*}"],
         JSON_TITLELINE: "{*Name*}"}
    ],
    JSON_NODES: [
        {JSON_CHILDREN: [],
         JSON_DATA: {"Name": "Main"},
         JSON_FORMAT: "DEFAULT",
         JSON_UID: "Main"}
    ],
    JSON_PROPERTIES: {
        JSON_TLVERSION: NATIVE_VERSION,
        JSON_TOPNODES: ["Main"]
    }
}


#endregion
#region Basic Manipulation

def read(path):
    """Read a .trln file into .content.

    .scan() is automatically called after reading the file.
    """
    g[PATH] = path
    g[CONTENT] = json.load(open(path))
    scan()


def new(path):
    """Start a new .trln file."""
    g[PATH] = path
    g[CONTENT] = copy.deepcopy(naked)
    scan()


def save(path=None):
    """Save a .trln file.

    When path is not supplied, uses the path that was specified when the
    file was loaded.
    """
    json.dump(g[CONTENT], open(g[PATH], "w", encoding="utf-8"),
              indent=g[INDENT])


def scan():
    """Scan .contents into indexed fields.

    Indexed fields are:
    * g[FORMATS]
    * g[NODES]
    * g[PROPERTIES]

    * g[CHILDREN]
    * g[DATA]
    * g[FORMAT]

    * g[TLVERSION]
    * g[TOPNODES]
    """
    g[FORMATS] = g[CONTENT][JSON_FORMATS]
    g[NODES] = g[CONTENT][JSON_NODES]
    g[PROPERTIES] = g[CONTENT][JSON_PROPERTIES]

    g[CHILDREN] = {}
    g[DATA] = {}
    g[FORMAT] = {}

    for node in g[NODES]:
        uid = node[JSON_UID]
        g[CHILDREN][uid] = node[JSON_CHILDREN]
        g[DATA][uid] = node[JSON_DATA]
        g[FORMAT][uid] = node[JSON_FORMAT]

    g[TLVERSION] = g[PROPERTIES][JSON_TLVERSION]
    g[TOPNODES] = g[PROPERTIES][JSON_TOPNODES]


#endregion
