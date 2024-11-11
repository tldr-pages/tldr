# pulumi convert

> Convert Pulumi programs from a supported source program into other supported languages.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_convert/>.

- Convert Pulumi programs from a supported source program into other supported languages:

`pulumi convert`

- Specify which converter plugin Pulumi should use use to read the source program (default "yaml"):

`pulumi convert --from {{converter_plugin}}`

- Generate the converted program(s) only:

`pulumi convert --generate-only`

- Specify which language plugin to use to generate the Pulumi project:

`pulumi convert --language {{language_plugin}}`

- Specify any mapping files to use in the conversion:

`pulumi convert --mappings {{mapping_files}}`

- Specify the name to use for the converted project:

`pulumi convert --name {{converted_project}}`
