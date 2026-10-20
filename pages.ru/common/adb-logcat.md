# adb logcat

> Выводить лог системных сообщений.
> Больше информации: <https://developer.android.com/tools/logcat>.

- Показать системные логи:

`adb logcat`

- Показать строки, соответствующие `reg[e]x`:

`adb logcat -e {{регулярное_выражение}}`

- Показать логи для тега в определённом режиме ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), фильтруя остальные теги:

`adb logcat {{тег}}:{{режим}} *:S`

- Показать логи приложений React Native в подробном ([V]erbose) режиме, подавив ([S]ilent) остальные теги:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Показать логи для всех тегов с уровнем приоритета [W]arning и выше:

`adb logcat *:W`

- Показать логи для конкретного PID:

`adb logcat --pid {{id_процесса}}`

- Показать логи для процесса конкретного пакета:

`adb logcat --pid $(adb shell pidof -s {{пакет}})`

- Раскрасить лог (обычно используется с фильтрами):

`adb logcat -v color`
