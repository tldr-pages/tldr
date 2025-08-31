# ack

> Narzędzie wyszukiwania, podobne do `grep`, zoptymalizowane dla programistów.
> Zobacz także: `rg`, który jest znacznie szybszy.
> Więcej informacji: <https://beyondgrep.com/documentation>.

- Szukaj rekurencyjnie plików zawierających ciąg znaków lub wyrażenie regularne w bieżącym katalogu:

`ack "{{wzorzec_wyszukiwania}}"`

- Szukaj na podstawie wzorca bez uwzględniania wielkości liter:

`ack {{[-i|--ignore-case]}} "{{wzorzec_wyszukiwania}}"`

- Szukaj linii zawierających wzorzec, wyświetlając tylk[o] pasujący tekst bez pozostałej zawartości linii:

`ack {{[-o|--output '$&']}} "{{wzorzec_wyszukiwania}}"`

- Ogranicz wyszukiwanie do plików wyłącznie określonego typu:

`ack {{[-t|--type]}} {{ruby}} "{{wzorzec_wyszukiwania}}"`

- Wyszukaj z pominięciem plików określonego typu:

`ack {{[-t|--type]}} no{{ruby}} "{{wzorzec_wyszukiwania}}"`

- Policz całkowitą liczbę znalezionych dopasowań:

`ack {{[-c|--count]}} {{[-h|--no-filename]}} "{{wzorzec_wyszukiwania}}"`

- Pokaż nazwy plików i liczbę dopasowań w każdym z nich:

`ack {{[-c|--count]}} {{[-l|--files-with-matches]}} "{{wzorzec_wyszukiwania}}"`

- Wypisz wszystkie możliwe wartości które mogą być użyte dla `--type`:

`ack --help-types`
