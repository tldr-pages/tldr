# nova

> Az OpenStack projekt, amely módot biztosít a számítási példányok rendelkezésre bocsátására. További információ: <https://docs.openstack.org/nova/latest/>.

- VM-ek listázása az aktuális bérlőn:

`nova list`

- Az összes bérlő VM-jeinek listázása (csak admin felhasználó):

`nova list --all-tenants`

- VM indítása egy adott állomáson:

`nova boot --nic net-id={{net_id}} --image {{image_id}} --flavor {{flavor}} --availability-zone nova:{{host_name}} {{vm_name}}`

- Kiszolgáló indítása:

`nova start {{server}}`

- Kiszolgáló leállítása:

`nova stop {{server}}`

- Hálózati interfész csatlakoztatása egy adott VM-hez:

`nova interface-attach --net-id {{net_id}} {{server}}`
