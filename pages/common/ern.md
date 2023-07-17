# ern

> Electrode Native platform command-line client.
> More information: <https://native.electrode.io/reference/index-6>.

- Create a new `ern` application (`MiniApp`):

`ern create-miniapp {{application_name}}`

- Run one or more `MiniApps` in the iOS/Android Runner application:

`ern run-{{ios|android}}`

- Create an Electrode Native container:

`ern create-container --miniapps {{/path/to/miniapp_directory}} --platform {{ios|android}}`

- Publish an Electrode Native container to a local Maven repository:

`ern publish-container --publisher {{maven}} --platform {{android}} --extra {{'{"groupId":"com.walmart.ern","artifactId":"quickstart"}'}}`

- Transform an iOS container into a pre-compiled binary framework:

`ern transform-container --platform {{ios}} --transformer {{xcframework}}`

- List all installed versions of Electrode Native:

`ern platform versions`

- Set a logging level:

`ern platform config set logLevel {{trace|debug}}`
