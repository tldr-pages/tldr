# sfdx

> Salesforce CLI is a powerful command line interface that simplifies development and build automation when working with your Salesforce org.
> More information: <https://developer.salesforce.com/tools/sfdxcli>.

- Authorize a Salesforce Org:

`sfdx force:auth:web:login -a {{org_alias}} -r {{org_url}}`

- List all authorized Orgs:

`sfdx force:org:list`

- Open an Org in your Browser:

`sfdx force:org:open -u {{org_alias}}`

- Display Org information:

`sfdx force:org:display -u {{org_alias}}`

- Push source meta data to an Org:

`sfdx force:source:push -u {{org_alias}}`

- Pull source meta data from an Org:

`sfdx force:source:pull -u {{org_alias}}`

- Generate a password for your Org user:

`sfdx force:user:password:generate -u {{org_alias}}`

- Assign a permission set to your Org user:

`sfdx force:user:permset:assign -n {{permission_set_name}} -u {{org_alias}}`
