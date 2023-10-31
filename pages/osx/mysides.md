# mysides

> add and remove folders to finder sidebar
> More information: <https://github.com/mosen/mysides>.

- List sidebar favorites items:

`mysides list`

- Add a new item to the end of the sidebar favorites:

`mysides add example file:///Users/Shared/example`

Remove an item by name:

`mysides remove example`

- Add the current directory to the sidebar:

`mysides add $(basename $(pwd)) file:///$(pwd)`

- Remove the current directory from the sidebar:

`mysides remove $(basename $(pwd))`