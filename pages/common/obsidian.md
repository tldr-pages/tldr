# obsidian

> Command line interface for the Obsidian Markdown note-taking app.
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

- Read the contents of a file:

`obsidian read file={{path/to/file}}`
