# ionice

> Obțineți sau setați programul I/O clasa de programare și prioritate.
> Cursuri de programare: 1 (în timp real), 2 (cel mai bun efort), 3 (inactiv).
> Niveluri prioritare: 0 (cea mai mare) - 7 (cea mai mică).

- Setați clasa de programare I/O a unui proces de rulare:

`ionice -c {{scheduling_class}} -p {{pid}}`

- Rulați o comandă cu clasa de programare I/O personalizate și prioritate:

`ionice -c {{scheduling_class}} -n {{priority}} {{command}}`

- Imprimați clasa de programare I/O și prioritatea unui proces de execuție:

`ionice -p {{pid}}`
