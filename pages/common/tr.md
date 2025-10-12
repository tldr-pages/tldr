# tr

> Translate characters: run replacements based on single characters and character sets.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Replace all occurrences of a character in a file, and print the result:

`tr < {{path/to/file}} {{find_character}} {{replace_character}}`

- Replace all occurrences of a character from another command's output:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- Map each character of the first set to the corresponding character of the second set:

`tr < {{path/to/file}} '{{abcd}}' '{{jkmn}}'`

- Delete all occurrences of the specified set of characters from the input:

`tr < {{path/to/file}} {{[-d|--delete]}} '{{input_characters}}'`

- Compress a series of identical characters to a single character:

`tr < {{path/to/file}} {{[-s|--squeeze-repeats]}} '{{input_characters}}'`

- Translate the contents of a file to upper-case:

`tr < {{path/to/file}} "[:lower:]" "[:upper:]"`

- Strip out non-printable characters from a file:

`tr < {{path/to/file}} {{[-cd|--complement --delete]}} "[:print:]"`
