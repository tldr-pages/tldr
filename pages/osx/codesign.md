# codesign

> Create and manipulate code signatures for macOS.
> More information: <https://www.unix.com/man-page/osx/1/codesign/>.

- Sign an application with a certificate:

`codesign --sign "{{My Company Name}}" {{path/to/App.app}}`

- Verify the certificate of an application:

`codesign --verify {{path/to/App.app}}`
