# npm unstar

> Remove the favorite/star mark from a package.
> More information: <https://docs.npmjs.com/cli/commands/npm-unstar>.

- Unstar a public package from the default registry:

`npm unstar {{package_name}}`

- Unstar a package within a specific scope:

`npm unstar @{{scope}}/{{package_name}}`

- Unstar a package from a specific registry:

`npm unstar {{package_name}} --registry {{registry_url}}`

- Unstar a private package that requires authentication:

`npm unstar {{package_name}} --auth-type {{legacy|oauth|web|saml}}`

- Unstar a package by providing an OTP for two-factor authentication:

`npm unstar {{package_name}} --otp {{otp}}`

- Unstar a package with a specific logging level:

`npm unstar {{package_name}} --loglevel {{silent|error|warn|notice|http|timing|info|verbose|silly}}`
