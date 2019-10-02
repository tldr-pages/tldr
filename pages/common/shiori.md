# shiori

> Simple bookmark manager built with Go.
> More information: <https://github.com/go-shiori/shiori>.

- Import bookmarks from HTML Netscape bookmark format file:

`shiori import {{path/to/bookmarks.html}}`

- Save the specified URL as bookmark:

`shiori add {{url}}`

- List the saved bookmarks:

`shiori print`

- Open the saved bookmark in a browser:

`shiori open {{bookmark_id}}`

- Start the web interface for managing bookmarks at port 8181:

`shiori serve --port {{8181}}`
