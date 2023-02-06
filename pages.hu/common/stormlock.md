# Stormlock

> Központi zárrendszer. További információ: <https://github.com/tmccombs/stormlock>.

- Bérleti jog megszerzése az erőforráshoz:

`stormlock acquire {{resource}}`

- Az adott erőforrás adott bérletének feloldása:

`stormlock release {{resource}} {{lease_id}}`

- Az erőforrás aktuális bérletére vonatkozó információk megjelenítése, ha van ilyen:

`stormlock current {{resource}}`

- Annak tesztelése, hogy az adott erőforráshoz tartozó bérlet jelenleg aktív-e:

`stormlock is-held {{resource}} {{lease_id}}`
