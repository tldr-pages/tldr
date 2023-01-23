# reflector

> Arch szkript a tükörlisták lekérdezéséhez és rendezéséhez. További információ: <https://manned.org/reflector>.

- Az összes tükör, a letöltési sebesség alapján történő rendezés és mentés:

`sudo reflector --sort {{rate}} --save {{/etc/pacman.d/mirrorlist}}`

- Csak a német HTTPS tükröket kapja meg:

`reflector --country {{Germany}} --protocol {{https}}`

- Csak a 10 legutóbbi szinkronizált tükröt kapja meg:

`reflector --latest {{10}}`
