# sf

> A powerful command line interface that simplifies development and build automation when working with your Salesforce org.
> More information: <https://developer.salesforce.com/tools/salesforcecli>.

- Authorize a Salesforce Organization:

`sf force:auth:web:login --setalias {{organization}} --instanceurl {{organization_url}}`

- List all authorized organizations:

`sf force:org:list`

- Open a specific organization in the default web browser:

`sf force:org:open --targetusername {{organization}}`

- Display information about a specific organization:

`sf force:org:display --targetusername {{organization}}`

- Push source metadata to an Organization:

`sf force:source:push --targetusername {{organization}}`

- Pull source metadata from an Organization:

`sf force:source:pull --targetusername {{organization}}`

- Generate a password for the organization's logged-in user:

`sf force:user:password:generate --targetusername {{organization}}`

- Assign a permission set for the organization's logged-in user:

`sf force:user:permset:assign --permsetname {{permission_set_name}} --targetusername {{organization}}`
