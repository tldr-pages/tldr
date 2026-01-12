# adb reverse

> Inverte le connessioni socket da un dispositivo Android o emulatore collegato.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Elenca tutte le connessioni socket inverse da emulatori e dispositivi:

`adb reverse --list`

- Inverte una porta TCP dall'unico emulatore o dispositivo collegato verso localhost:

`adb reverse tcp:{{porta_remota}} tcp:{{porta_locale}}`

- Inverte una porta TCP da un emulatore o dispositivo specifico (per ID dispositivo / numero [s]eriale) verso localhost:

`adb -s {{device_ID}} reverse tcp:{{porta_remota}} tcp:{{porta_locale}}`

- Rimuove una connessione socket inversa da un emulatore o dispositivo:

`adb reverse --remove tcp:{{porta_remota}}`

- Rimuove tutte le connessioni socket inverse da tutti gli emulatori e dispositivi:

`adb reverse --remove-all`
