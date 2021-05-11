# git mailinfo

> Extracts patch and authorship from a single e-mail message.
> More information: <https://git-scm.com/docs/git-mailinfo>.

- Extract the patch and author data from e-mail message:

`git mailinfo {{message|patch}}`

- Extract but remove leading and trailing whitespace:

`git mailinfo -k {{message}}|{{patch}}`

- Remove everything from the body before a scissors line (e.g. "-->* --") and retrieve the message or patch:

`git mailinfo --scissors {{message|patch}}`
