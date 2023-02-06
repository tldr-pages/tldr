# git credential

> Felhasználói hitelesítő adatok lekérése és tárolása. További információ: <https://git-scm.com/docs/git-credential>.

- A hitelesítő adatok megjelenítése, a felhasználónév és a jelszó lekérdezése a konfigurációs fájlokból:

`echo "{{url=http://example.com}}" | git credential fill`

- A hitelesítő adatok elküldése az összes konfigurált hitelesítő segédprogramnak, hogy későbbi használatra tárolja azokat:

`echo "{{url=http://example.com}}" | git credential approve`

- A megadott hitelesítői adatok törlése az összes konfigurált hitelesítői segédprogramból:

`echo "{{url=http://example.com}}" | git credential reject`
