# ftp

> Työkalut File Transfer Protokollan käyttämiseen palvelimen kanssa.
> Lisätietoa: <https://manned.org/ftp>.

- Yhdistä FTP-palvelimeen ja käytä interaktiivisesti:

`ftp {{ftp.example.com}}`

- Yhdistä FTP-palvelimeen määrittämällä sen IP-osoite ja portti:

`ftp {{ip_osoite}} {{portti}}`

- [Interaktiotila] Vaihda binäärien lähetystilaan (grafiikat, pakatut tiedostot, jne):

`binary`

- [Interaktiotila] Siirrä useita tiedostoja kysymättä varmistusta jokaiselle tiedostolle:

`prompt off`

- [Interaktiotila] Lataa useita tiedostoja (glob-lauseke):

`mget {{*.png}}`

- [Interaktiotila] Lähetä useita tiedostoja (glob-lauseke):

`mput {{*.zip}}`

- [Interaktiotila] Poista useita tiedostoja etäpalvelimelta:

`mdelete {{*.txt}}`

- [Interaktiotila] Nimeä etäpalvelimella oleva tiedosto uudelleen:

`rename {{alkuperäinen_tiedostonimi}} {{uusi_tiedostonimi}}`
