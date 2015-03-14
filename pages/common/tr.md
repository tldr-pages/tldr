# tr

> translate characters - run replacements based on single characters and character sets

- Replace all occurrences of a character in a file, and prints the result

`tr {{find_characters}} {{replace_characters}} < {{filename}}`

- Maps each character of the first set to the corresponding character of the second set.

`tr 'abcd' 'jkmn' < {{filename}}`

- Delete all occurances of the specified set of characters from the input.

`tr -d '{{input_characters}}'`

- Compresses a series of identical characters to a single character.

`tr -s '\n'`

- Translate the contents of the file to upper-case, prints result.

`tr "[:lower:]" "[:upper:]" < {{filename}}`

- Strip out non-printable characters from the file, prints result.

`tr -cd "[:print:]" < {{filename}}`
