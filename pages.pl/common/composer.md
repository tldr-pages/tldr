# composer

> Menadżer pakietów dla projektów PHP.
> Więcej informacji: <https://getcomposer.org/>.

- Interaktywnie utwórz plik `composer.json`:

`composer init`

- Dodaj pakiet do zależności tego projektu, dodając wpis do pliku `composer.json`:

`composer require {{uzytkownik/pakiet}}`

- Zainstaluj wszystkie zależności z projektowego `composer.json` i utwórz `composer.lock`:

`composer install`

- Odinstaluj pakiet z tego projektu, usuń go jako zaleśność z plików `composer.json` i `composer.lock`:

`composer remove {{uzytkownik/pakiet}}`

- Zaktualizuj wszystkie pakiety z projektowego `composer.json` i zanotuj nową wersję w pliku `composer.lock`:

`composer update`

- Zaktualizuj tylko plik `composer.lock` po ręcznej aktualizacji `composer.json`:

`composer update --lock`

- Dowiedz się więcej o powodach dlaczego zależność nie może zostać zainstalowana:

`composer why-not {{uzytkownik/pakiet}}`

- Zaktualizuj narzędzie composer do najnowszej wersji:

`composer self-update`
