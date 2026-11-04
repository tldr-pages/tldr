# prctl

> Lees of configureer de resource controls van lopende processen, taken en projecten.
> Meer informatie: <https://www.unix.com/man-page/sunos/1/prctl>.

- Bekijk de proceslimieten en -rechten:

`prctl {{proces_id}}`

- Bekijk de proceslimieten en -rechten in een machineleesbaar formaat:

`prctl -P {{proces_id}}`

- Verkrijg een specifieke limiet voor een lopend proces:

`prctl -n process.max-file-descriptor {{proces_id}}`
