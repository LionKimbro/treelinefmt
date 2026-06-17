"""inject.py  -- inject formats into a .trln file.

This module is essentially "main".
"""

import pprint
import inject.injectionspec as injectionspec
import inject.treeline as treeline
import inject.args as args
from inject.args import TREELINEPATH, INJECTIONSPECPATH, PRINTOUTPUT
from inject.args import SPECIFICFORMATS


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
    to_transfer = args.g[SPECIFICFORMATS]
    for fmt in injectionspec.formats:
        fmt_name = fmt[injectionspec.NAME]
        code = injectionspec.code_for_format(fmt)
        if (not to_transfer) or (fmt_name in to_transfer):
            inject_format_code(fmt_name, code)


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

