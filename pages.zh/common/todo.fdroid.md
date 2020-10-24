# fdroid

> F-Droid build tool.
> F-Droid is an installable catalogue of FOSS (Free and Open Source Software) applications for the Android platform.
> More information: <https://f-droid.org/>.

- Build a specific app:

`fdroid build {{app_id}}`

- Build a specific app in a build server VM:

`fdroid build {{app_id}} --server`

- Publish the app to the local repository:

`fdroid publish {{app_id}}`

- Install the app on every connected device:

`fdroid install {{app_id}}`

- Check if the metadata is formatted correctly:

`fdroid lint --format {{app_id}}`

- Fix the formatting automatically (if possible):

`fdroid rewritemeta {{app_id}}`
