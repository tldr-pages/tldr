# pio org

> PlatformIO szervezetek és tulajdonosaik kezelése. További információ: <https://docs.platformio.org/en/latest/core/userguide/org/>.

- Új szervezet létrehozása:

`pio org create {{organization_name}}`

- Szervezet törlése:

`pio org destroy {{organization_name}}`

- Felhasználó hozzáadása egy szervezethez:

`pio org add {{organization_name}} {{username}}`

- Felhasználó eltávolítása egy szervezetből:

`pio org remove {{organization_name}} {{username}}`

- Az összes szervezet felsorolása, amelynek az aktuális felhasználó tagja, valamint azok tulajdonosai:

`pio org list`

- Egy szervezet nevének, e-mail címének vagy megjelenített nevének frissítése:

`pio org update --orgname {{new_organization_name}} --email {{new_email}} --displayname {{new_display_name}} {{organization_name}}`
