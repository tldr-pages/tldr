# dnote

> A multi-device notebook for capturing commands, snippets, and notes.
> More information: <https://www.getdnote.com/docs/cli/commands/>.

- Add a note to a book in the configured editor:

`dnote add {{book_name}}`

- Add a note with inline content:

`dnote add {{book_name}} {{[-c|--content]}} "{{note_content}}"`

- List all books and notes:

`dnote view`

- View all notes in a specific book:

`dnote view {{book_name}}`

- Search notes using full-text search:

`dnote find "{{keywords}}"`

- Edit a specific note by its ID:

`dnote edit {{note_id}}`

- Remove a note or an entire book:

`dnote remove {{note_id|book_name}}`

- Synchronize notes with a Dnote server:

`dnote sync`
