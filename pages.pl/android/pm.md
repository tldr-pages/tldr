# pm

> Pokaż informacje o aplikacjach na urządzeniu z systemem Android.
> Więcej informacji: <https://developer.android.com/tools/adb#pm>.

- Wypisz wszystkie zainstalowane aplikacje:

`pm list packages`

- Wypisz wszystkie zainstalowane aplikacje [s]ystemowe:

`pm list packages -s`

- Wypisz wszystkie zainstalowane aplikacje firm trzecich ([3]):

`pm list packages -3`

- Wypisz aplikacje pasujące do określonych słów kluczowych:

`pm list packages {{słowo_kluczowe1 słowo_kluczowe2 ...}}`

- Pokaż ścieżkę APK konkretnej aplikacji:

`pm path {{aplikacja}}`
