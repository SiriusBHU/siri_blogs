import sys
import re
import os.path as osp

interline_tag = '<img src="https://www.zhihu.com/equation?tex={}" alt="{}\\\\" class="ee_img tr_noresize" eeimg="1">'
interline_pattern = "\$\$\n*((.|\n)*?)\n*\$\$"
inline_tag = '<img src="https://www.zhihu.com/equation?tex={}" alt="{}" class="ee_img tr_noresize" eeimg="1">'
inline_pattern = "\$\n*(.*?)\n*\$"


def replace_tex(content):
    def dashrepl(matchobj, tag):
        formular = matchobj.group(1)
        return tag.format(formular, formular)

    content = re.sub(interline_pattern, lambda mo: dashrepl(mo, interline_tag), content)
    # content = re.sub(inline_pattern, lambda mo: dashrepl(mo, inline_tag), content)

    return content


# import codecs
# import os
# import chardet
#
#
# def detectCode(path):
#     with open(path, 'rb') as file:
#         data = file.read()
#         dicts = chardet.detect(data)
#     return dicts["encoding"]
#
#
#
# print(detectCode("/Users/wangshimeng/sirius/projects/siri_blogs/docs/b01_from_hilbert_space2fourier_base/b01_from_hilbert_space2fourier_base.md"))


if __name__ == '__main__':
    dir_origin = "/Users/wangshimeng/sirius/projects/siri_blogs/docs/b01_from_hilbert_space2fourier_base"
    name_context = "b01_from_hilbert_space2fourier_base.md"

    dir_proc = "/Users/wangshimeng/sirius/projects/siri_blogs/zhihu"
    with open(osp.join(dir_origin, name_context), 'r', encoding="utf-8") as f:
        content = f.read()


        # print(content)
    with open(osp.join(dir_proc, name_context), 'w', encoding="utf-8") as f:
        f.write(replace_tex(content))
