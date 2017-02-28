# carthage

> Carthage is a dependency management tool for Cocoa applications.
> Download and build all dependencies mentioned in Cartfile.
> Also used to update dependencies to their latest version.

- Fetch and build the current set of dependencies:

`carthage update`

- Update dependencies and only build for iOS:

`carthage update --platform ios`

- Update dependencies but don't build:

`carthage update --no-build`

- Download and rebuild the current dependency set without updating:

`carthage bootstrap`

- Rebuild a specific dependency:

`carthage build {{dependency}}`
