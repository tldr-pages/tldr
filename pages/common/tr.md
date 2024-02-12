# tr

> Translate characters: run replacements based on single characters and character sets.
> More information: <https://www.gnu.org/software/coreutils/tr>.

- Replace all occurrences of a character in a file, and print the result:

`tr {{find_character}} {{replace_character}} < {{path/to/file}}`

- Replace all occurrences of a character from another command's output:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- Map each character of the first set to the corresponding character of the second set:

`tr '{{abcd}}' '{{jkmn}}' < {{path/to/file}}`

- Delete all occurrences of the specified set of characters from the input:

`tr -d '{{input_characters}}' < {{path/to/file}}`

- Compress a series of identical characters to a single character:

`tr -s '{{input_characters}}' < {{path/to/file}}`

- Translate the contents of a file to upper-case:

`tr "[:lower:]" "[:upper:]" < {{path/to/file}}`

- Strip out non-printable characters from a file:

`tr -cd "[:print:]" < {{path/to/file}}`
