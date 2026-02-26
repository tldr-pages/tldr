# Personal repositories guide

This guide describes a recommended layout for personal tldr page repositories ("taps").
Support for taps is optional and client-dependent.

## Goal

Personal repositories allow users to keep private, team-specific, or workflow-specific examples
without changing the official `tldr-pages/tldr` content.

## Recommended repository structure

Use the same page directory layout as the main repository:

- `pages/`
  - `common/`
  - `linux/`
  - `windows/`
  - `osx/`
  - ...etc.
- `pages.<locale>/` for translations (optional), using POSIX locale names.

Each command page should be a `.md` file using the same naming rules as official pages:

- `git checkout` -> `git-checkout.md`
- mixed case names are lowercased (`eyeD3` -> `eyed3.md`)

## Content recommendations

If a client appends personal additions to the official page output, keep pages focused on examples:

- use regular example descriptions (`- ...`) and example command lines (`` `...` ``)
- avoid duplicating generic command descriptions from the official page
- keep examples short, practical, and specific to your environment or conventions

## Distribution and updates

It is recommended to distribute personal repositories through git and version them with normal tags or branches.
Clients can then clone and update repositories through regular git operations.

## Compatibility note

Clients may implement personal repositories differently.
Repository authors should test pages with the specific client(s) they intend to use.
