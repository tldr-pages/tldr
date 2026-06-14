# pg_recvlogical

> Վերահսկել PostgreSQL տրամաբանական ապակոդավորման հոսքերը:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgrecvlogical.html>:.

- Ստեղծեք նոր տրամաբանական կրկնօրինակման բնիկ.:

`pg_recvlogical {{[-d|--dbname]}} {{dbname}} {{[-S|--slot]}} {{slot_name}} --create-slot`

- Սկսեք հոսքային փոփոխությունները տրամաբանական կրկնօրինակման բնիկից ֆայլ.:

`pg_recvlogical {{[-d|--dbname]}} {{dbname}} {{[-S|--slot]}} {{slot_name}} --start {{[-f|--file]}} {{filename}}`

- Բաց թողեք կրկնօրինակման տրամաբանական բնիկը.:

`pg_recvlogical {{[-d|--dbname]}} {{dbname}} {{[-S|--slot]}} {{slot_name}} --drop-slot`

- Ստեղծեք բնիկ՝ միացված երկփուլով.:

`pg_recvlogical {{[-d|--dbname]}} {{dbname}} {{[-S|--slot]}} {{slot_name}} --create-slot {{[-t|--enable-two-phase]}}`

- Ցուցադրել օգնությունը.:

`pg_recvlogical {{[-?|--help]}}`
