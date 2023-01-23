# doctl compute droplet

> Virtuális gépek listázása, létrehozása és törlése, amelyeket dropleteknek neveznek. További információ: <https://docs.digitalocean.com/reference/doctl/reference/compute/droplet/>.

- Droplet létrehozása:

`doctl compute droplet create --region {{region}} --image {{os_image}} --size {{vps_type}} {{droplet_name}}`

- Droplet törlése:

`doctl compute droplet delete {{droplet_id|droplet_name}}`

- Dropletek listázása:

`doctl compute droplet list`
