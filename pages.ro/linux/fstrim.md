# fstrim

> Aruncați blocurile neutilizate pe un sistem de fișiere montat.
> Acceptată numai de dispozitive de memorie flash, cum ar fi SSD-urile și cardurile microSD.
> Mai multe informaţii: <https://manned.org/fstrim>

- Trim blocuri neutilizate pe toate partițiile montate pe care le suportă:

`sudo fstrim --all`

- Trim blocuri neutilizate pe o partiție specificată:

`sudo fstrim {{/}}`

- Afișează statistici după tăiere:

`sudo fstrim --verbose {{/}}`
