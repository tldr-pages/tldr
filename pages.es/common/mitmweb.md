# mitmweb

> Un proxy HTTP interactivo de tipo "man-in-the-middle" basado en web.
> Vea también: `mitmproxy`.
> Más información: <https://docs.mitmproxy.org/stable/concepts-options/>.

- Inicia `mitmweb` con la configuración predeterminada:

`mitmweb`

- Inicia `mitmweb` vinculado a una dirección y un puerto personalizados:

`mitmweb --listen-host {{ip_direccion}} --listen-port {{puerto}}`

- Inicia `mitmweb` utilizando un script para procesar el tráfico:

`mitmweb --scripts {{ruta/a/script.py}}`
