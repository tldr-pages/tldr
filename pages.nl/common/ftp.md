# ftp

> Hulpmiddelen om via het File Transfer Protocol met een server te communiceren.
> Meer informatie: <https://manned.org/ftp>.

- Verbind met een FTP-server en start in interactieve modus:

`ftp {{ftp.example.com}}`

- Verbind met een FTP-server met opgave van IP-adres en poort:

`ftp {{ip_adres}} {{poort}}`

- [Interactief] Schakel om naar binaire overdrachtsmodus (grafische bestanden, gecomprimeerde bestanden, etc):

`binary`

- [Interactief] Draag meerdere bestanden over zonder bevestiging voor elk bestand:

`prompt off`

- [Interactief] Download meerdere bestanden (`glob`-expressie):

`mget {{*.png}}`

- [Interactief] Upload meerdere bestanden (`glob`-expressie):

`mput {{*.zip}}`

- [Interactief] Verwijder meerdere bestanden op de externe server:

`mdelete {{*.txt}}`

- [Interactief] Hernoem een bestand op de externe server:

`rename {{originele_bestandsnaam}} {{nieuwe_bestandsnaam}}`
