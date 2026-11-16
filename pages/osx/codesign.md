# codesign

> Create and manipulate code signatures for macOS.
> More information: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

- Sign an application with a certificate:

`codesign --sign "{{My Company Name}}" {{path/to/application_file.app}}`

- Verify an application's code signature:

`codesign --verify {{path/to/application_file.app}}`

- Display detailed information about an application's code signature:

`codesign --display --verbose=4 {{path/to/application_file.app}}`

- Display the entitlements embedded in an application's signature:

`codesign --display --entitlements - {{path/to/application_file.app}}`

- Sign a binary with an ad-hoc signature, without a certificate:

`codesign --sign - {{path/to/binary}}`
