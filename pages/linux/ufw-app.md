# ufw app

> Manage `ufw` application profiles and their associated firewall rules.
> Application profiles are defined in `/etc/ufw/applications.d/`.
> More information: <https://manned.org/ufw#head8>.

- List available application profiles:

`sudo ufw app list`

- Display information about a specific or all profiles:

`sudo ufw app info {{profile|all}}`

- Allow or deny traffic using an specific profile:

`sudo ufw {{allow|deny}} {{profile}}`

- Update existing firewall rules after modifying a profile or all:

`sudo ufw app update {{profile|all}}`

- Update an application profile, applying the default policy if new:

`sudo ufw app update --add-new {{profile}}`

- Set the default policy applied to new profiles:

`sudo ufw app default {{allow|deny|reject|skip}}`
