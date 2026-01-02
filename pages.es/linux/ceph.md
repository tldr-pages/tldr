# ceph

> Un sistema de almacenamiento unificado.
> Más información: <https://docs.ceph.com/en/latest/man/8/ceph/>.

- Comprueba el estado del cluster:

`ceph status`

- Comprueba las estadísticas de uso del cluster:

`ceph df`

- Obtiene las estadísticas de los grupos de colocación de un cluster:

`ceph pg dump --format {{plain}}`

- Crea un grupo de almacenamiento:

`ceph osd pool create {{nombre_pool}} {{número_de_página}}`

- Elimina un pool de almacenamiento:

`ceph osd pool delete {{nombre_pool}}`

- Cambia el nombre de un pool de almacenamiento:

`ceph osd pool rename {{nombre_actual}} {{nombre_nuevo}}`

- Auto-repara pool de almacenamiento:

`ceph pg repair {{nombre_pool}}`
