# reflector

> Arch script pentru a prelua și sorta liste de oglinzi.

- Obțineți toate oglinzile, sortați pentru viteza de descărcare și salvați-le:

`sudo reflector --sort {{rate}} --save {{/etc/pacman.d/mirrorlist}}`

- Obțineți doar oglinzi HTTPS germane:

`reflector --country {{Germany}} --protocol {{https}}`

- Primesc doar cele 10 oglinzi recent sincronizate:

`reflector --latest {{10}}`
