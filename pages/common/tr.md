# tr

> Translate characters - run replacements based on single characters and character sets.

- Replace all occurrences of a character in a file, and print the result:

`tr {{find_characters}} {{replace_characters}} < {{filename}}`

- Map each character of the first set to the corresponding character of the second set:

`tr 'abcd' 'jkmn' < {{filename}}`

- Delete all occurances of the specified set of characters from the input:

`tr -d '{{input_characters}}'`

- Compress a series of identical characters to a single character:

`tr -s '\n'`

- Translate the contents of the file to upper-case and print result:

`tr "[:lower:]" "[:upper:]" < {{filename}}`

- Strip out non-printable characters from the file and print result:

`tr -cd "[:print:]" < {{filename}}`
