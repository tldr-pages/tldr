# dumpsys

> Geef informatie over Android system services.
> Dit commando kan alleen worden gebruikt via `adb shell`.
> Meer informatie: <https://developer.android.com/tools/dumpsys>.

- Krijg diagnostische output voor alle systeemservices:

`dumpsys`

- Krijg diagnostische output voor een specifieke systeemservice:

`dumpsys {{service}}`

- Toon alle services waar `dumpsys` informatie over kan geven:

`dumpsys -l`

- Maak een lijst van servicespecifieke argumenten voor een service:

`dumpsys {{service}} -h`

- Sluit een specifieke service uit van de diagnostische output:

`dumpsys --skip {{service}}`

- Geef een timeout periode in seconden op (standaard 10s):

`dumpsys -t {{8}}`
