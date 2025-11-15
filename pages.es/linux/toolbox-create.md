# toolbox create

> Crea un nuevo contenedor de `toolbox`.
> Más información: <https://manned.org/toolbox-create.1>.

- Crea un contenedor para una distribución específica:

`toolbox create --distro {{distribución}}`

- Crea un contenedor de `toolbox` para una liberación específica de la distribución actual:

`toolbox create --release {{liberación}}`

- Crea un contenedor de `toolbox` con una imagen personalizada:

`toolbox create --image {{nombre}}`

- Crea un contenedor de `toolbox` de una imagen personalizada de Fedora:

`toolbox create --image {{registry.fedoraproject.org/fedora-toolbox:39}}`

- Crea un contenedor `toolbox` utilizando la imagen predeterminada de Fedora 39:

`toolbox create --distro {{fedora}} --release {{f39}}`
