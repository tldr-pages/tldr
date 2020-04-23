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

`read -d {{new_delimiter}} {{variable}}`

- Do not let backslash (\) act as an escape character:

`read -r {{variable}}`

- Display a prompt before the input:

`read -p {{"Enter your input here: "}} {{variable}}`

- Do not echo typed characters (silent mode):

`read -s {{variable}}`
