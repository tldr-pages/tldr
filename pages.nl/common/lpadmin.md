# lpadmin

> Configureer CUPS printers en klasses.
> Bekijk ook: `lpoptions`.
> Meer informatie: <https://openprinting.github.io/cups/doc/man-lpadmin.html>.

- Stel de standaard printer in:

`lpadmin -d {{printer}}`

- Verwijder een specifieke printer of klasse:

`lpadmin -x {{printer|klasse}}`

- Voeg een printer toe aan een klasse:

`lpadmin -p {{printer}} -c {{klasse}}`

- Verwijder een printer uit een klasse:

`lpadmin -p {{printer}} -r {{klasse}}`
