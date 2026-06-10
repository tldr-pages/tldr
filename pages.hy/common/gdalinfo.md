# gdalinfo

> Թվարկե՛ք տարբեր տեղեկություններ GDAL-ի աջակցվող ռաստերային տվյալների բազայի մասին:.
> Լրացուցիչ տեղեկություններ. <https://gdal.org/en/stable/programs/gdalinfo.html>:.

- Թվարկեք բոլոր աջակցվող ռաստերային ձևաչափերը.:

`gdalinfo --formats`

- Ցուցակեք տեղեկատվությունը որոշակի ռաստերային տվյալների վերաբերյալ.:

`gdalinfo {{path/to/input.tif}}`

- Ցուցակե՛ք JSON ձևաչափով կոնկրետ ռաստերային տվյալների հավաքածուի մասին տեղեկությունները.:

`gdalinfo -json {{path/to/input.tif}}`

- Ցույց տալ որոշակի ռաստերային տվյալների հիստոգրամային արժեքները.:

`gdalinfo -hist {{path/to/input.tif}}`

- Ցուցակե՛ք վեբ քարտեզների ծառայության (WMS) մասին տեղեկությունները.:

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}}`

- Ցուցակե՛ք վեբ քարտեզների ծառայության (WMS) որոշակի տվյալների բազայի մասին տեղեկությունները.:

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}} -sd {{4}}`
