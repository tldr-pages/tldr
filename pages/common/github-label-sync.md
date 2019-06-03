# github-label-sync

> A command line interface for synchronising GitHub labels.
> More information: <https://npmjs.com/package/github-label-sync>.

- Synchronise labels using a local `labels.json` file:

`github-label-sync --access-token {{token}} {{repository_name}}`

- Synchronise labels using a specific labels JSON file:

`github-label-sync --access-token {{token}} --labels {{url|path/to/json_file}} {{repository_name}}`

- Perform a dry run instead of actually synchronising labels:

`github-label-sync --access-token {{token}} --dry-run {{repository_name}}`

- Keep labels that aren't in `labels.json`:

`github-label-sync --access-token {{token}} --allow-added-labels {{repository_name}}`

- Synchronise using the `GITHUB_ACCESS_TOKEN` environment variable:

`github-label-sync {{repository_name}}`
