# ufw app

> Manage `ufw` application profiles and their associated firewall rules.
> Application profiles are defined in `/etc/ufw/applications.d/`.
> More information: <https://manned.org/ufw#head8>.

- List available application profiles:

`sudo ufw app list`

- Display information about a specific or all profiles:

`sudo ufw app info {{profile_name|all}}`

- Allow or deny traffic using a specific profile:

`sudo ufw {{allow|deny}} "{{profile_name}}"`

- Update firewall rules for a modified profile or all profiles:

`sudo ufw app update {{profile_name|all}}`

- Update a profile, adding new rules if none exist:

`sudo ufw app update --add-new "{{profile_name}}"`

- Configure the default behavior of `update --add-new`:

`sudo ufw app default {{allow|deny|reject|skip}}`
