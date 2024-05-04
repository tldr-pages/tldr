# logcat

> Zrzut dziennika komunikatów systemowych, w tym śladów stosu po wystąpieniu błędu i komunikatów informacyjnych rejestrowanych przez aplikacje.
> Więcej informacji: <https://developer.android.com/tools/logcat>.

- Wyświetl logi systemowe:

`logcat`

- Zapisz logi systemowe do pliku:

`logcat -f {{ścieżka/do/pliku}}`

- Wyświetl linie pasujące do wyrażenia regularnego:

`logcat --regex {{wyrażenie_regularne}}`

- Wyświetl logi dla określonego PID:

`logcat --pid {{pid}}`

- Wyświetl logi dla procesu określonego pakietu:

`logcat --pid $(pidof -s {{pakiet}})`
