# toolbox create

> Crea un nuevo contenedor de Toolbx.
> Más información: <https://manned.org/toolbox-create>.

- Crea un contenedor para una distribución específica:

`toolbox create {{[-d|--distro]}} {{distribución}}`

- Crea un contenedor de Toolbx para una liberación específica de la distribución actual:

`toolbox create {{[-r|--release]}} {{liberación}}`

- Crea un contenedor de Toolbx con una imagen personalizada:

`toolbox create {{[-i|--image]}} {{nombre}}`

- Crea un contenedor de Toolbx de una imagen personalizada de Fedora:

`toolbox create {{[-i|--image]}} {{registry.fedoraproject.org/fedora-toolbox:39}}`

- Crea un contenedor Toolbx utilizando la imagen predeterminada de Fedora 39:

`toolbox create {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{39}}`
