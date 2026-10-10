# cat

> Onyesha na unganisha faili.
> Maelezo zaidi: <https://manned.org/cat.1posix>.

- Onyesha maudhui ya faili kwenye `stdout`:

`cat {{njia/ya/faili}}`

- Unganisha faili kadhaa kuwa faili moja la matokeo:

`cat {{njia/ya/faili1 njia/ya/faili2 ...}} > {{njia/ya/faili_la_matokeo}}`

- Ongeza faili kadhaa mwishoni mwa faili la matokeo:

`cat {{njia/ya/faili1 njia/ya/faili2 ...}} >> {{njia/ya/faili_la_matokeo}}`

- Nakili maudhui ya faili kwenye faili la matokeo bila buffering:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Andika `stdin` kwenye faili:

`cat - > {{njia/ya/faili}}`
