# ddrescue

> Instrument de recuperare a datelor care citește datele de pe dispozitivele bloc deteriorate.
> Mai multe informaţii: <https://www.gnu.org/software/ddrescue/>

- Luați o imagine a unui dispozitiv, creând un fișier jurnal:

`sudo ddrescue {{/dev/sdb}} {{path/to/image.dd}} {{path/to/log.txt}}`

- Clone Disk A la Disk B, creând un fișier jurnal:

`sudo ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}} {{path/to/log.txt}}`
