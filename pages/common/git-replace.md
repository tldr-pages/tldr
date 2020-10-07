# git replace

> Create, list, delete refs to replace objects.
> More information: <https://linux.die.net/man/1/git-replace>.

- Replace any commit with a different one, rest commits unchanged:

`git replace {{object}} {{replacement}}`

- Delete existing replace refs for the given objects:

`git replace --delete {{object}}`

- Edit an object’s content interactively:

`git replace --edit {{object}}`
