# nettop

> A hálózatra vonatkozó frissített információk megjelenítése. További információ: <https://www.manpagez.com/man/1/nettop/>.

- A TCP és UDP aljzatok figyelése minden interfészről:

`nettop`

- TCP aljzatok figyelése a Loopback-interfészekről:

`nettop -m {{tcp}} -t {{loopback}}`

- Egy adott folyamat figyelése:

`nettop -p "{{process_id|process_name}}"`

- Folyamatonkénti összefoglaló megjelenítése:

`nettop -P`

- 10 minta nyomtatása hálózati információkból:

`nettop -l {{10}}`

- 5 másodpercenkénti változások figyelése:

`nettop -d -s {{5}}`

- A nettop futtatása közben az interaktív parancsok listázása:

`h`

- Súgó megjelenítése:

`nettop -h`
