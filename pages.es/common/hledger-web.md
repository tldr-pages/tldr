# hledger-web

> Una interfaz web y una API para `hledger`, una aplicación de contabilidad en texto plano, robusta y fácil de usar.
> Más información: <https://hledger.org/hledger-web.html>.

- Inicia la aplicación web y, si es posible, un navegador de internet, solo para ver y añadir datos de forma local:

`hledger-web`

- Igual que el anterior, pero con un archivo específico y permitiendo la edición de los datos existentes:

`hledger-web {{[-f|--file]}} {{ruta/al/archivo.journal}} --allow edit`

- Inicia solo la aplicación web y acepta conexiones entrantes al host y puerto especificados:

`hledger-web --serve --host {{mi.nombre.de.host}} --port 8000`

- Inicia solo la API JSON de la aplicación web y permite únicamente el acceso de lectura:

`hledger-web --serve-api --host {{mi.nombre.de.host}} --allow view`

- Muestra los importes convertidos al valor de mercado actual en tu moneda base, siempre que se conozca:

`hledger-web --value now --infer-market-prices`

- Muestra el manual en formato Info siempre que sea posible:

`hledger-web --info`

- Muestra la ayuda:

`hledger-web {{[-h|--help]}}`
