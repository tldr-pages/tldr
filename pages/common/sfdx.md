# sfdx

> Command-line tool for development and build automation with a Salesforce organization.
> More information: <https://developer.salesforce.com/tools/sfdxcli>.

- Authorize a Salesforce Organization:

`sfdx force:auth:web:login --setalias {{organization}} --instanceurl {{organization_url}}`

- List all authorized organizations:

`sfdx force:org:list`

- Open a specific organization in the default web browser:

`sfdx force:org:open --targetusername {{organization}}`

- Display information about a specific organization:

`sfdx force:org:display --targetusername {{organization}}`

- Push source metadata to an Organization:

`sfdx force:source:push --targetusername {{organization}}`

- Pull source metadata from an Organization:

`sfdx force:source:pull --targetusername {{organization}}`

- Generate a password for the organization's logged-in user:

`sfdx force:user:password:generate --targetusername {{organization}}`

- Assign a permission set for the organization's logged-in user:

`sfdx force:user:permset:assign --permsetname {{permission_set_name}} --targetusername {{organization}}`
