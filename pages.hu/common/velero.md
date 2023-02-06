# velero

> A Kubernetes-alkalmazások és azok állandó kötetei biztonsági mentése és migrálása. További információ: <https://github.com/heptio/velero>.

- Hozzon létre egy biztonsági mentést, amely tartalmazza az összes erőforrást:

`velero backup create {{backup_name}}`

- Az összes biztonsági mentés listázása:

`velero backup get`

- Biztonsági mentés törlése:

`velero backup delete {{backup_name}}`

- Heti mentés készítése, minden egyes mentés 90 napig (2160 óra) él:

`velero schedule create {{schedule_name}} --schedules="{{@every 7d}}" --ttl {{2160h0m0s}}`

- Visszaállítás létrehozása a legutóbbi sikeres biztonsági mentésből, amelyet egy adott ütemezés indít el:

`velero restore create --from-schedule {{schedule_name}}`
