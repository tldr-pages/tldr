# pulumi preview

> Show a preview of updates to a stack's resources.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_preview/>.

- Show a preview of updates to a stack's resources:

`pulumi preview`

- Show a preview of updates to a stack's resources in JSON format:

`pulumi preview {{[-j|--json]}}`

- Preview updates as a rich diff showing overall changes:

`pulumi preview --diff`

- Preview updates using a Policy Pack (without Pulumi Cloud, best on CI/CD):

`pulumi preview --policy-pack {{path/to/directory}}`

- Display help:

`pulumi preview {{[-h|--help]}}`
