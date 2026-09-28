# prctl

> Lees of configureer de resource controls van lopende processen, taken en projecten.
> Meer informatie: <https://www.unix.com/man-page/sunos/1/prctl>.

- Bekijk de proceslimieten en -rechten:

`prctl {{pid}}`

- Bekijk de proceslimieten en -rechten in een machineleesbaar formaat:

`prctl -P {{pid}}`

- Verkrijg een specifieke limiet voor een lopend proces:

`prctl -n process.max-file-descriptor {{pid}}`
