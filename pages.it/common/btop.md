# btop

> Monitor di risorse che mostra informazioni su CPU, memoria, dischi, rete e processi.
> Versione in C++ di `bpytop`.
> Vedi anche: `btm`, `glances`, `atop`, `htop`, `top`.
> Maggiori informazioni: <https://github.com/aristocratos/btop#command-line-options>.

- Avvia `btop`:

`btop`

- Avvia `btop` con il preset di impostazioni specificato:

`btop {{[-p|--preset]}} {{0..9}}`

- Avvia `btop` in modalità TTY usando 16 colori e simboli dei grafici compatibili con TTY:

`btop {{[-t|--tty]}}`

- Avvia `btop` in modalità 256 colori invece che in modalità colore a 24 bit:

`btop {{[-l|--low-color]}}`

- Imposta la frequenza di aggiornamento a 500 millisecondi:

`btop {{[-u|--update]}} 500`

- Esci da `btop`:

`<q>`

- Mostra l’aiuto:

`btop {{[-h|--help]}}`
