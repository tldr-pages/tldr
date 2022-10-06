# prctl

> Lees of configureer de Get or set the resource controls of running processes, tasks, and projects.
> Meer informatie: <https://www.unix.com/man-page/sunos/1/prctl>.

- Uitlezen van de process limits en rechten:

`prctl {{PID}}`

- Uitlezen van de process limits en rechten in een geformatteerde layout:

`prctl -P {{PID}}`

- Uitlezen van het max file descripter van een lopend proces:

`prctl -n process.max-file-descriptor {{PID}}`
