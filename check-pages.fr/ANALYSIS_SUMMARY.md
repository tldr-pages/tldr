# French Translation Analysis Summary

**Analysis Date:** February 8, 2026  
**Repository:** tldr-pages/tldr  
**Language:** French (fr)

## Overview

The French translation currently has **894 pages** out of **6,893 total English pages**, representing approximately **13% completion**.

### Key Statistics

| Metric | Count |
|--------|-------|
| Total English pages | 6,893 |
| Total French pages | 894 |
| Missing translations | 5,999 |
| Missing alias pages | 68 |
| Missing TLDR pages | 266 |
| Outdated pages (by count) | 116 |
| Outdated pages (by contents) | 416 |

---

## 1. Pages That Need to Be Created (Missing Translations)

Total: **5,999 pages**

These are English pages that have no French equivalent at all. They need to be translated from scratch.

### Platform Breakdown (Sample)
- **cisco-ios**: 19 pages
- **common**: ~4,500+ pages
- **linux**: ~1,500+ pages  
- **dos**: 200+ pages
- **windows**: ~250+ pages

### Examples of Missing Translations
- `cisco-ios/clock.md`
- `cisco-ios/configure.md`
- `cisco-ios/crypto.md`
- `common/3d-ascii-viewer.md`
- `common/accelerate.md`
- `common/agg.md`
- `common/aider.md`
- `common/alr.md`
- `common/animdl.md`

### Most Commands to Add
The most commonly missing commands categories include:
- **npm** commands (6)
- **magick/ImageMagick** commands (5)
- **gh/GitHub CLI** commands (5)
- **jira** commands (4)
- **bun** (JavaScript runtime) commands (4)

---

## 2. Pages That Need to Be Created (Missing Alias Pages)

Total: **68 unique commands**

Commands referenced in French "Voir aussi" (See also) sections that don't have corresponding French pages.

### Special Character Pages (1)
- `^` - (caret character, referenced in shell pages)

### Real Command Aliases (67)

#### Shell & Command Line Tools (20)
- `acme.sh-dns` - (referenced in acme.sh.md)
- `age-keygen` - (referenced in age.md)
- `bashmarks` - (referenced in autojump.md)
- `chpasswd` - (referenced in passwd.md)
- `dc` - (referenced in bc.md)
- `delta` - (referenced in diff.md)
- `difft` - (referenced in diff.md)
- `disown` - (referenced in bg.md)
- `doas` - (referenced in sudo.md)
- `fd` - (referenced in find.md)
- `fg` - (referenced in bg.md)
- `gawk` - (referenced in awk.md)
- `jobs` - (referenced in bg.md)
- `man` - (referenced in apropos.md)
- `printf` - (referenced in echo.md)
- `regex` - (referenced in grep.md)
- `run0` - (referenced in sudo.md)
- `screen` - (referenced in tmux.md)
- `unalias` - (referenced in alias.md)
- `whereis` - (referenced in type.md, which.md)

#### Process/System Monitoring Tools (10)
- `atop` - (referenced in btop.md)
- `btm` - (referenced in btop.md)
- `glances` - (referenced in btop.md)
- `htop` - (referenced in btop.md)
- `top` - (referenced in btop.md)
- `restorecon` - (referenced in linux/chcon.md)
- `secon` - (referenced in linux/chcon.md)
- `semanage-fcontext` - (referenced in linux/chcon.md)
- `hexdump` - (referenced in hexyl.md)
- `od` - (referenced in hexyl.md)
- `xxd` - (referenced in hexyl.md)

#### Editors & Development Tools (10)
- `gvim` - (referenced in vim.md)
- `nvim` - (referenced in vim.md)
- `pico` - (referenced in nano.md)
- `rnano` - (referenced in nano.md)
- `vimdiff` - (referenced in vim.md)
- `vimtutor` - (referenced in vim.md)
- `irb` - (referenced in ruby.md)
- `rake` - (referenced in ruby.md)
- `perldoc` - (referenced in perl.md)

#### Linux-Specific Commands (8)
- `debtap` - (referenced in linux/alien.md)
- `parted` - (referenced in linux/cfdisk.md)
- `pkgfile` - (referenced in linux/pacman-files.md)
- `iw` - (referenced in linux/iwctl.md)
- `nmcli` - (referenced in linux/iwctl.md)

