from pygments.formatter import Formatter
from pygments.token import Token, STANDARD_TYPES

__all__ = ['SatysfiFormatter']

FULL_DOCUMENT_HEADER = """\
@require: stdjabook
@import: pygments

document (|
  title = {code};
  author = {pygments};
  show-title = false;
  show-toc = false;
|) '<
"""

FULL_DOCUMENT_FOOTER = """
>
"""


def escape_satysfi(text):
    return text.replace('\\', '\\\\')\
               .replace('|', '\|')\
               .replace('{', '\{')\
               .replace('}', '\}')\
               .replace('%', '\%')\
               .replace('*', '\*')\
               .replace('@', '\@')\
               .replace('>', '\>')\
               .replace('<', '\<')\
               .replace(';', '\;')\
               .replace('`', '\`')\
               .replace('$', '\$')\
               .replace(' ', '\py-sp;')\
               .replace("\n", '\py-lb;')

def _get_ttype_name(ttype):
    fname = STANDARD_TYPES.get(ttype)
    if fname:
        return fname
    aname = ''
    while fname is None:
        aname = ttype[-1] + aname
        ttype = ttype.parent
        fname = STANDARD_TYPES.get(ttype)
    return fname + aname

def parse_color(color):
    if color:
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        return (r/256.0, g/256.0, b/256.0)
    else:
        return None

class SatysfiFormatter(Formatter):
    name = 'SATYSFi'
    aliases = ['satysfi']
    filenames = ['*.saty']

    def __init__(self, **options):
        Formatter.__init__(self, **options)

    def get_style_defs(self, arg=''):
        out= []
        out.append("let-block ctx +py-code inner = line-break true true ctx (read-inline ctx inner)")
        out.append("let-inline ctx \py-lb = discretionary 0 (inline-skip (get-text-width ctx *' 2.)) inline-fil inline-nil")
        out.append("let-inline ctx \py-sp = read-inline ctx (embed-string (string-unexplode [32]))")
        for ttype, style in self.style:
            ctx = "ctx"
            color = parse_color(style['color'])
            if color:
                ctx = "%s |> set-text-color (RGB%s)" % (ctx, color)
            out.append("let-inline ctx \py-%(name)s inner = read-inline (%(ctx)s) inner" % dict(
                name = _get_ttype_name(ttype),
                ctx = ctx
            ))
        return "\n".join(out)

    def format_unencoded(self, tokensource, outfile):
        if self.full:
            outfile.write(FULL_DOCUMENT_HEADER)
        outfile.write("+py-code{\n")
        for ttype, value in tokensource:
            value = escape_satysfi(value)
            outfile.write("\\py-%s{%s}" % (_get_ttype_name(ttype), value))

        outfile.write("}\n")
        if self.full:
            outfile.write(FULL_DOCUMENT_FOOTER)
