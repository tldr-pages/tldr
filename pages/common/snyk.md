# snyk

> Find vulnerabilities in your code and remediate risks.
> More information: <https://snyk.io>.

- Log in to your Snyk account:

`snyk auth`

- Test your code for any known vulnerabilities:

`snyk test`

- Test a local Docker image for any known vulnerabilities:

`snyk test --docker {{docker_image}}`

- Record the state of dependencies and any vulnerabilities on snyk.io:

`snyk monitor`

- Auto patch and ignore vulnerabilities:

`snyk wizard`
