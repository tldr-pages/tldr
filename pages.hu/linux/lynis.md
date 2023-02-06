# lynis

> Rendszer- és biztonsági ellenőrzési eszköz. További információ: <https://cisofy.com/documentation/lynis/>.

- Ellenőrizze, hogy a Lynis naprakész-e:

`sudo lynis update info`

- Futtasson biztonsági ellenőrzést a rendszeren:

`sudo lynis audit system`

- Egy Dockerfile biztonsági ellenőrzésének futtatása:

`sudo lynis audit dockerfile {{path/to/dockerfile}}`
