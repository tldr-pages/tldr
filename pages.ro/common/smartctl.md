# smartctl

> Vizualizați datele SMART ale unui disc și alte informații.
> Mai multe informaţii:< https://en.wikipedia.org/wiki/S.M.A.R.T .>

- Vezi Rezumatul de sănătate SMART

`sudo smartctl --health {{/dev/sdX}}`

- Vizualizaţi informaţii despre dispozitiv:

`sudo smartctl --info {{/dev/sdX}}`

- Începeți un scurt autotest:

`sudo smartctl --test short {{/dev/sdX}}`

- Vezi actual/ultima stare de auto-testare și alte capacități SMART:

`sudo smartctl --capabilities {{/dev/sdX}}`

- Vezi SMART auto-test jurnal (dacă este acceptat):

`sudo smartctl --log selftest {{/dev/sdX}}`
