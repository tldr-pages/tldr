# adb logcat

> Extrai um registro (log) de mensagens do sistema.
> Mais informações: <https://developer.android.com/tools/logcat>.

- Exibe registros (logs) do sistema:

`adb logcat`

- Exibe linhas que correspondem a uma `reg[e]x`:

`adb logcat -e {{regex}}`

- Exibe registros de uma tag em um modo específico ([V]erbose (detalhado), [D]ebug (depuração), [I]nfo (informação), [W]arning (aviso), [E]rror (erro), [F]atal (fatal), [S]ilent (silencioso)), filtrando outras tags:

`adb logcat {{tag}}:{{mode}} *:S`

- Exibe registros de aplicações React Native em modo [V]erbose, silenciando outras tags:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Exibe registros de todas as tags com nível de prioridade [W]arning (aviso) ou superior:

`adb logcat *:W`

- Exibe registros de um PID específico:

`adb logcat --pid {{pid}}`

- Exibe registros do processo de um pacote específico:

`adb logcat --pid $(adb shell pidof -s {{package}})`

- Colore o registro (geralmente usado com filtros):

`adb logcat -v color`
