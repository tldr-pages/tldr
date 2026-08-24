# apkeep

> Download APK files from various sources.
> More information: <https://github.com/EFForg/apkeep/blob/master/USAGE>.

- Download an APK file to the specified directory:

`apkeep {{[-a|--app]}} {{com.example.application}} {{path/to/directory}}`

- List all available versions for download:

`apkeep {{[-a|--app]}} {{com.example.application}} {{[-l|--list-versions]}}`

- Download a specific version of an APK file:

`apkeep {{[-a|--app]}} {{com.example.application}}@{{app_version}} {{path/to/directory}}`

- Specify a store to download from:

`apkeep {{[-a|--app]}} {{com.example.application}} {{[-d|--download-source]}} {{apk-pure|google-play|f-droid|huawei-app-gallery}} {{path/to/directory}}`

- Display help:

`apkeep {{[-h|--help]}}`
