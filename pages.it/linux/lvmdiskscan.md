# lvmdiskscan

> Cerca dispositivi che possono essere usati come volumi fisici da LVM (deprecato; preferisci `pvs`).
> Maggiori informazioni: <https://manned.org/lvmdiskscan>.

- Scansiona tutti i dispositivi:

`lvmdiskscan`

- Mostra solo i volumi fisici (PV):

`lvmdiskscan {{[-l|--lvmpartition]}}`

- Aumenta la verbosità (ripeti per maggiori dettagli):

`lvmdiskscan {{[-v|--verbose]}}`
