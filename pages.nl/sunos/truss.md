# truss

> Troubleshooting tool voor het traceren van system calls.
> SunOS equivalent van strace.
> Meer informatie: <https://www.unix.com/man-page/sunos/1/truss>.

- Start het traceren van een programma door het uit te voeren, en volg alle child processes:

`truss -f {{programma}}`

- Start het traceren van een specifiek proces aan de hand van de PID:

`truss -p {{pid}}`

- Start het traceren van een programma door het uit te voeren, en toon alle argumenten en omgevingsvariabelen:

`truss -a -e {{programma}}`

- Tel tijd, oproepen en fouten voor elke systeem call en geef een overzicht bij de beëindiging van de applicatie:

`truss -c -p {{pid}}`

- Traceer een proces en filter de uitvoer op systeem call:

`truss -p {{pid}} -t {{system_call_naam}}`
