# nb

> Note-taking, bookmarking, and archiving tool.
> Supports encryption, tagging, wiki-style links, Git syncing, Pandoc conversion, and more.
> More information: <https://github.com/xwmx/nb#-help>.

- Create a new note in your `$EDITOR`:

`nb {{[a|add]}} "{{note_title}}"`

- Edit a note in your `$EDITOR`:

`nb {{[e|edit]}} {{note_id}}`

- List all notes in the current notebook:

`nb list`

- Add a todo:

`nb {{[to|todos]}} {{[a|add]}} {{title}}`

- Import a file:

`nb import ({{path/to/file|url}})`

- Search for notes containing a keyword:

`nb {{[q|search]}} "{{keyword}}"`

- Sync notes via Git:

`nb sync`

- Display help:

`nb help`
