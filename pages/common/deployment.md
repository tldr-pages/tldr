# deployment

> Automatically pull Git repositories and run their `deploy` scripts.
> Reads deployments as `path,repository_url` rows from a CSV file.
> More information: <https://github.com/chrissxMedia/deployment>.

- Continuously deploy repositories listed in `/etc/deployments.csv`, using `/var/deployment` as the base directory for relative paths:

`deployment`

- Use a specific deployment list and base directory:

`deployment {{[-d|--deployments]}} {{path/to/deployments.csv}} {{[-H|--home]}} {{path/to/directory}}`

- Clone repositories that are missing locally, then exit:

`deployment {{[-c|--clone-only]}}`

- Simulate a deployment pass by printing commands without executing them:

`deployment {{[-n|--dry-run]}}`

- Set the delay in seconds after each deployment:

`deployment --delay {{60}}`

- Move build output from each repository's `dist` directory under the base directory's `dist` directory:

`deployment {{[-D|--global-dist]}}`
