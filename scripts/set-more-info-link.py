import argparse
import os
import re
import subprocess
import sys

labels = {
    'en': 'More information:',
    'bs': 'Više informacija:',
    'da': 'Mere information:',
    'de': 'Weitere Informationen:',
    'es': 'Más información:',
    'fa': 'اطلاعات بیشتر:',
    'fr': 'Plus d\'informations\xa0:',
    'sh': 'Više informacija:',
    'hi': 'अधिक जानकारी:',
    'id': 'Informasi lebih lanjut:',
    'it': 'Maggiori informazioni:',
    'ja': '詳しくはこちら:',
    'ko': '더 많은 정보:',
    'ml': 'കൂടുതൽ വിവരങ്ങൾ:',
    'nl': 'Meer informatie:',
    'no': 'Mer informasjon:',
    'pl': 'Więcej informacji:',
    'pt_BR': 'Mais informações:',
    'pt_PT': 'Mais informações:',
    'ru': 'Больше информации:',
    'sv': 'Mer information:',
    'ta': 'மேலும் தகவல்:',
    'th': 'ดูเพิ่มเติม:',
    'tr': 'Daha fazla bilgi için:',
    'zh_TW': '更多資訊：',
    'zh': '更多信息：',
}

IGNORE_FILES = (
    '.DS_Store',
)


def get_tldr_root():
    # if this script is running from tldr/scripts, the parent's parent is the root
    f = os.path.normpath(__file__)
    if f.endswith('tldr/scripts/set-more-info-link.py'):
        return os.path.dirname(os.path.dirname(f))

    if 'TLDR_ROOT' in os.environ:
        return os.environ['TLDR_ROOT']
    else:
        print(
            '\x1b[31mPlease set TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr.')
        sys.exit(1)


def set_link(file, link):
    with open(file) as f:
        lines = f.readlines()

    desc_start = 0
    desc_end = 0

    # find start and end of description
    for i, line in enumerate(lines):
        if line.startswith('>') and desc_start == 0:
            desc_start = i
        if not lines[i + 1].startswith('>') and desc_start != 0:
            desc_end = i
            break

    # compute locale
    pages_dir = os.path.basename(os.path.dirname(os.path.dirname(file)))
    if '.' in pages_dir:
        _, locale = pages_dir.split('.')
    else:
        locale = 'en'

    # build new line
    new_line = f'> {labels[locale]} <{link}>.\n'

    if lines[desc_end] == new_line:
        # return empty status to indicate that no changes were made
        return ''

    if re.search(r'^>.*<.+>', lines[desc_end]):
        # overwrite last line
        lines[desc_end] = new_line
        status = '\x1b[34mlink updated'
    else:
        # add new line
        lines.insert(desc_end + 1, new_line)
        status = '\x1b[36mlink added'

    with open(file, 'w') as f:
        f.writelines(lines)

    return status


def main():
    parser = argparse.ArgumentParser(
        description='Sets the "More information" link for all translations of a page')
    parser.add_argument('-p', '--page', type=str, required=True,
                        help='page name in the format "platform/command.md"')
    parser.add_argument('-s', '--stage', action='store_true', default=False,
                        help='stage modified pages (requires `git` to be on $PATH and TLDR_ROOT to be a Git repository)')
    parser.add_argument('link', type=str)
    args = parser.parse_args()

    root = get_tldr_root()
    pages_dirs = [d for d in os.listdir(root) if d.startswith('pages')]

    target_paths = []
    rel_paths = []

    if not args.page.lower().endswith('.md'):
        args.page = f'{args.page}.md'

    for pages_dir in pages_dirs:
        pages_dir_path = os.path.join(root, pages_dir)
        platforms = [i for i in os.listdir(
            pages_dir_path) if i not in IGNORE_FILES]
        for platform in platforms:
            platform_path = os.path.join(pages_dir_path, platform)
            pages = os.listdir(platform_path)
            commands = [
                f'{platform}/{p}' for p in pages if p not in IGNORE_FILES]
            if args.page in commands:
                path = os.path.join(pages_dir_path, args.page)
                target_paths.append(path)

    target_paths.sort()

    for path in target_paths:
        rel_path = path.replace(f'{root}/', '')
        rel_paths.append(rel_path)
        status = set_link(path, args.link)
        if status != '':
            print(f'\x1b[32m{rel_path} {status}\x1b[0m')

    if args.stage:
        subprocess.call(['git', 'add', *rel_paths], cwd=root)


if __name__ == '__main__':
    main()
