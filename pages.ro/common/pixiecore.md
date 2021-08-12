# pixiecore

> Instrument pentru a gestiona pornirea în rețea a mașinilor.
> Mai multe informaţii: <https://github.com/danderson/netboot/tree/master/pixiecore>

- Porniți un server de boot PXE care oferă o imagine de boot `netboot.xyz`:

`pixiecore {{quick}} xyz --dhcp-no-bind`

- Porniți un nou server de boot PXE care oferă o imagine de boot Ubuntu:

`pixiecore {{quick}} ubuntu --dhcp-no-bind`

- Obțineți o listă cu toate imaginile de boot disponibile pentru modul rapid:

`pixiecore quick --help`
