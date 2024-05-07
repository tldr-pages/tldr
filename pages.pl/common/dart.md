# dart

> Zarządzaj projektami Dart.
> Więcej informacji: <https://dart.dev/tools/dart-tool>.

- Zainicjuj nowy projekt Dart w katalogu o tej samej nazwie:

`dart create {{nazwa_projektu}}`

- Uruchom plik Dart:

`dart run {{ścieżka/do/pliku.dart}}`

- Pobierz zależności dla obecnego projektu:

`dart pub get`

- Uruchom testy jednostkowe dla obecnego projektu:

`dart test`

- Aktualizuj przestarzałe zależności projektu w celu obsługi null-safety:

`dart pub upgrade --null-safety`

- Skompiluj plik Dart do natywnego pliku binarnego:

`dart compile exe {{ścieżka/do/pliku.dart}}`

- Zastosuj automatyczne poprawki dla obecnego projektu:

`dart fix --apply`
