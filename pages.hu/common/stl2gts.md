# stl2gts

> STL fájlok konvertálása a GTS (GNU triangulated surface library) fájlformátumba. További információ: <https://manned.org/stl2gts>.

- STL fájl átalakítása GTS fájlba:

`stl2gts < {{path/to/file.stl}} > {{path/to/file.gts}}`

- STL fájl GTS fájlba konvertálása és az arcnormálisok visszaállítása:

`stl2gts --revert < {{path/to/file.stl}} > {{path/to/file.gts}}`

- Konvertáljon egy STL fájlt GTS-fájlba, és ne egyesítse a csúcsokat:

`stl2gts --nomerge < {{path/to/file.stl}} > {{path/to/file.gts}}`

- STL-fájl konvertálása GTS-fájlba és a felületi statisztikák megjelenítése:

`stl2gts --verbose < {{path/to/file.stl}} > {{path/to/file.gts}}`

- Súgó nyomtatása a `stl2gts`:

`stl2gts --help`
