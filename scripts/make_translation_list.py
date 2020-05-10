#!/usr/bin/env python3
from glob import glob
from os import path, walk
from subprocess import run, PIPE, STDOUT
import jinja2

ISO_CODES = {
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "hbs": "Serbo-Croatian",
    "it": "Italian",
    "ja": "Javanese",
    "ko": "Korean",
    "pl": "Polish",
    "pt_BR": "Portugese (Brazillian)",
    "pt_PT": "Portugese",
    "ta": "Tamil",
    "zh": "Chinese",
}


def get_language_files(dirname: str) -> dict:
    def make_page_set(subdir):
        pages = set()
        for _, subdir, files in walk(subdir, topdown=False):
            for fname in files:
                if path.splitext(fname)[1] == ".md":
                    pages.add(fname)
        return pages

    lang_files = {}
    for lang_dir in glob(path.join(dirname, "pages*")):
        if lang_dir == path.join(dirname, "pages"):
            iso_code = "en"
        else:
            iso_code = lang_dir.split(".")[-1]
        lang_files[iso_code] = make_page_set(lang_dir)

    return lang_files


if __name__ == "__main__":
    git_dir = run(["git", "rev-parse", "--git-dir"], stdout=PIPE,
                  stderr=STDOUT).stdout.decode("UTF-8").strip(".git\n")
    lang_files = get_language_files(git_dir)
    all_files = set().union(*lang_files.values())
    missing_files = {ISO_CODES[k]: all_files.difference(v) for k, v in
                     lang_files.items()}
    with open("translation_list_template.j2", "r") as f:
        template = jinja2.Template(f.read())
    content = template.render(missing_files=missing_files)
    with open(path.join(git_dir, "NEEDTRANSLATING.md"), "w") as f:
        f.write(content)
