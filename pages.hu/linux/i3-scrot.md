# i3-scrot

> Wrapper script a `scrot` képernyőfotó segédprogram körül az i3 ablakkezelőhöz. Az alapértelmezett mentési hely a `~/Pictures`, de megváltoztatható a `~/.config/i3-scrot.conf`. További információ: <https://gitlab.manjaro.org/packages/community/i3/i3-scrot>.

- Képernyőkép készítése a teljes képernyőről és mentése az alapértelmezett könyvtárba:

`i3-scrot`

- Képernyőkép készítése az aktív ablakról:

`i3-scrot --window`

- Képernyőkép készítése egy adott téglalap alakú kijelölésről:

`i3-scrot --select`

- Képernyőkép készítése a teljes képernyőről és másolása a vágólapra:

`i3-scrot --desk-to-clipboard`

- Képernyőkép készítése az aktív ablakról és másolása a vágólapra:

`i3-scrot --window-to-clipboard`

- Képernyőkép készítése egy adott kijelölésről és másolása a vágólapra:

`i3-scrot --select-to-clibpoard`

- Képernyőkép készítése az aktív ablakról 5 másodperces késleltetés után:

`i3-scrot --window {{5}}`
