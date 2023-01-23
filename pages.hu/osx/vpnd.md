# vpnd

> Figyeli a bejövő VPN-kapcsolatokat. Nem szabad manuálisan meghívni. További információ: <https://www.unix.com/man-page/osx/8/vpnd/>.

- Indítsa el a démont:

`vpnd`

- A démon futtatása az előtérben:

`vpnd -x`

- A démon előtérben történő futtatása és a naplók kinyomtatása a terminálra:

`vpnd -d`

- A démon előtérben történő futtatása, naplófájlok nyomtatása a terminálra, és kilépés az argumentumok érvényesítése után:

`vpnd -n`

- Használati összefoglaló nyomtatása és kilépés:

`vpnd -h`

- A démon futtatása egy adott kiszolgálókonfigurációhoz:

`vpnd -i {{server_id}}`
