# nu

> A Nushell ("egy új típusú shell") modern, strukturált módon közelíti meg a parancssort. Lásd még: `elvish`. További információ: <https://www.nushell.sh>.

- Indítson el egy interaktív shell munkamenetet:

`nu`

- Konkrét parancsok végrehajtása:

`nu --commands "{{echo 'nu is executed'}}"`

- Egy adott szkript végrehajtása:

`nu {{path/to/script.nu}}`

- Egy adott szkript végrehajtása naplózással:

`nu --loglevel {{error|warn|info|debug|trace}} {{path/to/script.nu}}`
