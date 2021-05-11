# git mailinfo

> Extracts patch and authorship from a single e-mail message.
> More information: <https://git-scm.com/docs/git-mailinfo>.

- Extract the patch and author data from e-mail message:

`git mailinfo {{msg}} {{patch}}`

- Remove leading and trailing whitespace and other cruft:

`git mailinfo -k`

- Remove everything from the body before a scissors line (e.g. "-->* --") and retrieve the patch:

`git mailinfo --scissors {{patch}}`
