# aspell

> Interactive spell checker.
> More information: <http://aspell.net/>.

- Spell check a single file:

`aspell check {{path/to/file}}`

- List misspelled words from standard input:

`cat {{file}} | aspell list`

- Show available dictionary languages:

`aspell dicts`

- Run `aspell` with a different language (takes two-letter ISO 639 language code):

`aspell --lang={{cs}}`

- List misspelled words from standard input and ignore words from personal word list:

`cat {{file}} | aspell --personal={{personal-word-list.pws}} list`
