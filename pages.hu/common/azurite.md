# azurite

> Azure Storage API kompatibilis kiszolgáló (emulátor) helyi környezetben. További információ: <https://www.npmjs.com/package/azurite>.

- Egy meglévő \[l\]ocation használata munkaterület elérési útvonalként:

`azurite {{-l|--location}} {{path/to/directory}}`

- A konzolon megjelenített hozzáférési napló letiltása:

`azurite {{-s|--silent}}`

- Engedélyezze a \[d\]ebug naplózást egy fájl elérési útvonalának megadásával naplózási célként:

`azurite {{-d|--debug}} {{path/to/debug.log}}`

- A Blob/Queue/Table szolgáltatás figyelési címének testreszabása:

`azurite {{--blobHost|--queueHost|--tableHost}} {{0.0.0.0}}`

- A Blob/Queue/Table szolgáltatás figyelőportjának testreszabása:

`azurite {{--blobPort|--queuePort|--tablePort}} {{8888}}`
