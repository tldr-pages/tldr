# codesign

> Sign code for the Mac certificate store.

- Link a certificate to your application:

`codesign -s "My Company Name" /path/to/App.app`

- Verify a certificate to an application:

`codesign -v /path/to/App.app`
