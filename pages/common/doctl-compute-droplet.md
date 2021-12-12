# doctl compute droplet

> List, create, and delete virtual machines which are called droplets.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/compute/droplet/>.

- Create a droplet:

`doctl compute droplet create --region {{region}} --image {{OS_image}} --size {{vps_type}} {{droplet_name}}`

- Delete a droplet:

`doctl compute droplet delete {{droplet_id}}`

- List Droplets:

`doctl compute droplet list`
