# pulumi import

> Import resources into an existing stack.
> Read syntax for your cloud provider: <https://www.pulumi.com/registry/>.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_import/>.

- Generate the resource definition for existing provider resource and name it {{name}}:

`pulumi import {{type_token}} {{name}} {{id}}`

- Import your existing aws user as a pulumi resource:

`pulumi import aws:iam/user:User {{my_user_resource}} {{id}}`

- Import your existing cloudflare worker:

`pulumi import cloudflare:index/workersScript:WorkersScript {{my_worker_script}} {{account_id/script_name}}`

- Import from a JSON file for bulk import operations and output to a file instead of stdout:

`pulumi import --file {{path/to/file.json}} --out {{path/to/file}}`
