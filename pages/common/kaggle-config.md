# kaggle config

> View and edit Kaggle CLI configuration values.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#config>.

- Display the current configuration:

`kaggle config view`

- Set the default competition:

`kaggle config set -n {{competition}} -v {{competition_name}}`

- Set the default download directory:

`kaggle config set -n {{path}} -v {{path/to/directory}}`

- Configure a proxy for API requests:

`kaggle config set -n {{proxy}} -v {{http://proxy:port}}`

- Unset a configuration value:

`kaggle config unset -n {{configuration_name}}`
