# prowler github

> Assess GitHub account, repository, and organization security best practices.
> See also: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`.
> More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

- Run all default GitHub security checks:

`prowler github`

- Authenticate using a GitHub Personal Access Token:

`prowler github --personal-access-token {{pat}}`

- Authenticate using a GitHub OAuth App Token:

`prowler github --oauth-app-token {{oauth_token}}`

- Authenticate using a GitHub App ID and private key:

`prowler github --github-app-id {{app_id}} --github-app-key {{app_key}}`
