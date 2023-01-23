# logcat

> A rendszerüzenetek naplójának kitöltése, beleértve a stack traces-t, ha hiba történt, és az alkalmazások által naplózott információs üzeneteket. További információ: <https://developer.android.com/studio/command-line/logcat>.

- Rendszernaplók megjelenítése:

`logcat`

- Rendszernaplók írása egy fájlba:

`logcat -f {{path/to/file}}`

- A reguláris kifejezésnek megfelelő sorok megjelenítése:

`logcat --regex {{regular_expression}}`
