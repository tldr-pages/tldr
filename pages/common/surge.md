# Surge

> Simple, single-command web publishing.

- Upload a new site to surge.sh:

`surge {{ /path/to/my-project }}`

- Deploy site to custom domain (note that the DNS records must be changed on the domain):

`surge {{ path/to/my-project }} {{ my-custom-domain.com }}`

- List your surge projects:

`surge list`

- Remove a project:

`surge teardown {{ your.project-domain.com }}`
