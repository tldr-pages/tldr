# valet

> Un entorno de desarrollo Laravel que permite alojar sitios a través de túneles locales en `http://<ejemplo>.test`.
> Más información: <https://laravel.com/docs/valet>.

- Inicia el daemon valet:

`valet start`

- Registra el directorio de trabajo actual como ruta en la que Valet debe buscar sitios:

`valet park`

- Muestra las rutas 'aparcadas':

`valet paths`

- Sirve un único sitio en lugar de un directorio completo:

`valet link {{nombre_aplicacion}}`

- Comparte un proyecto a través de un túnel Ngrok:

`valet share`
