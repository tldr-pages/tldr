# codesign

> Create and manipulate code signatures for macOS.
> More information: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

- Sign an application with a certificate:

`codesign --sign "{{My Company Name}}" {{path/to/application_file.app}}`

- Verify the certificate of an application:

`codesign --verify {{path/to/application_file.app}}`
