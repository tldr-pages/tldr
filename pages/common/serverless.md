# serverless

> Toolkit for deploying and operating serverless architectures on AWS, Google Cloud, Azure and IBM OpenWhisk.
> Commands can be run either using the `serverless` command or it's alias, `sls`.
> More information: <https://serverless.com/>.

- Create a serverless project:

`serverless create`

- Create a serverless project from a template:

`serverless create --template {{template_name}}`

- Deploy to a cloud provider:

`serverless deploy`

- Display information about a serverless project:

`serverless info`

- Invoke a deployed function:

`serverless invoke -f {{function_name}}`

- Follow the logs for a project:

`serverless logs -t`
