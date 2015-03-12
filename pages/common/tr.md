# tr

> translate characters - run replacements based on single characters

- replace all occurrences of a character in a file, and print the result

`tr {{find_character}} {{replace_character}} < {{filename}}`

 Translate the contents of the file to upper-case, prints result.

`tr "[:lower:]" "[:upper:]" < {{filename}}`

Strip out non-printable characters from the file, prints result.

`tr -cd "[:print:]" < {{filename}}`
