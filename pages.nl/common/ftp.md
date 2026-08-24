# ftp

> Hulpmiddelen om via het File Transfer Protocol met een server te communiceren.
> Meer informatie: <https://manned.org/ftp>.

- Verbinden met een FTP-server en start in interactieve modus:

`ftp {{ftp.example.com}}`

- Verbinden met een FTP-server met opgave van IP-adres en poort:

`ftp {{ip_adres}} {{poort}}`

- [Interactief] Omschakelen naar binaire overdrachtsmodus (grafische bestanden, gecomprimeerde bestanden, etc):

`binary`

- [Interactief] Meerdere bestanden overdragen zonder bevestiging voor elk bestand:

`prompt off`

- [Interactief] Meerdere bestanden downloaden (glob-expressie):

`mget {{*.png}}`

- [Interactief] Meerdere bestanden uploaden (glob-expressie):

`mput {{*.zip}}`

- [Interactief] Meerdere bestanden verwijderen op de externe server:

`mdelete {{*.txt}}`

- [Interactief] Een bestand hernoemen op de externe server:

`rename {{originele_bestandsnaam}} {{nieuwe_bestandsnaam}}`
