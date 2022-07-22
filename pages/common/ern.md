# ern

> Electrode Native platform command line client.
> More information: <https://native.electrode.io/reference/index-6>.

- Create a new `ern` application (`MiniApp`):

`ern create-miniapp {{appName}}`

- Run one or more `MiniApps` in the iOS Runner application:

`ern run-ios`

- Run one or more `MiniApps` in the Android Runner application:

`ern run-android`

- Create an Electrode Native container:

`ern create-container --miniapps {{/absolute/path/to/miniapp_directory}} --platform {{ios|android}}`

- Publish an Electrode Native container to local Maven repository:

`ern publish-container --publisher {{maven}} --platform {{android}} --extra {{'{"groupId":"com.walmart.ern","artifactId":"quickstart"}'}}`

- Transforms an iOS container to a pre-compiled binary framework:

`ern transform-container --platform {{ios}} --transformer {{xcframework}}`

- List all installed versions of Electrode Native:

`ern platform versions`

- Set the `ern` tool logging level:

`ern platform config set logLevel {{trace|debug}}`
