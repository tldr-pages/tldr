# Surge

> Simple, single-command web publishing.

- Upload a new site:

`surge {{ /path/to/my-project }}`

- Deploy site to custom domain (note DNS records must be changed on domain):

`surge {{ path/to/my-project }} {{ my-custom-domain.com }}`

- List your surge projects:

`surge list`

- Remove a project:

`surge teardown {{ your.project-domain.com }}`
