# surge

> Simple web publishing.
> More information: <https://surge.sh/help/>.

- Upload a new site to surge.sh:

`surge {{path/to/project}}`

- Deploy site to custom domain (note that the DNS records must point to the surge.sh subdomain):

`surge {{path/to/project}} {{example.com}}`

- List your surge projects:

`surge list`

- Remove a project:

`surge teardown {{example.com}}`