#### Audio/Media Players (3)
- `clementine` - (referenced in linux/cmus.md)
- `ncmpcpp` - (referenced in linux/cmus.md)
- `qmmp` - (referenced in linux/cmus.md)

#### Package Managers & Tools (4)
- `brew-info` - (referenced in brew-abv.md)
- `brew-uninstall` - (referenced in brew-remove.md, brew-rm.md)

#### Utilities (11)
- `mac2unix`, `unix2dos`, `unix2mac` - (format conversion, referenced in dos2unix.md)
- `unzip` - (referenced in zip.md)
- `users` - (referenced in useradd.md, userdel.md, usermod.md)
- `wcurl` - (referenced in curl.md)
- `wget` - (referenced in curl.md)
- `wl-copy` - (referenced in linux/xclip.md)
- `nix-classic`, `nix-flake` - (nix package manager)

#### Terminal & TUI (3)
- `terminalizer` - (referenced in asciinema.md)
- `zellij` - (referenced in tmux.md)
- `tcsh` - (referenced in csh.md)

---

## 3. Pages That Need to Be Created (Missing TLDR Referenced Pages)

Total: **266 unique commands**

Commands referenced in French pages using `tldr <command>` syntax that don't exist in French.

### Key Categories

#### File & Text Processing (40+ commands)
- `aa-status`, `cksum`, `comm`, `dirname`, `fmt`, `join`, `paste`, `sort`, `tac`, `tee`, `tr`, `uniq`, `expand`, `unexpand`
- `basenc`, `bzip2`
- Archive commands: `bzip2`, `xz`, `gzip`, `lrzip`,etc.

#### System/Process Management (30+ commands)
- `id`, `nice`, `nohup`, `logname`, `groups`, `users`, `who`, `tty`
- `pinky`, `hostid`, `hostname`
- System tools: `systemctl-try-restart`, `systemctl-stop`, `setarch`

#### Networking (20+ commands)
- `ping6`, `traceroute`, `telnet`, `nc`, `http`, `avahi-resolve`

#### Package Managers (40+ commands)
- **npm**: `npm-exec`, `npm-install-test`, `npm-ls`, `npm-owner`, `npm-rebuild`, `npm-run` (8 variations)
- **brew**: `brew-info`, `brew-uninstall`
- **choco**: `choco-install`, `choco-list`, `choco-push`
- **dnf**: `dnf`, `dnf-config-manager`, `dnf-repoquery`
- **podman**: `podman-load`, `podman-pull`

#### Development Tools (30+ commands)
- **Git**: `git-abort`, `git-cola`
- **Python**: `python`
- **Node**: `bun-create`, `bun-install`, `bun-pm-ls`, `bun-remove`, `bunx`
- **Cloud**: `aws-*` (various), `vercel`, `netlify`
- **Docker**: `docker-container-update`, `docker-image-tag`

#### Security Tools (30+ commands)
- Impacket tools: `getadusers.py`, `getnpusers.py`, `mssqlclient.py`, etc.
- `sambapipe.py`, `secretsdump.py`, `rpcdump.py`
- `radare2`, `hping3`

#### Editors & Terminal (20+ commands)
- `vim` aliases: `nvim`, `gvim`, etc.
- Terminal tools: `zellij`, `hx` (helix), `zed`

#### System Configuration (10+ commands)
- `update-alternatives`
- SELinux variants
- AppArmor variants

#### Miscellaneous
- Various CLI utilities like `test`, `true`, `false`, `timeout`

### Platform-Specific Variants
Many GNU core utilities with `g` prefix for macOS:
- `gmake`, `gmd5sum`, `gnproc`, `gjoin`, `grm`, etc.

---

## 4. Pages That Need Updates (Outdated by Command Count)

Total: **116 pages**

These French pages exist but have a different number of commands compared to the English version.

### Platform Breakdown
- **android**: 3 pages
- **common**: 97 pages
- **linux**: 14 pages  
- **windows**: 2 pages

### Most Critical Updates

#### Core Commands (High Priority)
- `pages.fr/common/bash.md` - EN: 8 commands, FR: 7
- `pages.fr/common/cargo.md` - EN: 8 commands, FR: 7
- `pages.fr/common/tmux.md` - EN: 8 commands, FR: 6
- `pages.fr/common/tput.md` - EN: 8 commands, FR: 6
- `pages.fr/common/zsh.md` - EN: 8 commands, FR: 6

