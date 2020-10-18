# aws cdk

> CLI for AWS Cloud Development Kit (CDK).
> More information: <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>.

- List the stacks in the app:

`cdk ls`

- Synthesize and print the CloudFormation template for the specified stack(s):

`cdk synth {{stack_name}}`

- Deploy the specified stack(s):

`cdk deploy {{stack_name}}`

- Destroy the specified stack(s):

`cdk destroy {{stack_name}}`

- Compare the specified stack with the deployed stack or a local CloudFormation template:

`cdk diff {{stack_name}}`

- Create a new CDK project in the current directory for a specified language:

`cdk init -l {{language_name}}`

- Open the CDK API reference in your browser:

`cdk doc`
