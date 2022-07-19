# ern

> Electrode Native is a mobile platform that integrates React Native components into mobile applications.
> More information: <https://www.electrode.io/site/native.html>.

- Create a new ern application(miniapp):

`ern create-miniapp {{appName}}`

- Run one or more MiniApps in the iOS Runner application:

`ern run-ios`

- Run one or more MiniApps in the Android Runner application:

`ern run-android`

- Create an Electrode Native container:

`ern create-container -m {{/absolute/path/to/miniapp/directory}} -p {{ios|android}}`

- Publish an Electrode Native container to local Maven repository:

`ern publish-container -p {{maven}} --platform {{android}} -e {{'{"groupId":"com.walmart.ern","artifactId":"quickstart"}'}}`

- Transform container (creates an iOS framework):

`ern transform-container -p {{ios}} -t {{xcframework}}`

- List all versions of Electrode Native installed:

`ern platform versions`

- Set the ern tool logging level:

`ern platform config set logLevel {{trace|debug}}`
