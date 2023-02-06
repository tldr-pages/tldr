# ceph

> Egységes tárolórendszer. További információ: <https://ceph.io>.

- A fürt állapotának ellenőrzése:

`ceph status`

- A fürthasználati statisztikák ellenőrzése:

`ceph df`

- A fürtben lévő elhelyezési csoportok statisztikáinak lekérdezése:

`ceph pg dump --format {{plain}}`

- Tárolási pool létrehozása:

`ceph osd pool create {{pool_name}} {{page_number}}`

- Tárolómedence törlése:

`ceph osd pool delete {{pool_name}}`

- Tárolómedence átnevezése:

`ceph osd pool rename {{current_name}} {{new_name}}`

- Tároló poolok önjavítása:

`ceph pg repair {{pool_name}}`
