# glab config

> Manage configuration settings for the GitLab CLI.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/config/_index.md>.

- Display the value of a specific configuration key:

`glab config get {{key}}`

- Display the value of a configuration key from the global configuration file:

`glab config get {{key}} {{[-g|--global]}}`

- Display the value of a configuration key for a specific host:

`glab config get {{key}} --host {{host}}`

- Set a configuration key to a specific value:

`glab config set {{key}} "{{value}}"`

- Set a configuration key globally:

`glab config set {{key}} "{{value}}" {{[-g|--global]}}`

- Set a configuration key for a specific host:

`glab config set {{key}} "{{value}}" --host {{host}}`

- Open the local configuration file in the default text editor:

`glab config edit {{[-l|--local]}}`

- Display the path to the global configuration file:

`glab config path`
