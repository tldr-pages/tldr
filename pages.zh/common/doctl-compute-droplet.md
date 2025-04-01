# doctl compute droplet

> 列出、创建和删除称为 droplet 的虚拟机。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/compute/droplet/>.

- 创建一个 droplet：

`doctl compute droplet create --region {{region}} --image {{os_image}} --size {{vps_type}} {{droplet_name}}`

- 删除一个 droplet：

`doctl compute droplet delete {{droplet_id|droplet_name}}`

- 列出所有 droplet：

`doctl compute droplet list`