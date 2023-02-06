# f3fix

> Egy hamis pendrive partíciós táblájának szerkesztése. Lásd még: `f3probe`, `f3write`, `f3read`. További információ: <http://oss.digirati.com.br/f3/>.

- Töltse fel a hamis flash meghajtót egyetlen partícióval, amely megfelel a valódi kapacitásának:

`sudo f3fix {{/dev/device_name}}`

- Jelölje meg a partíciót bootolhatónak:

`sudo f3fix --boot {{/dev/device_name}}`

- Adja meg a fájlrendszert:

`sudo f3fix --fs-type={{filesystem_type}} {{/dev/device_name}}`
