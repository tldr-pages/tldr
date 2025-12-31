# jrnl

> A simple journal application.
> More information: <https://jrnl.sh/en/stable/reference-command-line/>.

- Insert a new entry with your editor:

`jrnl`

- Quickly insert a new entry:

`jrnl {{today at 3am}}: {{title}}. {{content}}`

- View the last ten entries:

`jrnl -n {{10}}`

- View everything that happened from the start of last year to the start of last march:

`jrnl -from "{{last year}}" -until {{march}}`

- Edit all entries tagged with "texas" and "history":

`jrnl {{@texas}} -and {{@history}} --edit`
