# toolbox init-container

> Initialize a running container.
> More information: <https://www.mankier.com/1/toolbox-init-container>.

- Pass GID as the user's numerical group ID from the host to the toolbox container:

`toolbox init-container --gid {{GID}}`

- Create a user inside the toolbox container whose login directory is HOME (Required):

`toolbox init-container --home {{HOME}}`

- Create a user inside the toolbox container whose login shell is SHELL (Required):

`toolbox init-container --shell {{SHELL}}`

- Create a user inside the toolbox container whose numerical user ID is UID (Required):

`toolbox init-container --uid {{UID}}`

- Create a user inside the toolbox container whose login name is LOGIN (Required):

`toolbox init-container {{USER}}`
