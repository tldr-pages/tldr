#!/usr/bin/env python3
from glob import glob
from os import path
from functools import partial
from subprocess import run, PIPE, STDOUT
import requests as r
import re
from multiprocessing.dummy import Pool

from make_translation_list import get_git_root


def get_changed_files() -> set:
    diff_lines = run(["git", "diff", "--cached", "--name-status"],
                     stdout=PIPE, stderr=STDOUT).stdout.decode(
        "UTF-8").splitlines()
    changed_files = set()
    for line in diff_lines:
        if m := re.search(r"^[A-Z]\s+(pages.*)", line):
            changed_files.add(m.group(1))
    return changed_files


def find_translations(filepath: str) -> set:
    lang_dirs = glob(path.join(get_git_root(), "pages*"))
    fp_lang_relative = filepath.split("/", 1)[1]
    translations = set()
    for d in lang_dirs:
        translation_path = path.join(d.split("/")[-1], fp_lang_relative)
        if translation_path != filepath:
            translations.add(translation_path)
    return translations


def get_recent_contribs(filename: str, shared_dict: dict):
    resp = r.get(
        "https://api.github.com/repos/tldr-pages/tldr/commits",
        params={"path": filename},
    )
    resp.raise_for_status()
    shared_dict[path.basename(filename)] = \
        set([commit["author"]["login"] for commit in resp.json()][:5])


def make_translator_comment_body() -> str:
    files = set()
    for f in get_changed_files():
        files.update(find_translations(f))
    contrib_dict = {}
    Pool().map(partial(get_recent_contribs, shared_dict=contrib_dict), files)
    # remove empty results
    contrib_dict = {k: v for k, v in contrib_dict.items() if v}
    comment_body = ""
    for k, v in contrib_dict.items():
        line = f"* {k}: "
        for contrib in v:
            line += f"@{contrib} "
        comment_body += line.rstrip() + "\n"
    return comment_body
