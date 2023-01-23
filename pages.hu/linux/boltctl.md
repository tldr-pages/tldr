# boltctl

> Thunderbolt eszközök vezérlése. További információ: <https://manned.org/boltctl>.

- A csatlakoztatott (és engedélyezett) eszközök listája:

`boltctl`

- Listázza a csatlakoztatott eszközöket, beleértve a nem engedélyezetteket is:

`boltctl list`

- Egy eszköz ideiglenes engedélyezése:

`boltctl authorize {{device_uuid}}`

- Egy eszköz engedélyezése és megjegyzése:

`boltctl enroll {{device_uuid}}`

- Korábban engedélyezett eszköz visszavonása:

`boltctl forget {{device_uuid}}`

- További információk megjelenítése egy eszközről:

`boltctl info {{device_uuid}}`
