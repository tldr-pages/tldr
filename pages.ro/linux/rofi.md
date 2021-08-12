# rofi

> Un lansator de aplicații și comutator de ferestre.
> Mai multe informaţii: <https://github.com/davatorium/rofi>

- Afișează lista de aplicații:

`rofi -show drun`

- Afișați lista tuturor comenzilor:

`rofi -show run`

- Comutarea între ferestre:

`rofi -show window`

- Pipe o listă de elemente pentru a stdin și imprima elementul selectat la stdout:

`printf "{{Choice1\nChoice2\nChoice3}}" | rofi -dmenu`
