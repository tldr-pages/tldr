# yes

> Wypisuje coś wielokrotnie.
> Komenda używana często aby potwierdzić pytania zadawane przez komendy instalujące takie jak `apt-get`.
> Więcej informacji: <https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- Wypisuj bez końca "wiadomość":

`yes {{wiadomość}}`

- Wypisuj bez końca "y":

`yes`

- Wysyłaj potwierdzenie dla każdego pytania zadanego przez `apt-get`:

`yes | sudo apt-get install {{program}}`

- Wielokrotnie wypisuj znak nowej linii, aby zawsze akceptować domyślne opcje poleceń:

`yes ''`
