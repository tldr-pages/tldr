# npm star

> Mark a package as favorite.
> More information: <https://docs.npmjs.com/cli/npm-star>.

- Star a public package from the default registry:

`npm star {{package_name}}`

- Star a package within a specific scope:

`npm star @{{scope}}/{{package_name}}`

- Star a package from a specific registry:

`npm star {{package_name}} --registry {{registry_url}}`

- Star a private package that requires authentication:

`npm star {{package_name}} --auth-type {{legacy|oauth|web|saml}}`

- Star a package by providing an OTP for two-factor authentication:

`npm star {{package_name}} --otp {{otp}}`

- Star a package with detailed logging:

`npm star {{package_name}} --loglevel verbose`

- List all your starred packages:

`npm star --list`

- List your starred packages from a specific registry:

`npm star --list --registry {{registry_url}}`
