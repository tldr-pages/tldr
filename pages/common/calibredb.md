# calibredb

> Tool to manipulate the your eBook database.
> Part of the Calibre eBook library.
> More information: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- List eBooks in the library with additional information:

`calibredb list`

- Search for eBooks displaying additional information:

`calibredb list --search {{search_term}}`

- Search for just ids of eBooks:

`calibredb search {{search_term}}`

- Add one or more eBooks to the library:

`calibredb add {{file1 file2 …}}`

- Recursively add all eBooks under a directory to the library:

`calibredb add -r {{path/to/directory}}`

- Remove one or more eBooks from the library. You need the eBook IDs (see above):

`calibredb remove {{id1 id2 …}}`
