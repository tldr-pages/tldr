# vagrant global-status

> Display the state of all active Vagrant environments for the current user.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/global-status>.

- List all known Vagrant environments:

`vagrant global-status`

- Remove invalid entries from the status cache:

`vagrant global-status --prune`

- Prune the cache and filter results for a specific machine name:

`vagrant global-status --prune | grep {{machine_name}}`

- Output only the machine IDs for scripting:

`vagrant global-status | awk 'NR>2 && $1 !~ /^---/ {print $1}'`
