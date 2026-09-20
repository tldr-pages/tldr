# prctl

> Lees of configureer de resource controls van lopende processen, taken en projecten.
> Meer informatie: <https://www.unix.com/man-page/sunos/1/prctl>.

- Uitlezen van de process limits en rechten:

`prctl {{pid}}`

- Uitlezen van de process limits en rechten in een geformatteerde layout:

`prctl -P {{pid}}`

- Uitlezen van het max file descripter van een lopend proces:

`prctl -n process.max-file-descriptor {{pid}}`
