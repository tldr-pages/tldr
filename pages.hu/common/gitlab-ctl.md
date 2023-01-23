# gitlab-ctl

> CLI eszköz a GitLab omnibusz kezelésére. További információ: <https://docs.gitlab.com/omnibus/maintenance/>.

- Minden szolgáltatás állapotának megjelenítése:

`sudo gitlab-ctl status`

- Egy adott szolgáltatás állapotának megjelenítése:

`sudo gitlab-ctl status {{nginx}}`

- Minden szolgáltatás újraindítása:

`sudo gitlab-ctl restart`

- Egy adott szolgáltatás újraindítása:

`sudo gitlab-ctl restart {{nginx}}`

- Minden szolgáltatás naplójának megjelenítése és folyamatos olvasása a `Ctrl + C` megnyomásáig:

`sudo gitlab-ctl tail`

- Egy adott szolgáltatás naplóinak megjelenítése:

`sudo gitlab-ctl tail {{nginx}}`
