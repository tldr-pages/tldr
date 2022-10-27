# tlmgr repository

> Manage repositories of a TeX Live installation.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all configured repositories and their tags (if set):

`tlmgr repository list`

- List all packages available in a specific repository:

`tlmgr repository list {{path|url|tag}}`

- Add a new repository with a specific tag (the tag is not required):

`sudo tlmgr repository add {{path|url}} {{tag}}`

- Remove a specific repository:

`sudo tlmgr repository remove {{path|url|tag}}`

- Set a new list of repositories, overwriting the previous list:

`sudo tlmgr repository set {{path|url|tag}}#{{tag}} {{path|url|tag}}#{{tag}} {{...}}`

- Show the verification status of all configured repositories:

`tlmgr repository status`
