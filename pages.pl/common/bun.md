# bun

> Środowisko uruchomieniowe JavaScript i zestaw narzędzi.
> Zawiera kompilator, narzędzie do uruchamiania testów i menadżera pakietów.
> Więcej informacji: <https://bun.com/docs>.

- Stwórz nowy projekt Bun w aktualnym katalogu:

`bun init`

- Uruchom plik JavaScript lub skrypt `package.json`:

`bun run {{ścieka/do/pliku|nazwa_skryptu}}`

- Uruchom testy jednostkowe:

`bun test`

- Pobierz i zainstaluj wszystkie pakiety wpisane jako zależności w `package.json`:

`bun {{[i|install]}}`

- Dodaj zależność do `package.json`:

`bun {{[a|add]}} {{nazwa_biblioteki}}`

- Usuń zależność z `package.json`:

`bun {{[rm|remove]}} {{nazwa_biblioteki}}`

- Uruchom REPL (interaktywną powłokę):

`bun repl`

- Zaktualizuj Bun do najnowszej wersji:

`bun upgrade`
