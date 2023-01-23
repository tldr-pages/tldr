# update-rc.d

> Telepítse és távolítsa el azokat a szolgáltatásokat, amelyek System-V stílusú init script linkek. Az init scriptek a `/etc/init.d/` oldalon találhatók. További információ: <https://manned.org/update-rc.d>.

- Telepítsen egy szolgáltatást:

`update-rc.d {{mysql}} defaults`

- Engedélyezzen egy szolgáltatást:

`update-rc.d {{mysql}} enable`

- Egy szolgáltatás letiltása:

`update-rc.d {{mysql}} disable`

- Egy szolgáltatás erőszakos eltávolítása:

`update-rc.d -f {{mysql}} remove`
