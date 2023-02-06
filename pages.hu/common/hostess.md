# hostess

> Egy idempotens parancssori segédprogram a `/etc/hosts` fájl kezelésére. További információ: <https://github.com/cbednarski/hostess>.

- A tartományok, a cél IP-címek és a be-/kikapcsolt állapot listája:

`hostess list`

- A gépére mutató tartomány hozzáadása a hosts fájlhoz:

`hostess add {{local.example.com}} {{127.0.0.1}}`

- Távolítson el egy tartományt a hosts fájlból:

`hostess del {{local.example.com}}`

- Egy tartomány letiltása (de nem eltávolítása):

`hostess off {{local.example.com}}`
