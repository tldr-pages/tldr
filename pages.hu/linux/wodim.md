# wodim

> Parancs (egyes rendszereken `cdrecord` néven) adatok CD-re vagy DVD-re történő rögzítésére. A wodim egyes meghívásai romboló műveleteket okozhatnak, például a lemezen lévő összes adat törlését. További információ: <https://manned.org/wodim>.

- A `wodim` elérhető optikai meghajtók megjelenítése:

`wodim --devices`

- Csak hangot tartalmazó lemez rögzítése ("égetése"):

`wodim dev=/dev/{{optical_drive}} -audio {{track*.cdaudio}}`

- Egy fájl lemezre égetése, a lemez kiadása, ha elkészült (egyes írók ezt igénylik):

`wodim -eject dev=/dev/{{optical_drive}} -data {{file.iso}}`

- Fájlt írni a lemezre egy optikai meghajtóban, esetleg egymás után több lemezre írva:

`wodim -tao dev=/dev/{{optical_drive}} -data {{file.iso}}`
