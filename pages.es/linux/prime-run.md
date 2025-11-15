# prime-run

> Ejecuta un programa utilizando una tarjeta gráfica Nvidia alternativa.
> Más información: <https://wiki.archlinux.org/title/PRIME#PRIME_render_offload>.

- Ejecuta un programa utilizando una GPU Nvidia dedicada:

`prime-run {{comando}}`

- Valida si se está utilizando la tarjeta Nvidia:

`prime-run glxinfo | grep "OpenGL renderer"`
