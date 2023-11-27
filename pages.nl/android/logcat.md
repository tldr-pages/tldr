# logcat

> Dump een logboek van systeemberichten, inclusief stacktraces wanneer er een fout is opgetreden, en informatieberichten die door applicaties zijn vastgelegd.
> Meer informatie: <https://developer.android.com/studio/command-line/logcat>.

- Toon systeemlogs:

`logcat`

- Schrijf systeemlogs naar een bestand:

`logcat -f {{pad/naar/bestand}}`

- Toon lijnen die overeenkomen met een reguliere expressie:

`logcat --regex {{reguliere_expressie}}`

- Toon logs voor een specifieke PID:

`logcat --pid={{pid}}`

- Toon logs voor een proces van een specifiek pakket:

`logcat --pid=$(pidof -s {{pakket}})`
