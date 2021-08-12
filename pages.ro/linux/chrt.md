# chrt

> Manipulați atributele în timp real ale unui proces.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man1/chrt.1.html>

- Afişarea atributelor unui proces:

`chrt --pid {{PID}}`

- Afişarea atributelor tuturor firelor unui proces:

`chrt --all-tasks --pid {{PID}}`

- Afișează valorile prioritare min/max care pot fi utilizate cu `chrt`:

`chrt --max`

- Setați politica de programare pentru un proces:

`chrt --pid {{PID}} --{{deadline|idle|batch|rr|fifo|other}}`
