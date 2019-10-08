# doctl

> DigitalOcean command line client.
> More information: <https://github.com/digitalocean/doctl/blob/master/README.md>.

- Get the droplet information in the JSON format:

`doctl compute droplet get {{droplet_id}} --output json`

- Get the list of all droplets with their ID, name, and public IPV4 address:

`doctl compute droplet list --format "ID,Name,PublicIPv4"`

- Get the name of the droplet in the format of "name: name":

`doctl compute droplet get {{12345678}} --template "name: {{ .Name}}`

- Create a 64-bit Debian 8 Droplet named test with 1GB of memory, an SSH key, and backups enabled:

`doctl compute droplet create {{test}} --size {{1gb}} --image {{debian-8-x64}} --region {{nyc1}} --ssh-keys {{4d:23:e6:e4:8c:17:d2:cf:89:47:36:b5:c7:33:40:4e}} --enable-backups`
