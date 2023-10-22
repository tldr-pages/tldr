#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import argparse
import os
import re
import subprocess
import sys

labels = {
    "en": "More information:",
    "ar": "لمزيد من التفاصيل:",
    "bn": "আরও তথ্য পাবেন:",
    "bs": "Više informacija:",
    "cs": "Více informací:",
    "ca": "Més informació:",
    "da": "Mere information:",
    "de": "Weitere Informationen:",
    "es": "Más información:",
    "fa": "اطلاعات بیشتر:",
    "fr": "Plus d'informations :",
    "sh": "Više informacija:",
    "hi": "अधिक जानकारी:",
    "id": "Informasi lebih lanjut:",
    "it": "Maggiori informazioni:",
    "ja": "詳しくはこちら:",
    "ko": "더 많은 정보:",
    "lo": "ຂໍ້ມູນເພີ່ມເຕີມ:",
    "ml": "കൂടുതൽ വിവരങ്ങൾ:",
    "ne": "थप जानकारी:",
    "nl": "Meer informatie:",
    "no": "Mer informasjon:",
    "pl": "Więcej informacji:",
    "pt_BR": "Mais informações:",
    "pt_PT": "Mais informações:",
    "ro": "Mai multe informații:",
    "ru": "Больше информации:",
    "sr": "Više informacija na:",
    "sv": "Mer information:",
    "ta": "மேலும் விவரத்திற்கு:",
    "th": "ข้อมูลเพิ่มเติม:",
    "tr": "Daha fazla bilgi için:",
    "uk": "Більше інформації:",
    "uz": "Ko'proq malumot:",
    "zh_TW": "更多資訊：",
    "zh": "更多信息：",
}

IGNORE_FILES = (".DS_Store",)


def get_tldr_root():
    # if this script is running from tldr/scripts, the parent's parent is the root
    f = os.path.normpath(__file__)
    if f.endswith("tldr/scripts/set-more-info-link.py"):
        return os.path.dirname(os.path.dirname(f))

    if "TLDR_ROOT" in os.environ:
        return os.environ["TLDR_ROOT"]
    print(
        "\x1b[31mPlease set TLDR_ROOT to the location of a clone of https://github.com/tldr-pages/tldr."
    )
    sys.exit(1)


def set_link(file, link):
    with open(file) as f:
        lines = f.readlines()

    desc_start = 0
    desc_end = 0

    # find start and end of description
    for i, line in enumerate(lines):
        if line.startswith(">") and desc_start == 0:
            desc_start = i
        if not lines[i + 1].startswith(">") and desc_start != 0:
            desc_end = i
            break

    # compute locale
    pages_dir = os.path.basename(os.path.dirname(os.path.dirname(file)))
    if "." in pages_dir:
        _, locale = pages_dir.split(".")
    else:
        locale = "en"

    # build new line
    if locale == "hi":
        new_line = f"> {labels[locale]} <{link}>।\n"
    elif locale in ["ja", "th"]:
        new_line = f"> {labels[locale]} <{link}>\n"
    elif locale in ["zh", "zh_TW"]:
        new_line = f"> {labels[locale]}<{link}>.\n"
    else:
        new_line = f"> {labels[locale]} <{link}>.\n"

    if lines[desc_end] == new_line:
        # return empty status to indicate that no changes were made
        return ""

    if re.search(r"^>.*<.+>", lines[desc_end]):
        # overwrite last line
        lines[desc_end] = new_line
        status = "\x1b[34mlink updated"
    else:
        # add new line
        lines.insert(desc_end + 1, new_line)
        status = "\x1b[36mlink added"

    with open(file, "w") as f:
        f.writelines(lines)

    return status


def get_link(file):
    with open(file) as f:
        lines = f.readlines()

    desc_start = 0
    desc_end = 0

    # find start and end of description
    for i, line in enumerate(lines):
        if line.startswith(">") and desc_start == 0:
            desc_start = i
        if not lines[i + 1].startswith(">") and desc_start != 0:
            desc_end = i
            break

    # match link
    if re.search(r"^>.*<.+>", lines[desc_end]):
        return re.search("<(.+)>", lines[desc_end]).group(1)
    else:
        return ""


def sync(root, pages_dirs, command, link):
    rel_paths = []
    for page_dir in pages_dirs:
        path = os.path.join(root, page_dir, command)
        if os.path.exists(path):
            rel_path = path.replace(f"{root}/", "")
            rel_paths.append(rel_path)
            status = set_link(path, link)
            if status != "":
                print(f"\x1b[32m{rel_path} {status}\x1b[0m")
    return rel_paths


def main():
    parser = argparse.ArgumentParser(
        description='Sets the "More information" link for all translations of a page'
    )
    parser.add_argument(
        "-p",
        "--page",
        type=str,
        required=False,
        default="",
        help='page name in the format "platform/command.md"',
    )
    parser.add_argument(
        "-s",
        "--stage",
        action="store_true",
        default=False,
        help="stage modified pages (requires `git` to be on $PATH and TLDR_ROOT to be a Git repository)",
    )
    parser.add_argument(
        "-S",
        "--sync",
        action="store_true",
        default=False,
        help="synchronize each translation's more information link (if exists) with that of English page",
    )
    parser.add_argument("link", type=str, nargs="?", default="")
    args = parser.parse_args()

    root = get_tldr_root()
    pages_dirs = [d for d in os.listdir(root) if d.startswith("pages")]

    rel_paths = []

    # Use '--page' option
    if args.page != "":
        target_paths = []

        if not args.page.lower().endswith(".md"):
            args.page = f"{args.page}.md"

        for pages_dir in pages_dirs:
            pages_dir_path = os.path.join(root, pages_dir)
            platforms = [i for i in os.listdir(pages_dir_path) if i not in IGNORE_FILES]
            for platform in platforms:
                platform_path = os.path.join(pages_dir_path, platform)
                commands = [
                    f"{platform}/{p}"
                    for p in os.listdir(platform_path)
                    if p not in IGNORE_FILES
                ]
                if args.page in commands:
                    path = os.path.join(pages_dir_path, args.page)
                    target_paths.append(path)

        target_paths.sort()

        for path in target_paths:
            rel_path = path.replace(f"{root}/", "")
            rel_paths.append(rel_path)
            status = set_link(path, args.link)
            if status != "":
                print(f"\x1b[32m{rel_path} {status}\x1b[0m")

    # Use '--sync' option
    elif args.sync:
        pages_dirs.remove("pages")
        en_page = os.path.join(root, "pages")
        platforms = [i for i in os.listdir(en_page) if i not in IGNORE_FILES]
        for platform in platforms:
            platform_path = os.path.join(en_page, platform)
            commands = [
                f"{platform}/{p}"
                for p in os.listdir(platform_path)
                if p not in IGNORE_FILES
            ]
            for command in commands:
                link = get_link(os.path.join(root, "pages", command))
                if link != "":
                    rel_paths += sync(root, pages_dirs, command, link)

    if args.stage:
        subprocess.call(["git", "add", *rel_paths], cwd=root)


if __name__ == "__main__":
    main()
