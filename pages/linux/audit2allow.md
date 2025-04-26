# audit2allow

> Create an SELinux local policy module to allow rules based on denied operations found in logs.
> Note: Use audit2allow with caution. Always review the generated policy before applying it, as it may allow excessive access.
> More information: <https://manned.org/audit2allow>.

- Generate a local policy to allow access for all denied services:

`sudo audit2allow {{[-a|--all]}} -M {{local_policy_name}}`

- Generate a local policy module to grant access to a specific process/service/command from the audit logs:

`sudo grep {{apache2}} /var/log/audit/audit.log | sudo audit2allow -M {{local_policy_name}}`

- Inspect and review the Type Enforcement (.te) file for a local policy:

`vim {{local_policy_name}}.te`

- Install a local policy module:

`sudo semodule {{[-i|--install]}} {{local_policy_name}}.pp`
