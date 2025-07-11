# pulumi schema

> Check a Pulumi package schema for errors.
> Schema reference: <https://www.pulumi.com/docs/iac/extending-pulumi/schema/>.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_schema/>.

- Check a package schema:

`pulumi schema check {{path/to/file}}`

- Check a package schema without failing if the reference to a type is missing:

`pulumi schema check --allow-dangling-references {{path/to/file}}`

- Display help:

`pulumi schema check {{[-h|--help]}}`
