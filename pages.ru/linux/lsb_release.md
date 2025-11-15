# lsb_release

> Выводит информацию, определённую стандартом LSB (Linux Standard Base), а также характерную для дистрибутива.
> Больше информации: <https://manned.org/lsb_release>.

- Отобразить всю имеющуюся информацию:

`lsb_release {{[-a|--all]}}`

- Отобразить описание (обычно полное наименование) операционной системы:

`lsb_release {{[-d|--description]}}`

- Отобразить наименование ОС, без указания поля "Distributor ID":

`lsb_release {{[-is|--id --short]}}`

- Отобразить номер релиза (release number) и кодовое наименование дистрибутива без указания полей с названием:

`lsb_release {{[-rcs|--release --codename --short]}}`
