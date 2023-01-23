# ddrescue

> Adatmentő eszköz, amely adatokat olvas ki sérült blokkeszközökről. További információ: <https://www.gnu.org/software/ddrescue/>.

- Készítsen képet egy eszközről, naplófájlt létrehozva:

`sudo ddrescue {{/dev/sdb}} {{path/to/image.dd}} {{path/to/log.txt}}`

- Klónozza az A lemezt a B lemezre, naplófájlt létrehozva:

`sudo ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}} {{path/to/log.txt}}`
