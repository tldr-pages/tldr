# aws pricing

> Centralized and convenient way to programmatically query Amazon Web Services for services, products, and pricing information.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- List service codes of a specific region:

`aws pricing describe-services --region {{us-east-1}}`

- List attributes for a given service code in a specific region:

`aws pricing describe-services --service-code {{AmazonEC2}} --region {{us-east-1}}`

- Get pricing information for a service code:

`aws pricing get-products --service-code {{AmazonEC2}} --region {{us-east-1}}`

- Get a list of attribute values to use while filtering:

`aws pricing get-attribute-values --service-code {{AmazonEC2}} --attribute-name {{instanceType}} --region {{us-east-1}}`

- Get pricing information for a service code and attribute using a filter on the instance type and location:

`aws pricing get-products --service-code {{AmazonEC2}} --filters {{"Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge"}} {{"Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)"}} --region {{us-east-1}}`
