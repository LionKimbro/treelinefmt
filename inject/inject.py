"""inject.py  -- inject formats into a .trln file.

This module is essentially "main".
"""

import pprint
import inject.injectionspec as injectionspec
import inject.treeline as treeline
import inject.args as args
from inject.args import TREELINEPATH, INJECTIONSPECPATH, PRINTOUTPUT


def inject_format_code(format_name, code):
    formats = treeline.g[treeline.FORMATS]
    for D in formats:
        if D[treeline.JSON_FORMATNAME] == format_name:
            break
    else:
        formats.append({})
        D = formats[-1]
    D.clear()
    D.update(code)


def inject():
    for fmt in injectionspec.formats:
        code = injectionspec.code_for_format(fmt)
        inject_format_code(fmt[injectionspec.NAME], code)


def run():
    injectionspec.read(args.g[INJECTIONSPECPATH])
    try:
        treeline.read(args.g[TREELINEPATH])
    except FileNotFoundError:
        treeline.new(args.g[TREELINEPATH])
    inject()
    if args.g[PRINTOUTPUT]:
        pprint.pprint(treeline.g[treeline.CONTENT])
    else:
        treeline.save()


if __name__ == "__main__":
    run()

