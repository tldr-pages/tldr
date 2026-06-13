# adb logcat

> Estrae un log dei messaggi di sistema.
> Maggiori informazioni: <https://developer.android.com/tools/logcat>.

- Visualizza i log di sistema:

`adb logcat`

- Visualizza le righe che corrispondono a una `reg[e]x`:

`adb logcat -e {{regex}}`

- Visualizza i log per un tag in una modalità specifica ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), filtrando gli altri tag:

`adb logcat {{tag}}:{{mode}} *:S`

- Visualizza i log per applicazioni React Native in modalità [V]erbose [S]ilenzia gli altri tag:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Visualizza i log per tutti i tag con livello di priorità [W]arning e superiore:

`adb logcat *:W`

- Visualizza i log per un PID specifico:

`adb logcat --pid {{pid}}`

- Visualizza i log per il processo di un pacchetto specifico:

`adb logcat --pid $(adb shell pidof -s {{pacchetto}})`

- Colora il log (di solito usato con filtri):

`adb logcat -v color`
