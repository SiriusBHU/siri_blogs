import sys
import re
import os.path as osp
import urllib.parse


interline_pattern = "\$\$\n*((.|\n)*?)\n*\$\$"
inline_pattern = "\$\n*(.*?)\n*\$"
zhihu_equation_fmt = ('<img src="https://www.zhihu.com/equation'
                      '?tex={texurl}{align}"'
                      ' alt="{tex}{altalign}"'
                      ' class="ee_img'
                      ' tr_noresize"'
                      ' eeimg="1">')


def tex_to_zhihu_compatible(tex):
    r"""
    Convert tex to zhihu compatible format.
    - ``>`` in img alt mess up the next escaped brace: ``\{ q > 1 \} --> \{ q > 1 }``.
    """

    tex = re.sub(r'\n', '', tex)
    tex = tex.replace(r'>', r'\gt')
    texurl = urllib.parse.quote(tex)
    return tex, texurl


def tex_to_zhihu(tex, block):
    """
        Convert tex source to a img tag link to a svg on zhihu.
        www.zhihu.com/equation is a public api to render tex into svg.

        Args:
            tex(str): tex source

            block(bool): whether to render a block(center-aligned) equation or
                inline equation.

        Returns:
            string of a ``<img>`` tag.
    """

    tex, texurl = tex_to_zhihu_compatible(tex)
    if block:
        # zhihu use double back slash to center-align an equation.
        align = '%5C%5C'
        altalign = '\\\\'
    else:
        align = ''
        altalign = ''

    url = zhihu_equation_fmt.format(
        tex=tex,
        texurl=texurl,
        align=align,
        altalign=altalign,
    )
    return url


def dash_replace(match_obj, block=True):
    tex = match_obj.group(1)
    url = tex_to_zhihu(tex, block)
    return url


def replace_tex(content):
    content = re.sub(interline_pattern, lambda mo: dash_replace(mo, True), content)
    content = re.sub(interline_pattern, lambda mo: dash_replace(mo, False), content)
    return content


if __name__ == '__main__':
    dir_origin = r"D:\projects\siri_blogs\docs\b01_from_hilbert_space2fourier_base"
    name_context = "b01_from_hilbert_space2fourier_base.md"

    dir_proc = r"D:\projects\siri_blogs\zhihu"
    with open(osp.join(dir_origin, name_context), 'r', encoding="utf-8") as f:
        content = f.read()

    with open(osp.join(dir_proc, name_context), 'w', encoding="utf-8") as f:
        f.write(replace_tex(content))
