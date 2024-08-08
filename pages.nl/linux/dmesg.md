# dmesg

> Schrijf de kernelberichten naar `stdout`.
> Meer informatie: <https://manned.org/dmesg>.

- Toon kernelberichten:

`dmesg`

- Toon kernel foutmeldingen:

`dmesg --level err`

- Toon kernelberichten en blijf nieuwe lezen, vergelijkbaar met `tail -f` (beschikbaar in kernels 3.5.0 en nieuwer):

`dmesg -w`

- Toon hoeveel fysiek geheugen beschikbaar is op dit systeem:

`dmesg | grep -i memory`

- Toon kernelberichten 1 pagina per keer:

`dmesg | less`

- Toon kernelberichten met een tijdstempel (beschikbaar in kernels 3.5.0 en nieuwer):

`dmesg -T`

- Toon kernelberichten in een leesbare vorm (beschikbaar in kernels 3.5.0 en nieuwer):

`dmesg -H`

- Kleur output (beschikbaar in kernels 3.5.0 en nieuwer):

`dmesg -L`
