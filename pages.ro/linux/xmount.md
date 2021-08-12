# xmount

> Conversie din mers între mai multe tipuri de imagini de pe hard disk de intrare și ieșire cu suport opțional pentru memoria cache de scriere.
> Creează un sistem de fișiere virtual utilizând FUSE (Sistem de fișiere în spațiul de utilizator) care conține o reprezentare virtuală a imaginii de intrare.
> Mai multe informaţii: <https://manned.org/xmount>

- Montați un fișier imagine `.raw` într-un fișier container DMG:

`xmount --in {{raw}} {{path/to/image.dd}} --out {{dmg}} {{mountpoint}}`

- Montați un fișier imagine EWF cu suport de scriere cache într-un fișier VHD pentru a porni de la:

`xmount --cache {{path/to/cache.ovl}} --in {{ewf}} {{path/to/image.E??}} --out {{vhd}} {{mountpoint}}`

- Montați prima partiție din sectorul 2048 într-un nou fișier imagine `.raw`:

`xmount --offset {{2048}} --in {{raw}} {{path/to/image.dd}} --out {{raw}} {{mountpoint}}`
