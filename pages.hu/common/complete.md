# complete

> Automatikus argumentum-kiegészítést biztosít a shell parancsokhoz. További információ: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>.

- Olyan függvény alkalmazása, amely automatikus kiegészítést végez egy parancsra:

`complete -F {{function}} {{command}}`

- Alkalmazza az automatikus kiegészítést végző parancsot egy másik parancsra:

`complete -C {{autocomplete_command}} {{command}}`

- Alkalmazza az automatikus kitöltést anélkül, hogy szóközt csatolna a kitöltött szóhoz:

`complete -o nospace -F {{function}} {{command}}`
