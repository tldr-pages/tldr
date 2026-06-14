# unhash

> Հեռացրեք հաշված գործարկվող վայրերը:.
> Տես նաև՝ `hash`:.
> Լրացուցիչ տեղեկություններ. <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>:.

- Հեռացրեք հատուկ հրամանը հեշ աղյուսակից.:

`unhash {{command}}`

- Unhash ոչ վերջածանց [a]liases:

`unhash -a {{alias}}`

- Unhash [s] endifix aliases:

`unhash -s {{alias}}`

- Unhash shell [f]unctions:

`unhash -f {{function}}`

- Unhash [d]rectories:

`unhash -d {{directory}}`

- Անջատեք յուրաքանչյուր ֆունկցիա, որը [m] կպչում է օրինաչափությանը.:

`unhash -f -m "{{pattern}}"`
