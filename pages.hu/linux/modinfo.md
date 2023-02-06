# modinfo

> Egy Linux kernelmodulról szóló információk kinyerése. További információ: <https://manned.org/modinfo>.

- Egy kernelmodul összes attribútumának listázása:

`modinfo {{kernel_module}}`

- Csak a megadott attribútum listázása:

`modinfo -F {{author|description|license|parm|filename}} {{kernel_module}}`
