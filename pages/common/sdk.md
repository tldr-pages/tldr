# sdk

> Tool for managing parallel versions of multiple Software Development Kits.
> Supports Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x and many others.
> More information: <https://sdkman.io/usage>.

- Install an SDK version:

`sdk install {{sdk_name}} {{sdk_version}}`

- Use a specific SDK version in the current terminal:

`sdk use {{sdk_name}} {{sdk_version}}`

- Show the stable version of a SDK:

`sdk current {{sdk_name}}`

- Show the stable versions of installed SDKs:

`sdk current`

- List all SDKs:

`sdk list`

- List all versions of a SDK:

`sdk list {{sdk_name}}`

- Upgrade a SDK to the latest stable version:

`sdk upgrade {{sdk_name}}`

- Uninstall a SDK version:

`sdk rm {{sdk_name}} {{sdk_version}}`
