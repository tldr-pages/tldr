# radeontop

> Mostra Utilizzo di AMD GPUs.
> Maggiori informazioni: <https://github.com/clbr/radeontop>.

- Mostra utilizzo del AMD GPU principale:

`radeontop`

- Inizia output con colore:

`radeontop --color`

- Scegli un GPU specifico (il numero del bus è il primo numero nell'output di `lspci`):

`radeontop --bus {{bus_numero}}`

- Specifica la frequenza di aggiornamento del display (più alto aggiunge più sovraccarico al GPU):

`radeontop --ticks {{aggiornamenti_per_secondo}}`
