# nb

> Command-line note-taking, bookmarking, and archiving tool.
> Supports encryption, tagging, wiki-style links, Git syncing, Pandoc conversion, and more.
> More information: <https://github.com/xwmx/nb>


- Create a new note in your `$EDITOR`:

`nb add "{{note_title}}"`

- Edit a note in your `$EDITOR`:

`nb edit {{note_id}}`

- Add a bookmark:

`nb {{url}}`

- List all notes in the current notebook:

`nb list`

- Add a todo:

`nb todo add {{title}}`

- Add a task: 

`nb task add {{title}}`

- Import a file:

`nb import ({{path}} | {{url}})`

- Search for notes containing a keyword:

`nb search "{{keyword}}"`

- Sync notes via Git:

`nb sync`

- Convert a note to another format using Pandoc:

`nb export "{{note_title}}" --to pdf`

- Help information:

`nb help`