# apptainer capability

> Manage Linux capabilities for users and groups.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_capability.html>.

- Show all available Linux capabilities:

`apptainer capability avail`

- Show description for specific capabilities:

`apptainer capability avail {{cap_chown,cap_net_raw,...}}`

- List capabilities for all users and groups:

`apptainer capability list`

- List capabilities for a specific user or group:

`apptainer capability list {{username|groupname}}`

- Add capabilities to a user:

`sudo apptainer capability add {{[-u|--user]}} {{username}} {{cap_net_raw,cap_chown,...}}`

- Add capabilities to a group:

`sudo apptainer capability add {{[-g|--group]}} {{groupname}} {{cap_net_raw,cap_chown,...}}`

- Remove capabilities from a user:

`sudo apptainer capability drop {{[-u|--user]}} {{username}} {{cap_net_raw,cap_chown,...}}`

- Remove all capabilities from a user:

`sudo apptainer capability drop {{[-u|--user]}} {{username}} all`
