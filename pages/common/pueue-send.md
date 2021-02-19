# pueue send

> Send input to a task.

- Send input to a running command:

`pueue send {{task ID}} {{input}}`

- Send confirmation to a task expecting y/N (e.g. apt, cp):

`pueue send {{task ID}} y`

- Write to a file open in background:

`pueue add cat > {{location/to/file}}; sleep 3h; pueue send {{task ID}} {{some text}}`
