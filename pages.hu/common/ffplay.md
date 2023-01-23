# ffplay

> Egy egyszerű és hordozható médialejátszó, amely az FFmpeg könyvtárakat és az SDL könyvtárat használja. További információ: <https://ffmpeg.org/ffplay-all.html>.

- Médiafájl lejátszása:

`ffplay {{path/to/file}}`

- Videó lejátszása és mozgásvektorok megjelenítése valós időben:

`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb {{path/to/file}}`

- Csak a videó kulcskockáinak megjelenítése:

`ffplay -vf select="{{eq(pict_type\,PICT_TYPE_I)}}" {{path/to/file}}`
