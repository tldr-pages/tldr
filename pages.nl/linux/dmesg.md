# dmesg

> Schrijf de kernelberichten naar `stdout`.
> Zie ook: `journalctl`.
> Meer informatie: <https://manned.org/dmesg>.

- Toon kernelberichten:

`sudo dmesg`

- Toon kernelberichten in een leesbare formaat (gelijk aan `dmesg --color --reltime` piped to a pager):

`sudo dmesg {{[-H|--human]}}`

- Toon kernel foutmeldingen:

`sudo dmesg {{[-l|--level]}} err`

- Toon kernelberichten en blijf nieuwe lezen, vergelijkbaar met `tail -f`:

`sudo dmesg {{[-w|--follow]}}`

- Toon kernelberichten die in het afgelopen uur zijn verzonden:

`sudo dmesg --since "1 hour ago"`

- Toon kernelberichten met tijdstempels als verschillen ten opzichte van de lokale tijd:

`sudo dmesg {{[-e|--reltime]}}`

- Toon kernelberichten met een tijdstempel voor elk bericht:

`sudo dmesg {{[-T|--ctime]}}`

- Kleur output:

`sudo dmesg {{[-L|--color]}}`
