# clear

> Șterge ecranul terminalului.
> Mai multe informaţii: <https://manned.org/clear>

- Goliți ecranul (echivalent cu apăsarea Control-L în shell-ul Bash):

`clear`

- Ștergeți ecranul, dar păstrați tamponul de derulare înapoi al terminalului:

`clear -x`

- Indicați tipul de terminal de curățat (valorile implicite ale variabilei de mediu „TERM”):

`clear -T {{type_of_terminal}}`

- Arată versiunea `ncurses` utilizată de `clear`:

`clear -V`
