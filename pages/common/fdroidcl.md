# fdroidcl

> Manage F-Droid apps of devices connected via ADB.
> More information: <https://github.com/mvdan/fdroidcl>.

- Fetch the F-Droid index:

`fdroidcl update`

- Display information about an app:

`fdroidcl show {{app_id}}`

- Download the APK file of an app:

`fdroidcl download {{app_id}}`

- Search for an app in the index:

`fdroidcl search {{search_pattern}}`

- Install an app on a connected device:

`fdroidcl install {{app_id}}`

- Add a repository:

`fdroidcl repo add {{repo_name}} {{url}}`

- Remove, enable or disable a repository:

`fdroidcl repo {{remove|enable|disable}} {{repo_name}}`
