# grex

> Simple command line tool to generate regular expressions. 
> More information: https://github.com/pemistahl/grex.

- Simple regex generation:

` grex {{space_separated_strings}}`

- Case insensitive regex generation:

`grex -i {{space_separated_strings}}`
	
- Replace digits with '\d':

`grex -d {{space_separated_strings}}`
	
- Replace unicode word character with '\w':

`grex -w {{space_separated_strings}}`

- Replace spaces with '\s':

`grex -s {{space_separated_strings}}`

- Adding {min, max} quantifier representation for repeating sub-strings:

`grex -r {{space_separated_strings}}`
