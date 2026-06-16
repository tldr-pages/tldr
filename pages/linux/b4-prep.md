# b4 prep

> Prepare a new patch series for submission to a mailing list.
> More information: <https://b4.docs.kernel.org/en/latest/contributor/prep.html>.

- Start a new patch series branch forked from a specific point:

`b4 prep {{[-n|--new]}} {{series_name}} {{[-f|--fork-point]}} {{fork_point}}`

- Edit the cover letter for the current series:

`b4 prep --edit-cover`

- Automatically populate the cover letter with recipients from commit trailers and maintainer files:

`b4 prep {{[-c|--auto-to-cc]}}`

- Run local checks (e.g., `checkpatch.pl`) on the series:

`b4 prep --check`

- Enroll an existing branch as a b4-prep-managed branch:

`b4 prep {{[-e|--enroll]}} {{base_branch}}`

- Archive and clean up an obsolete prep-managed branch:

`b4 prep --cleanup {{branch_name}}`
