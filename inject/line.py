"""line.py  -- read and interpret a line in the injection spec

read(ln)  -- read in a line

g[LINE]  -- the line that was read in
g[WORD0]  -- the first "word" that was read
g[WORD1]  -- the second "word" that was read
g[BRACKETED]  -- the text that is bracketed
g[PARENTHESIS]  -- the text within parenthesis (de-csv'ed)
g[INDENT]  -- how far the text was indented

decsv(s)  -- return a list from comma separated values
"""


LINE="LINE"
WORD0="WORD0"
WORD1="WORD1"
REST="REST"
BRACKETED="BRACKETED"
PARENTHESIS="PARENTHESIS"
INDENT="INDENT"

g = {LINE: "",
     WORD0: "",
     WORD1: "",
     REST: "",
     BRACKETED: "",
     PARENTHESIS: "",
     INDENT: None}


def reset():
    g[LINE] = ""
    g[WORD0] = ""
    g[WORD1] = ""
    g[REST] = ""
    g[BRACKETED] = ""
    g[PARENTHESIS] = ""
    g[INDENT] = None


def read(ln):
    reset()
    g[LINE] = ln
    g[INDENT] = len(ln) - len(ln.lstrip())
    words = g[LINE].split()
    if len(words) > 0:
        g[WORD0] = words[0]
        if len(words) > 1:
            g[WORD1] = words[1]
            word0, g[REST] = ln.split(None, 1)
    try:
        b0 = ln.index("[")
        b1 = ln.index("]")
        g[BRACKETED] = ln[b0+1:b1]
    except ValueError:
        pass
    try:
        p0 = ln.index("(")
        p1 = ln.index(")")
        g[PARENTHESIS] = decsv(ln[p0+1:p1])
    except ValueError:
        pass


def decsv(s):
    return [x.strip() for x in s.split(",")]
