# kscreen-doctor

> A képernyő beállításának módosítása és manipulálása a parancssorból. További információ: <https://invent.kde.org/plasma/libkscreen>.

- A kijelző kimeneti információinak megjelenítése:

`kscreen-doctor --outputs`

- Az 1 azonosítóval rendelkező kijelző kimenet forgatásának beállítása jobbra:

`kscreen-doctor {{output.1.rotation.right}}`

- A `HDMI-2` azonosítóval rendelkező kijelző kimenet méretarányának beállítása 2-re (200%):

`kscreen-doctor {{output.HDMI-2.scale.2}}`
