# git mailinfo

> Extract patch and authorship information from a single email message.
> More information: <https://git-scm.com/docs/git-mailinfo>.

- Extract the patch and author data from an email message:

`git mailinfo {{message|patch}}`

- Extract but remove leading and trailing whitespace:

`git mailinfo -k {{message|patch}}`

- Remove everything from the body before a scissors line (e.g. "-->* --") and retrieve the message or patch:

`git mailinfo --scissors {{message|patch}}`
