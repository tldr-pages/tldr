# adb logcat

> A rendszerüzenetek naplójának kitöltése. További információ: <https://developer.android.com/studio/command-line/logcat>.

- A rendszer naplóinak megjelenítése:

`adb logcat`

- A reguláris kifejezésnek megfelelő sorok megjelenítése:

`adb logcat -e {{regular_expression}}`

- Naplók megjelenítése egy címkéhez egy adott üzemmódban (\[V\]erbose, \[D\]ebug, \[I\]nfo, \[W\]arning, \[E\]rror, \[F\]atal, \[S\]ilent), más címkék szűrése:

`adb logcat {{tag}}:{{mode}} *:S`

- React Native alkalmazások naplóinak megjelenítése \[V\]erbose módban \[S\]ilencing other tags:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Az összes \[W\]arning és magasabb prioritási szintű címkék naplóinak megjelenítése:

`adb logcat *:W`

- A napló színezése (általában szűrőkkel együtt használjuk):

`adb logcat -v color`
