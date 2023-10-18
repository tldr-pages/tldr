# krunvm

> Utilidad basada en CLI para crear micro máquinas virtuales utilizando imagenes OCI.
> Más información: <https://github.com/containers/krunvm>.

- Crea una micro máquina virtual basada en Fedora:

`krunvm create {{docker.io/fedora}} --cpus {{numero_de_vcpus}} --mem {{memoria_en_megabytes}} --name "{{nombre}}"`

- Inicia una imagen especifica:

`krunvm start "{{nombre}}"`

- Lista las imagenes existentes:

`krunvm list`

- Cambia una imagen especifica:

`krunvm changevm --cpus {{numero_de_vcpus}} --mem {{memoria_en_megabytes}} --name "{{nuevo_nombre}}" "{{nombre}}"`

- Borra una imagen especifica:

`krunvm delete "{{nombre}}"`
