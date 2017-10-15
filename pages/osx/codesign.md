# codesign

> Create and manipulate code signatures for macOS.

- Sign an application with your certificate:

`codesign -s {{"My Company Name"}} {{/path/to/App.app}}`

- Verify the certificate of an application:

`codesign -v {{/path/to/App.app}}`
