# pm

> Pokaż informacje o aplikacjach na urządzeniu z systemem Android.
> Więcej informacji: <https://developer.android.com/studio/command-line/adb#pm>.

- Listuj wszystkie zainstalowane aplikacje:

`pm list packages`

- Listuj wszystkie zainstalowane aplikacje systemowych:

`pm list packages -s`

- Listuj wszystkie zainstalowane aplikacje firm trzecich:

`pm list packages -3`

- Listuj aplikacje pasujące do określonych słów kluczowych:

`pm list packages {{słowo_kluczowe}}`

- Pokaż ścieżkę APK konkretnej aplikacji:

`pm path {{aplikacja}}`
