# sdk

> Manage parallel versions of multiple Software Development Kits.
> Supports Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x and many others.
> More information: <https://sdkman.io/usage>.

- Install an SDK version:

`sdk install {{sdk_name}} {{sdk_version}}`

- Use a specific SDK version for the current terminal session:

`sdk use {{sdk_name}} {{sdk_version}}`

- Show the stable version of any available SDK:

`sdk current {{sdk_name}}`

- Show the stable versions of all installed SDKs:

`sdk current`

- List all available SDKs:

`sdk list`

- List all versions of an SDK:

`sdk list {{sdk_name}}`

- Upgrade an SDK to the latest stable version:

`sdk upgrade {{sdk_name}}`

- Uninstall a specific SDK version:

`sdk rm {{sdk_name}} {{sdk_version}}`
