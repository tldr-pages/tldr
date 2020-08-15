# git send-email

> Send a collection of patches as emails.
> Patches can be specified as files, directions, or a revision list.
> More information: https://git-scm.com/docs/git-send-email

- Send the last commit in the current branch:

`git send-email -1`

- Send a given commit:

`git send-email -1 {{commit}}`

- Send multiple (e.g. 10) commits in the current branch:

`git send-email -10`

- Send an extra mail before the patch mail(s) (e.g. an introduction to the patch set as a cover letter) and edit the mail(s) to be sent:

`git send-email -{{number of commits} --cover-letter --annotate

- Send the last commit in the current branch with the patch version (e.g. 2) indicated in the subject header (to appear as [PATCH v2]):

`git send-email -v2 -1`