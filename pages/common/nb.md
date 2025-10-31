# nb

> Command-line note-taking, bookmarking, and archiving tool.
> Supports encryption, tagging, wiki-style links, Git syncing, Pandoc conversion, and more.
> More information: <https://github.com/xwmx/nb>.

- Create a new note in your `$EDITOR`:

`nb add "{{note_title}}"`

- Edit a note in your `$EDITOR`:

`nb edit {{note_id}}`

- List all notes in the current notebook:

`nb list`

- Add a todo:

`nb todos add {{title}}`

- Import a file:

`nb import ({{path}} | {{url}})`

- Search for notes containing a keyword:

`nb search "{{keyword}}"`

- Sync notes via Git:

`nb sync`

- Help information:

`nb help`
