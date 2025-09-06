# eselect locale

> Een `eselect`-module voor het beheren van de `LANG`-omgevingsvariabele, die de systeemtaal instelt.
> Meer informatie: <https://wiki.gentoo.org/wiki/Eselect#Locale>.

- Toon van beschikbare locales:

`eselect locale list`

- Stel de `LANG`-omgevingsvariabele in `/etc/profile.env` in op naam of index van de `list`-opdracht:

`eselect locale set {{naam|index}}`

- Toon de waarde van `LANG` in `/etc/profile.env`:

`eselect locale show`
