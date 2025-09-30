# dmesg

> Schrijf de kernelberichten naar `stdout`.
> Meer informatie: <https://manned.org/dmesg>.

- Toon kernelberichten:

`sudo dmesg`

- Toon kernel foutmeldingen:

`sudo dmesg {{[-l|--level]}} err`

- Toon kernelberichten en blijf nieuwe lezen, vergelijkbaar met `tail -f` (beschikbaar in kernels 3.5.0 en nieuwer):

`sudo dmesg {{[-w|--follow]}}`

- Toon hoeveel fysiek geheugen beschikbaar is op dit systeem:

`sudo dmesg | grep {{[-i|--ignore-case]}} memory`

- Toon kernelberichten 1 pagina per keer:

`sudo dmesg | less`

- Toon kernelberichten met een tijdstempel (beschikbaar in kernels 3.5.0 en nieuwer):

`sudo dmesg {{[-T|--ctime]}}`

- Toon kernelberichten in een leesbare vorm (beschikbaar in kernels 3.5.0 en nieuwer):

`sudo dmesg {{[-H|--human]}}`

- Kleur output (beschikbaar in kernels 3.5.0 en nieuwer):

`sudo dmesg {{[-L|--color]}}`
