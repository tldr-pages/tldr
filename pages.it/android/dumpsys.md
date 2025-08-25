# dumpsys

> Mostra informazioni sui servizi di sistema Android.
> Questo comando può essere usato solo tramite `adb shell`.
> Maggiori informazioni: <https://developer.android.com/tools/dumpsys>.

- Ottieni l'output diagnostico di tutti i servizi di sistema:

`dumpsys`

- Ottieni l'output diagnostico di un servizio di sistema specifico:

`dumpsys {{servizio}}`

- Elenca tutti i servizi di cui `dumpsys` può fornire informazioni:

`dumpsys -l`

- Elenca gli argomenti specifici per un determinato servizio:

`dumpsys {{servizio}} -h`

- Escludi un servizio specifico dall'output diagnostico:

`dumpsys --skip {{servizio}}`

- Specifica un [t]imeout in secondi (predefinito: 10s):

`dumpsys -t {{8}}`
