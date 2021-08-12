# f3fix

> Editați tabela de partiții a unei unități flash false.
> A se vedea, de asemenea, `f3probe`, `f3read`.
> Mai multe informaţii: <http://oss.digirati.com.br/f3/>

- Umpleți o unitate flash falsă cu o singură partiție care se potrivește capacității sale reale:

`sudo f3fix {{/dev/device_name}}`

- Marcați partiția ca fiind bootabilă:

`sudo f3fix --boot {{/dev/device_name}}`

- Specificați sistemul de fișiere:

`sudo f3fix --fs-type={{filesystem_type}} {{/dev/device_name}}`
