# aws cur

> Create, query, and delete AWS usage report definitions.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- Create an AWS cost and usage report definition from a JSON file:

`aws cur put-report-definition --report-definition file://{{path/to/report_definition.json}}`

- List usage report definitions defined for the logged in account:

`aws cur describe-report-definitions`

- Delete a usage report definition:

`aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}`
