# micro

> Micro is a terminal-based text editor that aims to be easy to use and intuitive, while also taking advantage of the full capabilities of modern terminals.
> You can use your keyboard, but also your mouse to navigate and/or select text.

- Open a file:

`micro {{file}}`

- Cut the entire line:

`<Ctrl>k`

- Search for a pattern in the file (press `<Ctrl>n`/`<Ctrl>p` to go to next/previous match):

`<Ctrl>f "{{pattern}}" <Enter>`

- Execute a command:

`<Ctrl>e {{command}} <Enter>`

- Perform a substitution in the whole file:

`<Ctrl>e replaceall "{{pattern}}" "{{replacement}}" <Enter>`

- Quit:

`<Ctrl>q`
