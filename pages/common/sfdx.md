# sfdx

> Salesforce CLI is a powerful command line interface that simplifies development and build automation when working with your Salesforce org.
> More information: <https://developer.salesforce.com/tools/sfdxcli>.

- Authorize a Salesforce Org:

`sfdx force:auth:web:login -a {{Org Alias}} -r {{Org URL}}`

- List all authorized Orgs:

`sfdx force:org:list`

- Open an Org in your Browser:

`sfdx force:org:open -u {{Org Alias}}`

- Display Org information:

`sfdx force:org:display -u {{Org Alias}}`

- Push source meta data to an Org

`sfdx force:source:push -u {{Org Alias}}`

- Pull source meta data from an Org

`sfdx force:source:pull -u {{Org Alias}}`

- Generate a password for your Org user:

`sfdx force:user:password:generate -u {{Org Alias}}`

- Assign a permission set to your Org user:

`sfdx force:user:permset:assign -n {{Permission Set Name}} -u {{Org Alias}}`

- Check Salesforce CLI version

`sfdx -v`

- Check and update Salesforce CLI

`sfdx update`