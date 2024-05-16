#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to add or update the "More information" link for all translations of a page.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If the script doesn't find it in the current path, the environment variable TLDR_ROOT will be used as the tldr root. Also, ensure 'git' is available.

Usage:
    python3 scripts/set-more-info-link.py [-p PAGE] [-S] [-l LANGUAGE] [-s] [-n] [LINK]

Options:
    -p, --page PAGE
        Specify the page in the format "platform/command". This option allows setting the link for a specific page.
    -S, --sync
        Synchronize each translation's "More information" link (if exists) with that of the English page.
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
    -s, --stage
        Stage modified pages (requires 'git' on $PATH and TLDR_ROOT to be a Git repository).
    -n, --dry-run
        Show what changes would be made without actually modifying the page.

Positional Argument:
    LINK          The link to be set as the "More information" link.

Examples:
    1. Set the link for a specific page:
       python3 scripts/set-more-info-link.py -p common/tar https://example.com
       python3 scripts/set-more-info-link.py --page common/tar https://example.com

    2. Read English pages and synchronize the "More information" link across translations:
       python3 scripts/set-more-info-link.py -S
       python3 scripts/set-more-info-link.py --sync

    3. Read English pages and synchronize the "More information" link for Brazilian Portuguese pages only:
       python3 scripts/set-more-info-link.py -S -l pt_BR
       python3 scripts/set-more-info-link.py --sync --language pt_BR

    4. Read English pages, synchronize the "More information" link across translations and stage modified pages for commit:
       python3 scripts/set-more-info-link.py -Ss
       python3 scripts/set-more-info-link.py --sync --stage

    5. Show what changes would be made across translations:
       python3 scripts/set-more-info-link.py -Sn
       python3 scripts/set-more-info-link.py --sync --dry-run
"""

import re
from pathlib import Path
from _common import (
    IGNORE_FILES,
    Colors,
    get_tldr_root,
    get_pages_dir,
    get_target_paths,
    get_locale,
    get_status,
    stage,
    create_colored_line,
    create_argument_parser,
)

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
    "fi": "Lisätietoja:",
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


def set_link(
    path: Path, link: str, dry_run: bool = False, language_to_update: str = ""
) -> str:
    """
    Write a "More information" link in a page to disk.

    Parameters:
    path (string): Path to a page
    link (string): The "More information" link to insert.
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (string): Optionally, the language of the translation to be updated.

    Returns:
    str: Execution status
         "" if the page does not need an update or if the locale does not match language_to_update.
         "\x1b[36mlink added"
         "\x1b[34mlink updated"
         "\x1b[36mlink would be added"
         "\x1b[34mlink would updated"
    """

    locale = get_locale(path)
    if language_to_update != "" and locale != language_to_update:
        # return empty status to indicate that no changes were made
        return ""

    with path.open(encoding="utf-8") as f:
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

    # build new line
    if locale in ["bn", "hi", "ne"]:
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
        action = "updated"
    else:
        # add new line
        lines.insert(desc_end + 1, new_line)
        action = "added"

    status = get_status(action, dry_run, "link")

    if not dry_run:  # Only write to the path during a non-dry-run
        with path.open("w", encoding="utf-8") as f:
            f.writelines(lines)

    return status


def get_link(path: Path) -> str:
    """
    Determine whether the given path has a "More information" link.

    Parameters:
    path (Path): Path to a page

    Returns:
    str: "" If the path doesn't exit or does not have a link,
         otherwise return the "More information" link.
    """

    if not path.exists():
        return ""
    with path.open(encoding="utf-8") as f:
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


def sync(
    root: Path,
    pages_dirs: list[Path],
    command: str,
    link: str,
    dry_run: bool = False,
    language_to_update: str = "",
) -> list[Path]:
    """
    Synchronize a "More information" link into all translations.

    Parameters:
    root (Path): TLDR_ROOT
    pages_dirs (list of Path's): Path's of page entry and platform, e.g. "page.fr/common".
    command (str): A command like "tar".
    link (str): A link like "https://example.com".
    dry_run (bool): Whether to perform a dry-run, i.e. only show the changes that would be made.
    language_to_update (str): Optionally, the language of the translation to be updated.

    Returns:
    list (list of Path's): A list of Path's to be staged into git, using by --stage option.
    """
    paths = []
    for page_dir in pages_dirs:
        path = root / page_dir / command
        if path.exists():
            status = set_link(path, link, dry_run, language_to_update)
            if status != "":
                rel_path = "/".join(path.parts[-3:])
                paths.append(rel_path)
                print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))
    return paths


def main():
    parser = create_argument_parser(
        'Sets the "More information" link for all translations of a page'
    )
    parser.add_argument("link", type=str, nargs="?", default="")
    args = parser.parse_args()

    root = get_tldr_root()
    pages_dirs = get_pages_dir(root)

    target_paths = []

    # Use '--page' option
    if args.page != "":
        target_paths += get_target_paths(args.page, pages_dirs)

        for path in target_paths:
            rel_path = "/".join(path.parts[-3:])
            status = set_link(path, args.link, args.dry_run, args.language)
            if status != "":
                print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))

    # Use '--sync' option
    elif args.sync:
        pages_dirs.remove(root / "pages")
        en_path = root / "pages"
        platforms = [i.name for i in en_path.iterdir() if i.name not in IGNORE_FILES]
        for platform in platforms:
            platform_path = en_path / platform
            commands = [
                f"{platform}/{page.name}"
                for page in platform_path.iterdir()
                if page.name not in IGNORE_FILES
            ]
            for command in commands:
                link = get_link(root / "pages" / command)
                if link != "":
                    target_paths += sync(
                        root, pages_dirs, command, link, args.dry_run, args.language
                    )

    # Use '--stage' option
    if args.stage and not args.dry_run and len(target_paths) > 0:
        stage(target_paths)


if __name__ == "__main__":
    main()
