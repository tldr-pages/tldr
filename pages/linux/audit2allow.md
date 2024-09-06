# audit2allow

> Create an SELinux local policy module to allow rules based on denied operations found in logs.
> More information: <https://man7.org/linux/man-pages/man1/audit2why.1.html>.

- Generate and install a local policy to allow access for all denied services:

`sudo audit2allow --all -M {{local_policy_name}} && sudo semodule -i {{local_policy_name}}.pp`

- Generate and install a local policy module to grant access to a specific process/service/command from the audit logs:

`sudo grep {{apache2}} /var/log/audit/audit.log | sudo audit2allow -M {{local_policy_name}} && sudo semodule -i {{local_policy_name}}.pp`

- View the Type Enforcement (.te) file for a local policy:

`cat {{local_policy_name}}.te`
