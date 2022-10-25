# say

> Czyta na głos.
> Więcej informacji: <https://ss64.com/osx/say.html>.

- Powiedz na głos:

`say "{{Lubię jeździć na rowerze.}}"`

- Przeczytaj z pliku:

`say --input-file={{plik.txt}}`

- Przeczytaj używając konkretnego głosu i prędkości mowy:

`say --voice={{głos}} --rate={{słowa_na_minutę}} "{{Przepraszam Dave, ale nie mogę Ci na to pozwolić.}}"`

- Pokaż listę dostępnych głosów:

`say --voice="?"`

- Powiedz coś Angielskim głosem:

`say --voice=Alex "{{Here's to the Crazy Ones.}}"`

- Stwórz plik audio z tekstu:

`say --output-file={{plik.aiff}} "{{Litwo, ojczyzno moja!}}"`
