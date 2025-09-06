# aws route53

> CLI for AWS Route53 - Route 53 is a highly available and scalable Domain Name System (DNS) web service.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html>.

- List all hosted zones, private and public:

`aws route53 list-hosted-zones`

- Show all records in a zone:

`aws route53 list-resource-record-sets --hosted-zone-id {{zone_id}}`

- Create a new, public zone using a request identifier to retry the operation safely:

`aws route53 create-hosted-zone --name {{name}} --caller-reference {{request_identifier}}`

- Delete a zone (if the zone has non-defaults SOA and NS records the command will fail):

`aws route53 delete-hosted-zone --id {{zone_id}}`

- Test DNS resolving by Amazon servers of a given zone:

`aws route53 test-dns-answer --hosted-zone-id {{zone_id}} --record-name {{name}} --record-type {{type}}`
