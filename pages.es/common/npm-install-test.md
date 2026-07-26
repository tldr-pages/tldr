# npm install-test

> Equivale a ejecutar `npm install` seguido de `npm test`.
> Nota: `it` puede utilizarse como abreviatura de `install-test`.
> Más información: <https://docs.npmjs.com/cli/npm-install-test/>.

- Instala todas las dependencias y, a continuación, ejecuta las pruebas:

`npm {{[it|install-test]}}`

- Instala un paquete específico y, a continuación, ejecuta las pruebas:

`npm {{[it|install-test]}} {{nombre_del_paquete}}`

- Instala un paquete y lo guarda como dependencia antes de ejecutar las pruebas:

`npm {{[it|install-test]}} {{nombre_del_paquete}} {{[-S|--save]}}`

- Instala las dependencias de forma global y, a continuación, ejecuta las pruebas:

`npm {{[it|install-test]}} {{[-g|--global]}}`
