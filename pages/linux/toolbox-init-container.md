# toolbox init-container

> Initialize a running container.
> More information: <https://www.mankier.com/1/toolbox-init-container>.

- Pass gid as the user's numerical group ID from the host to the `toolbox` container:

`toolbox init-container --gid {{gid}}`

- Create a user inside the toolbox container whose login directory is home (Required):

`toolbox init-container --home {{home}}`

- Create a user inside the `toolbox` container whose login shell is shell (Required):

`toolbox init-container --shell {{shell}}`

- Create a user inside the `toolbox` container whose numerical user id is uid (Required):

`toolbox init-container --uid {{uid}}`

- Create a user inside the `toolbox` container whose login name is login (Required):

`toolbox init-container {{user}}`
