# say

> Czyta na głos.
> Więcej informacji: <https://keith.github.io/xcode-man-pages/say.1.html>.

- Powiedz na głos:

`say "{{Lubię jeździć na rowerze.}}"`

- Przeczytaj z pliku:

`say --input-file={{ścieżka/do/pliku.txt}}`

- Przeczytaj używając konkretnego głosu i prędkości mowy:

`say --voice={{głos}} --rate={{słowa_na_minutę}} "{{Przepraszam Dave, ale nie mogę Ci na to pozwolić.}}"`

- Pokaż listę dostępnych głosów, różne głosy obsługują różne języki:

`say --voice="?"`

- Powiedz coś po angielsku:

`say --voice={{Alex}} "{{Here's to the Crazy Ones.}}"`

- Stwórz plik audio z tekstu:

`say --output-file={{ścieżka/do/pliku.aiff}} "{{Litwo, ojczyzno moja!}}"`
