# ftp

> Hulpmiddelen om via het File Transfer Protocol met een server te communiceren.
> Meer informatie: <https://manned.org/ftp>.

- Verbinden met een FTP-server:

`ftp {{ftp.example.com}}`

- Verbinden met een FTP-server met opgave van IP-adres en poort:

`ftp {{ip_adres}} {{poort}}`

- Omschakelen naar binaire overdrachtsmodus (grafische bestanden, gecomprimeerde bestanden, etc):

`binary`

- Meerdere bestanden overdragen zonder bevestiging voor elk bestand:

`prompt off`

- Meerdere bestanden downloaden (glob-expressie):

`mget {{*.png}}`

- Meerdere bestanden uploaden (glob-expressie):

`mput {{*.zip}}`

- Meerdere bestanden verwijderen op de externe server:

`mdelete {{*.txt}}`

- Een bestand hernoemen op de externe server:

`rename {{originele_bestandsnaam}} {{nieuwe_bestandsnaam}}`
