# pixiecore

> Eszköz a gépek hálózati indításának kezelésére. További információ: <https://github.com/danderson/netboot/tree/master/pixiecore>.

- Indítson el egy PXE boot szervert, amely a `netboot.xyz` boot image-et biztosítja:

`pixiecore {{quick}} xyz --dhcp-no-bind`

- Új PXE boot szerver indítása, amely Ubuntu boot image-et biztosít:

`pixiecore {{quick}} ubuntu --dhcp-no-bind`

- A gyors üzemmódhoz rendelkezésre álló összes boot image listájának lekérdezése:

`pixiecore quick --help`