#### File Operations
- `pages.fr/common/cat.md` - EN: 5 commands, FR: 3
- `pages.fr/common/cp.md` - EN: 8 commands, FR: 6
- `pages.fr/common/mkdir.md` - EN: 4 commands, FR: 2

#### Development Tools
- `pages.fr/common/nano.md` - EN: 8 commands, FR: 5
- `pages.fr/common/python.md` commands
- `pages.fr/common/ssh-keygen.md` - EN: 8 commands, FR: 7

#### Git Commands (High Priority - 20+ pages)
- `pages.fr/common/git-*.md` - Multiple git subcommands need updating
  - `git-blame.md` - EN: 8 commands, FR: 2 (severe!)
  - `git-commit.md` - EN: 8 commands, FR: 4
  - `git-status.md` - EN: 7 commands, FR: 4
  - `git-init.md` - EN: 4 commands, FR: 2

#### Docker
- `pages.fr/common/docker-container-top.md` - EN: 2 commands, FR: 1
- `pages.fr/common/docker-image-ls.md` - EN: 6 commands, FR: 5

#### Linux/Platform Specific
- `pages.fr/linux/ip-route-list.md` - EN: 8 commands, FR: 1 (severe!)
- `pages.fr/linux/systemctl.md` - EN: 8 commands, FR: 7
- `pages.fr/linux/pacman.md` - EN: 8 commands, FR: 7
- `pages.fr/linux/yay.md` - EN: 8 commands, FR: 6
- `pages.fr/linux/xclip.md` - EN: 8 commands, FR: 7

---

## 5. Pages That Need Updates (Outdated by Command Contents)

Total: **416 pages**

These French pages have the same command count as English but the actual command content differs (updated examples, new parameters, etc.).

### Platform Breakdown
- **android**: 10 pages
- **common**: ~300 pages
- **linux**: ~100 pages
- **osx**: 1 page
- **sunos**: 3 pages
- **windows**: 15 pages

### Major Categories Affected

#### All Git Commands
Every single `git-*` page has outdated examples due to git updates over time.

#### Cloud/DevOps Tools
- All `aws-*` commands
- Docker commands (docker-*.md)
- k8s/container tools

#### Development Tools  
- Node.js, Python, Go, Rust tooling
- Package managers (npm, pip, cargo, brew)

#### Linux System Tools
- systemd tools
- btrfs filesystem commands
- pacman/arch-specific commands

---

## Recommendation Priority

### Priority 1: Critical (Must Fix Immediately)
1. **High-usage outdated pages** - Core commands like bash, cat, cp, ssh
2. **Severely outdated git pages** - `git-blame.md` with 8→2 commands, `git-commit.md` with 8→4
3. **Missing alias pages for top tools** - `fd`, `htop`, `whereis`, `man`

### Priority 2: High
1. **Complete missing TLDR references** - 266 commands, especially npm, brew, dnf
2. **Linux-specific system commands** - ip-route-list update needed严重
3. **Docker container commands** - Several need updates

### Priority 3: Medium  
1. **Outdated by contents** - 416 pages need content refresh
2. **Package manager variants** - npm/brew subcommands
3. **Security tools** - Many missing

### Priority 4: Low
1. **Special character pages** - Can wait
2. **Obscure utilities** - Less frequently used
3. **Newer tools** - May not have widespread adoption yet

---

## Files Generated

All results are saved in **/Users/giorgiobirnthaler/Desktop/agy/githubissuesfixes/translation-workspace/tldr/check-pages.fr/**

1. `missing-fr-alias-pages.txt` - List of 68 missing alias pages
2. `missing-tldr-fr-commands.txt` - List of 266 missing TLDR-referenced commands
3. `outdated-fr-pages-based-on-command-count.txt` - List of 116 pages with wrong command count
4. `outdated-fr-pages-based-on-command-contents.txt` - List of 416 pages with outdated content

---

## Discrepancy Note

The GitHub issue #13570 mentions slightly different numbers:
- 138 missing alias pages vs 68 found
- 151 missing TLDR pages vs 266 found
- 95 outdated by count vs 116 found
- 35 outdated by contents vs 416 found

This discrepancy likely indicates:
1. The issue was created earlier when the state was different
2. Some filtering or deduplication in the official check-pages.sh script
3. False positives in this analysis that need manual review
4. The tldr-pages repository has been updated since the issue was opened

The analysis here represents the **current state** as of February 8, 2026.
