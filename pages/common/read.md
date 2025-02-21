# read

> Shell builtin for retrieving data from `stdin`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-read>.

- Store data that you type from the keyboard:

`read {{variable}}`

- Store each of the next lines you enter as values of an array:

`read -a {{array}}`

- Specify the number of maximum characters to be read:

`read -n {{character_count}} {{variable}}`

- Assign multiple values to multiple variables:

`read {{_ variable1 _ variable2}} <<< "{{The surname is Bond}}"`

- Do not let backslash (\\) act as an escape character:

`read -r {{variable}}`

- Display a prompt before the input:

`read -p "{{Enter your input here: }}" {{variable}}`

- Do not echo typed characters (silent mode):

`read -s {{variable}}`

- Read `stdin` and perform an action on every line:

`while read line; do {{echo|ls|rm|...}} "$line"; done < {{/dev/stdin|path/to/file|...}}`
