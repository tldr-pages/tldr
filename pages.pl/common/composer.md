# composer

> Menadżer pakietów dla projektów PHP.
> Więcej informacji: <https://getcomposer.org/>.

- Interaktywnie utwórz plik `composer.json`:

`composer init`

- Dodaj pakiet do zależności tego projektu, dodając wpis do `composer.json`:

`composer require {{użytkownik/pakiet}}`

- Zainstaluj wszystkie zależności z projektowego `composer.json` i utwórz `composer.lock`:

`composer install`

- Odinstaluj pakiet z tego projektu, usuwając go jako zależność z `composer.json` i `composer.lock`:

`composer remove {{użytkownik/pakiet}}`

- Zaktualizuj wszystkie pakiety z projektowego `composer.json` i zanotuj nową wersję w `composer.lock`:

`composer update`

- Zaktualizuj tylko `composer.lock` po ręcznej aktualizacji `composer.json`:

`composer update --lock`

- Dowiedz się więcej o powodach dlaczego zależność nie może zostać zainstalowana:

`composer why-not {{użytkownik/pakiet}}`

- Zaktualizuj narzędzie composer do najnowszej wersji:

`composer self-update`
