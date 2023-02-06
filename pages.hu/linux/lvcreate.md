# lvcreate

> Logikai kötetet hoz létre egy meglévő kötetcsoportban. A kötetcsoport logikai és fizikai kötetek gyűjteménye. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/lvcreate.8.html>.

- Hozzon létre egy 10 gigabájtos logikai kötetet a vg1 kötetcsoportban:

`lvcreate -L {{10G}} {{vg1}}`

- Hozzon létre egy 1500 megabájtos lineáris logikai kötetet mylv néven a vg1 kötetcsoportban:

`lvcreate -L {{1500}} -n {{mylv}} {{vg1}}`

- Hozzon létre egy mylv nevű logikai kötetet, amely a vg1 kötetcsoportban a teljes hely 60%-át használja:

`lvcreate -l {{60%VG}} -n {{mylv}} {{vg1}}`

- Hozzon létre egy mylv nevű logikai kötetet, amely a vg1 kötetcsoportban lévő összes ki nem osztott helyet használja:

`lvcreate -l {{100%FREE}} -n {{mylv}} {{vg1}}`
