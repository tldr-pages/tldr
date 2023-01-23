# magento

> CLI a Magento PHP keretrendszer kezeléséhez. További információ: <https://magento.com>.

- Engedélyezzen egy vagy több, szóközzel elválasztott modult:

`magento module:enable {{module(s)}}`

- Egy vagy több szóközzel elválasztott modul letiltása:

`magento module:disable {{module(s)}}`

- A modulok engedélyezése után frissítse az adatbázist:

`magento setup:upgrade`

- A kód és a függőségi injektálás konfigurációjának frissítése:

`magento setup:di:compile`

- Statikus eszközök telepítése:

`magento setup:static-content:deploy`

- Karbantartási mód engedélyezése:

`magento maintenance:enable`

- Karbantartási mód letiltása:

`magento maintenance:disable`

- Az összes elérhető parancs listázása:

`magento list`
