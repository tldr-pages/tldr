# mysides

> Add, list and remove finder favorites.
> More information: <https://github.com/mosen/mysides>.

- List sidebar favorites:

`mysides list`

- Add a new item to the end of the sidebar favorites:

`mysides add {{example}} {{file:///Users/Shared/example}}`

- Remove an item by name:

`mysides remove {{example}}`

- Add the current directory to the sidebar:

`mysides add $(basename $(pwd)) file:///$(pwd)`

- Remove the current directory from the sidebar:

`mysides remove $(basename $(pwd))`
