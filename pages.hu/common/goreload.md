# goreload

> Élő újratöltő segédprogram Go programokhoz. További információ: <https://github.com/acoshift/goreload>.

- Állítsuk be a megfigyelendő bináris fájl nevét (alapértelmezés szerint `.goreload`):

`goreload -b {{path/to/binary}} {{path/to/file}}.go`

- Egyéni naplóelőtag beállítása (alapértelmezett: `goreload`):

`goreload --logPrefix {{prefix}} {{path/to/file}}.go`

- Újratöltés, amikor bármely fájl változik:

`goreload --all`
