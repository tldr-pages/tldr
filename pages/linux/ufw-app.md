# ufw app

> List, inspect, and update application profiles.
> Profiles are defined in files under `/etc/ufw/applications.d/`, not created or removed by this command.
> More information: <https://manned.org/ufw#head8>.

- List available application profiles:

`sudo ufw app list`

- Allow traffic using a specific profile:

`sudo ufw allow {{profile}}`

- Show information on a specific profile or all:

`sudo ufw app info {{[profile|all]}}`

- Apply edits on a specific profile or all to existing rules:

`sudo ufw app update {{profile|all}}`

- Update a profile's rules, applying the default application policy (replaces the existing action, or adds a rule if none exists):

`sudo ufw app update --add-new {{profile}}`

- Set the policy applied to new profiles by `ufw app update --add-new`:

`sudo ufw app default {{allow|deny|reject|skip}}`
