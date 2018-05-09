# jrnl

> A simple journal application for your command line.

- Insert new entry with your editor:

`jrnl`

- Quickly insert new entry:

`jrnl {{timestamp}}: {{title}}. {{content}}`

- View last ten entries:

`jrnl -n {{10}}`

- View everything that happened from the start of last year to the start of last march:

`jrnl -from {{"last year"}} -until {{march}}`

- Edit all entries tagged with @texas and @history:

`jrnl {{@texas}} -and {{@history}} --edit`
