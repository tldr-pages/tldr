# tr

> Translate characters: the tr utility will translate (i.e., substitute or delete) charaters from an input stream and output those results.

- Replace all occurrences of a character in a file, and print the result on the screen (file remains unchanged):

`tr {{find_character}} {{replace_character}} < {{filename}}`

- Replace all occurrences of a character from another command's output:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- Delete all occurrences of the specified set of characters from the input file and output to the screen:

`tr -d '{{input_characters}}' < {{filename}}`

- Compress a series of identical characters in a file to a single character and output to the screen:

`tr -s '{{input_characters}}' < {{filename}}`

- Translate the contents of a file to upper-case and output to the screen:

`tr "[:lower:]" "[:upper:]" < {{filename}}`

- Strip out non-printable characters from a file and output to the screen:

`tr -cd "[:print:]" < {{filename}}`
