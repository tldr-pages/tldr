# ufw app

> Manage application profiles for Uncomplicated Firewall.
> Profiles live in `/etc/ufw/applications.d` and can be referenced by name in rules.
> More information: <https://manned.org/ufw>.

- List application profiles known to `ufw`:

`sudo ufw app list`

- Show ports and description for a profile:

`sudo ufw app info {{application_name}}`

- Show details for every known application profile:

`sudo ufw app info all`

- Allow traffic using an application profile name:

`sudo ufw allow {{application_name}}`

- Allow a profile only from a specific network:

`sudo ufw allow from {{192.168.0.0/16}} to any app {{application_name}}`

- Update firewall rules after editing a profile:

`sudo ufw app update {{application_name}}`

- Update a profile and automatically add a new rule for it:

`sudo ufw app update --add-new {{application_name}}`

- Set the default policy used by `app update --add-new` (`skip` is the default):

`sudo ufw app default {{skip|allow|deny}}`
