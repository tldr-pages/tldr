# obsidian

> Command-line interface for the Obsidian Markdown note-taking app.
> Note: Requires the Obsidian app to be running.
> More information: <https://obsidian.md/help/cli>.

- Open today's daily note:

`obsidian daily`

- Append a task to today's daily note:

`obsidian daily:append content="- [ ] {{task}}"`

- Create a new note from a template:

`obsidian create name="{{note_name}}" template={{template_name}}`

- Search the vault for text:

`obsidian search query="{{search_query}}"`

- List all incomplete tasks in the vault:

`obsidian tasks todo`

- Read a specific note:

`obsidian read file={{note_name}}`

- Read a note at a specific path relative to the vault root:

`obsidian read path={{path/to/note.md}}`

- Read the active note:

`obsidian read`
