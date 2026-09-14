# gopls

> The official Go language server.
> More information: <https://go.dev/gopls/>.

- Start the language server:

`gopls serve`

- Show diagnostics for one or more files:

`gopls check {{path/to/file1.go path/to/file2.go ...}}`

- Format one or more files in-place:

`gopls format {{[-w|-write]}} {{path/to/file1.go path/to/file2.go ...}}`

- Add missing and remove unused imports in a file in-place:

`gopls imports {{[-w|-write]}} {{path/to/file.go}}`

- Show the definition of the identifier at a specific line and column:

`gopls definition {{path/to/file.go}}:{{line}}:{{column}}`

- List all references to the identifier at a specific line and column:

`gopls references {{path/to/file.go}}:{{line}}:{{column}}`

- Rename the identifier at a specific line and column, writing the changes to the affected files:

`gopls rename {{[-w|-write]}} {{path/to/file.go}}:{{line}}:{{column}} {{new_name}}`

- Display version:

`gopls version`
