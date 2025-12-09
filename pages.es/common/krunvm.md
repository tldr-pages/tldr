# krunvm

> Utilidad basada en CLI para crear micro máquinas virtuales utilizando imágenes OCI.
> Más información: <https://github.com/containers/krunvm>.

- Crea una micro máquina virtual basada en Fedora:

`krunvm create {{docker.io/fedora}} --cpus {{número_de_vcpus}} --mem {{memoria_en_megabytes}} --name "{{nombre}}"`

- Inicia una imagen específica:

`krunvm start "{{nombre}}"`

- Lista las imágenes existentes:

`krunvm list`

- Cambia una imagen específica:

`krunvm changevm --cpus {{número_de_vcpus}} --mem {{memoria_en_megabytes}} --name "{{nuevo_nombre}}" "{{nombre}}"`

- Borra una imagen específica:

`krunvm delete "{{nombre}}"`
