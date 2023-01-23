# pio access

> A közzétett erőforrások (csomagok) hozzáférési szintjének beállítása a nyilvántartásban. További információ: <https://docs.platformio.org/en/latest/core/userguide/access/>.

- Egy felhasználónak hozzáférést biztosít egy erőforráshoz:

`pio access grant {{guest|maintainer|admin}} {{username}} {{resource_urn}}`

- Megszünteti egy felhasználó hozzáférését egy erőforráshoz:

`pio access revoke {{username}} {{resource_urn}}`

- Megjeleníti az összes erőforrást, amelyhez egy felhasználó vagy csapat hozzáféréssel rendelkezik, valamint a hozzáférési szintet:

`pio access list {{username}}`

- Az erőforráshoz való hozzáférés korlátozása bizonyos felhasználókra vagy csapattagokra:

`pio access private {{resource_urn}}`

- Minden felhasználó számára engedélyezni az erőforráshoz való hozzáférést:

`pio access public {{resource_urn}}`
