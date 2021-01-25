"""args.py  -- execution configuration & execution argument parsing

devconf()  -- configure for mid-development execution
readargs()  -- read arguments from sys.argv
"""

import argparse


#region Globals

TREELINEPATH = "TREELINEPATH"
INJECTIONSPECPATH = "INJECTIONSPECPATH"
PRINTOUTPUT = "PRINTOUTPUT"

g = {TREELINEPATH: None,
     INJECTIONSPECPATH: None,
     PRINTOUTPUT: False}


#endregion
#region Mid-Development Configuration (NOT Argument Parsing)

def mid_development():
    g[INJECTIONSPECPATH] = (r"D:\repo\treelinefmt\devref"
                            r"\example_input.txt")
    g[TREELINEPATH] = (r"D:\repo\treelinefmt\devref"
                       r"\source_treeline_file.trln")
    g[PRINTOUTPUT] = True


#endregion
#region Argments Parsing


desc = "Inject formats into a Treeline .trln document."

def readargs():
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("injection",
                        help="Injection Specification file (.txt)")
    parser.add_argument("treeline",
                        help="Treeline file (.trln) to inject formats into")
    parser.add_argument("-p", "--print-only",
                        help="Don't modify treeline; Instead, print output",
                        action='store_true')
    result = parser.parse_args()
    g[INJECTIONSPECPATH] = result.injection
    g[TREELINEPATH] = result.treeline
    g[PRINTOUTPUT] = result.print_only


#endregion