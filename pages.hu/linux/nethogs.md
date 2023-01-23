# nethogs

> A sávszélesség-használat folyamatonkénti nyomon követése. További információ: <https://github.com/raboof/nethogs>.

- Indítsa el a nethogs-t root-ként (alapértelmezett eszköz az eth0):

`sudo nethogs`

- A sávszélesség figyelése egy adott eszközön:

`sudo nethogs {{device}}`

- Sávszélesség figyelése több eszközön:

`sudo nethogs {{device1}} {{device2}}`

- Frissítési sebesség megadása:

`sudo nethogs -t {{seconds}}`
