# aspell

> Interactive spell checker.

- Spell check a single file:

`aspell check file`

- List mispelled words from standard input:

`cat file | aspell list`

- Show available dictionary files:

`aspell dicts`

- Run aspell with different language (takes two letter ISO 639 language code):

`aspell --lang=lang-code`

- List mispelled words from standard input and ignore words from personal word list:

`cat file |aspell --personal=personal-word-list.pws --dont-suggest list`
