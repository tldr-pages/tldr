# vgcreate

> Több tömegtároló eszközt egyesítő kötetcsoportok létrehozása. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/vgcreate.8.html>.

- Hozzon létre egy új, vg1 nevű kötetcsoportot a `/dev/sda1` eszközzel:

`vgcreate {{vg1}} {{/dev/sda1}}`

- Új, vg1 nevű kötetcsoport létrehozása több eszköz használatával:

`vgcreate {{vg1}} {{/dev/sda1}} {{/dev/sdb1}} {{/dev/sdc1}}`
