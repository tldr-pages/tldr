# virt-xml-validate

> A `libvirt` XML-fájlok séma szerinti validálása. Ha nincs megadva séma, a sémát az XML-fájl gyökéreleme határozza meg. További információ: <https://libvirt.org/manpages/virt-xml-validate.html>.

- Egy XML-fájl validálása egy adott séma alapján:

`virt-xml-validate {{path/to/file.xml}} {{schema}}`

- A domain XML validálása a domain séma alapján:

`virt-xml-validate {{path/to/domain.xml}} domain`
