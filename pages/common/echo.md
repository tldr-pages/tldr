# echo

> Print given arguments.

- Print a text message. Note: quotes are optional:

`echo "{{Hello World}}"`

- Print a message with environment variables:

`echo "{{My path is $PATH}}"`

- Print a message without the trailing newline:

`echo -n "{{Hello World}}"`

- Append a message to the file:

`echo "{{Hello World}}" >> {{file.txt}}`

- Enable interpretation of backslash escapes (special characters):

`echo -e "{{Column 1\tColumn 2}}"`
