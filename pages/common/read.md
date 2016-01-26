# read

> BASH builtin for retrieving data from standard input.

- Store data that you type from the keyboard:

`read {{variable}}`

- Store each of the next lines you enter as values of an array:

`read -a {{array}}`

- Enable backspace and GNU readline hotkeys when entering input with read:

`read -e {{variable}}`

- Specify the number of maximum characters to be read:

`read -n {{character_count}} {{variable}}`

- Use a specific character as a delimiter instead of a new line:

- store data that you type from the keyboard

`read {{variable}}`

- store each of the next lines you enter as values of an array

`read -a {{array}}`

- enable backspace and GNU readline hotkeys when entering input with read

`read -e {{variable}}`

- specify the number of maximum characters to be read

`read -n {{character_count}} {{variable}}`

- use a specific character as a delimiter instead of a new line

`read -d {{delimiter}} {{variable}}`
