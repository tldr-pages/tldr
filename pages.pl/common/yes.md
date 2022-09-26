# yes

> Wypisuje coś wielokrotnie.
> Komenda używana często aby potwierdzić pytania zadawane przez komendy instalujące takie jak apt-get.
> Więcej informacji: <https://www.gnu.org/software/coreutils/yes>.

- Wypisuje bez końca "wiadomość":

`yes {{wiadomość}}`

- Wypisuje bez końca "y":

`yes`

- Wysyłaj potwierdzenie dla każdego pytania zadanego przez `apt-get`:

`yes | sudo apt-get install {{program}}`
