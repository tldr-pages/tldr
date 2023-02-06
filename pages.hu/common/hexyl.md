# hexyl

> Egy egyszerű hexa-kijelző a terminálhoz. Színes kimenetet használ a különböző bájtkategóriák megkülönböztetésére. További információ: <https://github.com/sharkdp/hexyl>.

- Kiírja egy fájl hexadecimális ábrázolását:

`hexyl {{path/to/file}}`

- Egy fájl első n bájtjának hexadecimális ábrázolását nyomtatja ki:

`hexyl -n {{n}} {{path/to/file}}`

- Egy fájl 512-től 1024-ig terjedő bájtjainak nyomtatása:

`hexyl -r {{512}}:{{1024}} {{path/to/file}}`

- 512 bájt kinyomtatása az 1024. bájttól kezdve:

`hexyl -r {{1024}}:+{{512}} {{path/to/file}}`
