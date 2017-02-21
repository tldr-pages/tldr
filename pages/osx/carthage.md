# carthage

> Carthage is a dependency management tool for Swift and Objective-C.

- Update the current set of dependencies:

`carthage update`

- Update dependencies and only build for iOS:

`carthage update --platform ios`

- Update dependencies but dont bulid:

`carthage update --no-build`

- Download and rebuild the current dependency set with out updating:

`carthage bootstrap`

- Rebuild a specific dependency:

`carthage build {{dependency}}`
