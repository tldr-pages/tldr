# f3probe

> Sondează un dispozitiv bloc (de exemplu, o unitate flash sau un card microSD) pentru memorie flash contrafăcută.
> A se vedea, de asemenea, `f3read`, `f3write`, `f3fix”.
> Mai multe informaţii: <https://github.com/AltraMayor/f3>

- Sonda un dispozitiv bloc:

`sudo f3probe {{path/to/block_device}}`

- Utilizați minim despre RAM posibil:

`sudo f3probe --min-memory {{path/to/block_device}}`

- Operaţii de disc de timp:

`sudo f3probe --time-ops {{path/to/block_device}}`
