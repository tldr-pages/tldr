# woeusb

> Windows médiakészítő eszköz. További információ: <https://github.com/WoeUSB/WoeUSB>.

- Formázzon meg egy USB-t, majd hozzon létre egy bootolható Windows telepítő meghajtót:

`woeusb --device {{path/to/windows.iso}} {{/dev/sdX}}`

- Windows-fájlok másolása egy USB-tárolóeszköz meglévő partíciójára, majd bootolhatóvá tétele a jelenlegi adatok törlése nélkül:

`woeusb --partition {{path/to/windows.iso}} {{/dev/sdXN}}`
