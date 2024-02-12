# calibredb

> Manipulate an e-book database.
> Part of the Calibre e-book library.
> More information: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- List e-books in the library with additional information:

`calibredb list`

- Search for e-books displaying additional information:

`calibredb list --search {{search_term}}`

- Search for just ids of e-books:

`calibredb search {{search_term}}`

- Add one or more e-books to the library:

`calibredb add {{file1 file2 …}}`

- Recursively add all e-books under a directory to the library:

`calibredb add -r {{path/to/directory}}`

- Remove one or more e-books from the library. You need the e-book IDs (see above):

`calibredb remove {{id1 id2 …}}`
