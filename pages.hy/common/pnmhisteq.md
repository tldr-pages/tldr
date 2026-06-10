# pnmhisteq

> Հիստոգրամ-հավասարեցրեք PNM պատկերը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmhisteq.html>:.

- Բարձրացրեք PNM պատկերի հակադրությունը՝ օգտագործելով հիստոգրամի հավասարեցում.:

`pnmhisteq {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Փոփոխեք միայն մոխրագույն պիքսելները.:

`pnmhisteq {{[-g|-grey]}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Հիստոգրամի հավասարեցման մեջ մի ներառեք սև կամ սպիտակ պիքսելները.:

`pnmhisteq -no{{black|white}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
