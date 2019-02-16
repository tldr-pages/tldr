# rbt

> RBTools is a set of command line tools for working with Review Board and RBCommons.
> Homepage: <https://www.reviewboard.org/docs/rbtools/dev/>.

- Posts changes to Review Board:

`rbt post {{changenum}}`

- Displays the diff that will be sent to Review Board:

`rbt diff`

- Lands a change in a local branch or on a review request:

`rbt land {{branchname}}`

- Patches your tree with a change on a review request:

`rbt patch {{reviewrequestid}}`

- Sets up RBTools to talk to your repository:

`rbt setup-repo`
