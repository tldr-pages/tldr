# jdupes

> Nagy teljesítményű duplikátumkereső és az fdupes továbbfejlesztett elágazása. További információ: <https://github.com/jbruchon/jdupes>.

- Egyetlen könyvtár keresése:

`jdupes {{path/to/directory}}`

- Keresés több könyvtárban:

`jdupes {{directory1}} {{directory2}}`

- Minden könyvtárban rekurzívan kereshet:

`jdupes --recurse {{path/to/directory}}`

- Rekurzív könyvtárkeresés, és a felhasználó kiválaszthatja a megőrzendő fájlokat:

`jdupes --delete --recurse {{path/to/directory}}`

- Több könyvtár keresése és az alkönyvtárak követése a directory2 alatt, nem a directory1 alatt:

`jdupes {{directory1}} --recurse: {{directory2}}`

- Keresés több könyvtárban és a könyvtárak sorrendjének megtartása az eredményben:

`jdupes -O {{directory1}} {{directory2}} {{directory3}}`
