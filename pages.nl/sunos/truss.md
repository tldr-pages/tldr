# truss

> Troubleshooting tool voor het traceren van system calls.
> SunOS equivalent van strace.
> Meer informatie: <https://www.unix.com/man-page/linux/1/truss>.

- Start het traceren van een programma door het uit te voeren, en de tracering van alle child processes:

`truss -f {{program}}`

- Start het traceren van een specifiek proces aan de hand van het PID:

`truss -p {{pid}}`

- Start het traceren van een programma door het uit te voeren, en toont alle argumenent en omgevingsinstellingen:

`truss -a -e {{program}}`

- Telt tijd, oproepen, en fouten voor elke systeem call en geeft een oplijsting bij de beindiging van de applicatie:

`truss -c -p {{pid}}`

- Traceert een process filter output via system call:

`truss -p {{pid}} -t {{system_call_name}}`
