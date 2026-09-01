# doctl vpcs

> Manage DigitalOcean VPC networks.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/vpcs/>.

- List VPC networks:

`doctl vpcs list`

- Create a VPC network with a specific name, region, and IP range:

`doctl vpcs create --name {{vpc_name}} --region {{nyc1}} --ip-range {{10.116.0.0/20}}`

- Retrieve details of a specific VPC network:

`doctl vpcs get {{vpc_id}}`

- Update the name of a specific VPC network:

`doctl vpcs update {{vpc_id}} --name {{new_name}}`

- Delete a VPC network:

`doctl vpcs delete {{vpc_id}}`
