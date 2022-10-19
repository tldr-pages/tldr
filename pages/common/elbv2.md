# aws elbv2

> Helps create Elastic Load balancers using AWS CLI.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/elbv2/>.

- Verify if the the AWS CLI version is supported:

`aws elbv2 help`

- Create an Application Load Balancer:

`aws elbv2 create-load-balancer --name {{my-load-balancer}}  \ --subnets {{subnet-0e3f5cac72EXAMPLE subnet-081ec835f3EXAMPLE}} --security-groups {{sg-07e8ffd50fEXAMPLE}}`

- Create dualstack load balancer:

`aws elbv2 create-load-balancer --name {{my-load-balancer}}  \--subnets {{subnet-0e3f5cac72EXAMPLE subnet-081ec835f3EXAMPLE}} --security-groups {{sg-07e8ffd50fEXAMPLE}} --ip-address-type dualstack`

- Create a target group:

`aws elbv2 create-target-group --name {{my-targets}} --protocol {{HTTP}} --port {{80}} \ --vpc-id {{vpc-0598c7d356EXAMPLE}} --ip-address-type {{ipv4/ipv6}}`
