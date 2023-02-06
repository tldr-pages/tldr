# http_load

> Egy HTTP benchmarking eszköz, amely több HTTP-futást futtat párhuzamosan, hogy tesztelje a webszerver teljesítményét. További információ: <http://www.acme.com/software/http_load/>.

- Egy adott URL-listafájl alapján másodpercenként 20 kérést emulál 60 másodpercen keresztül:

`http_load -rate {{20}} -seconds {{60}} {{path/to/urls.txt}}`

- Emulál 5 egyidejű kérést egy adott URL-listafájl alapján 60 másodpercen keresztül:

`http_load -parallel {{5}} -seconds {{60}} {{path/to/urls.txt}}`

- 1000 kérés emulálása másodpercenként 20 kéréssel, egy adott URL-listafájl alapján:

`http_load -rate {{20}} -fetches {{1000}} {{path/to/urls.txt}}`

- Egy adott URL-listafájl alapján 1000 kérés emulálása 5 egyidejű kéréssel egy időben:

`http_load -parallel {{5}} -fetches {{1000}} {{path/to/urls.txt}}`
