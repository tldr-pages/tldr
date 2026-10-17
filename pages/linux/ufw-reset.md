# ufw reset

> Reset the firewall to installation defaults.
> Disables UFW and removes all installed rules.
> More information: <https://manned.org/ufw>.

- Simulate resetting the firewall without making changes:

`sudo ufw --dry-run reset`

- Reset the firewall to defaults, prompting for confirmation:

`sudo ufw reset`

- Reset the firewall to defaults without prompting for confirmation:

`sudo ufw --force reset`
