# radeontop

> Afișează utilizarea GPU-urilor AMD.
> Poate necesita privilegii de root în funcție de sistemul dvs.
> Mai multe informaţii: <https://github.com/clbr/radeontop>

- Arată utilizarea GPU AMD implicit:

`radeontop`

- Activează ieșirea colorată:

`radeontop --color`

- Selectați un GPU specific (numărul magistralei este primul număr din ieșirea `lspci`):

`radeontop --bus {{bus_number}}`

- Specificați rata de reîmprospătare a afișajului (mai mare înseamnă mai multe GPU deasupra capului):

`radeontop --ticks {{samples_per_second}}`
