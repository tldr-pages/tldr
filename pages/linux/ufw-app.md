# ufw app

> Manage `ufw` application profiles and their associated firewall rules.
> Application profiles are defined in `/etc/ufw/applications.d/`.
> More information: <https://manned.org/ufw#head8>.

- List available application profiles:

`sudo ufw app list`

- Display information about a specific profile or all:

`sudo ufw app info {{[profile|all]}}`

- Allow traffic or deny using an specific profile:

`sudo ufw {{allow|deny}} {{profile}}`

- Update existing firewall rules after modifying a profile or all:

`sudo ufw app update {{profile|all}}`

- Update a profile's rules, applying the default application policy (replaces the existing action, or adds a rule if none exists):

`sudo ufw app update --add-new {{profile}}`

- Set the policy applied to new profiles by `ufw app update --add-new`:

`sudo ufw app default {{allow|deny|reject|skip}}`
