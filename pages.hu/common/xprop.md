# xprop

> Az X-kiszolgáló ablak- és betűtípus-tulajdonságainak megjelenítésére szolgáló eszköz. További információ: <https://manned.org/xprop>.

- A gyökérablak nevének megjelenítése:

`xprop -root WM_NAME`

- Megjeleníti egy ablak ablakkezelő tippjeit:

`xprop -name "{{window_name}}" WM_HINTS`

- A betűtípus pontméretének megjelenítése:

`xprop -font "{{font_name}}" POINT_SIZE`

- A 0x200007 azonosítójú ablak összes tulajdonságának megjelenítése:

`xprop -id {{0x200007}}`
