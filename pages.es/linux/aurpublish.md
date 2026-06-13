# aurpublish

> Publica paquetes del repositorio de usuarios de Arch.
> Más información: <https://github.com/eli-schwartz/aurpublish/blob/master/doc/aurpublish.1.asciidoc>.

- Verifica la integridad de `PKGBUILD`, genera `.SRCINFO`, crea una plantilla de mensaje de confirmación y publica el paquete en AUR:

`aurpublish {{nombre_del_paquete}}`

- Añade githooks al repositorio actual:

`aurpublish setup`

- Muestra la ayuda:

`aurpublish {{[-h|--help]}}`
