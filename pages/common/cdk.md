# aws cdk

> CLI for AWS Cloud Development Kit (CDK)
> More information: <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>.

- Lists the stacks in the app:

`cdk ls`

- Synthesizes and prints the CloudFormation template for the specified stack(s):

`cdk synth {{stack_name}}`

- Deploys the specified stack(s):

`cdk deploy {{stack_name}}`

- Destroys the specified stack(s):

`cdk destroy {{stack_name}}`

- Compares the specified stack with the deployed stack or a local CloudFormation template:

`cdk diff {{stack_name}}`

- Creates a new CDK project in the current directory for a specified language:

`cdk init -l {{language_name}}`

- Opens the CDK API reference in your browser:

`cdk doc`
