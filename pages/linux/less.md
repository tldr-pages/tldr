# less

> View file contents or command output one page at a time.
> Allows both forward and backward navigation through text.
> More information: <https://greenwoodsoftware.com/less/>.

- Open a file:

`less {{path/to/file}}`

- View command output one page at a time:

`{{command}} | less`

- Navigate forward and backward through file content:

`<Space> (forward), b (backward)`

- Search for a string (press `n` to go to next match, `N` to go to previous match):

`/{{search_string}}`

- Exit less:

`q`

- Display help about available commands:

`h`

- Go to a specific line number:

`g{{line_number}}`

- Open file at a specific position (n percent through the file):

`p{{percentage}}`
