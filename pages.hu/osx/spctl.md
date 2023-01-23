# spctl

> A biztonsági értékelési házirend alrendszer kezelése. Segédprogram a Gatekeeper kezeléséhez a macOS-ben. További információ: <https://www.unix.com/man-page/osx/8/SPCTL/>.

- A Gatekeeper kikapcsolása:

`spctl --master-disable`

- Adjon hozzá egy szabályt egy alkalmazás futtatásának engedélyezéséhez (a szabály felcímkézése opcionális):

`spctl --add --label {{rule_name}} {{path/to/file}}`

- A Gatekeeper bekapcsolása:

`spctl --master-enable`

- Az összes szabály listázása a rendszerben:

`spctl --list`
