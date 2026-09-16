# jj gerrit

> Interact with gerrit to upload changes for code review, or update existing changes.
> See also: `jj git push`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-gerrit-upload>.

- Upload the current change (or its parent if the working copy has no description):

`jj gerrit upload`

- Upload a specific revision:

`jj gerrit upload {{[-r|--revision]}} {{revset}}`

- Upload multiple specific revsets:

`jj gerrit upload {{[-r|--revision]}} {{revset1}} {{[-r|--revision]}} {{revset2}}`

- Upload a revision targeting a specific remote branch for merging:

`jj gerrit upload {{[-r|--revision]}} {{revset}} {{[-b|--remote-branch]}} {{branch}}`

- Upload to a specific Gerrit remote:

`jj gerrit upload --remote {{remote}}`

- Upload and add reviewers and CC recipients by email (flags can be repeated):

`jj gerrit upload --reviewer {{reviewer@example.com}} --cc {{cc@example.com}}`

- Upload while suppressing non-essential output:

`jj gerrit upload --quiet`

- Preview what would be uploaded without pushing to Gerrit:

`jj gerrit upload {{[-n|--dry-run]}}`
