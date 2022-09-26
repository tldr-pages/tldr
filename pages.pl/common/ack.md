# ack

> Narzędzie wyszukiwania, takie jak grep, zoptymalizowane dla programistów.
> Zobacz też: `rg`, który jest znacznie szybszy.
> Więcej informacji: <https://beyondgrep.com/documentation>.

- Znajdź pliki zawierające ciąg znaków lub wyrażenie regularne rekurencyjnie w bieżącym katalogu:

`ack "{{wzorzec}}"`

- Szukaj na podstawie wzorca bez uwzględniania wielkości liter:

`ack --ignore-case "{{wzorzec}}"`

- Szukaj linii zawierających wzorzec, wyświetl wyłącznie pasujący tekst bez pozostałej zawartości linii:

`ack -o "{{wzorzec}}"`

- Ogranicz wyszukiwanie do plików wyłącznie określonego typu:

`ack --type={{ruby}} "{{wzorzec}}"`

- Wyszukaj z pominięciem plików określonego typu:

`ack --type=no{{ruby}} "{{wzorzec}}"`

- Policz całkowitą liczbę dopasowań:

`ack --count --no-filename "{{wzorzec}}"`

- Pokaż nazwy plików i liczbę dopasowań w każdym z nich:

`ack --count --files-with-matches "{{wzorzec}}"`

- Wypisz wszystkie możliwe wartości które mogą być użyte dla `--type`:

`ack --help-types`
