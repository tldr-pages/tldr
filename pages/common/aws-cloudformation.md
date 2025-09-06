# aws cloudformation

> Model, provision, and manage AWS and third-party resources by treating infrastructure as code.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html>.

- Create a stack from a template file:

`aws cloudformation create-stack --stack-name {{stack-name}} --region {{region}} --template-body {{file://path/to/file.yml}} --profile {{profile}}`

- Delete a stack:

`aws cloudformation delete-stack --stack-name {{stack-name}} --profile {{profile}}`

- List all stacks:

`aws cloudformation list-stacks --profile {{profile}}`

- List all running stacks:

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile {{profile}}`

- Check the status of a stack:

`aws cloudformation describe-stacks --stack-name {{stack-id}} --profile {{profile}}`

- Initiate drift detection for a stack:

`aws cloudformation detect-stack-drift --stack-name {{stack-id}} --profile {{profile}}`

- Check the drift status output of a stack using 'StackDriftDetectionId' from the previous command output:

`aws cloudformation describe-stack-resource-drifts --stack-name {{stack-drift-detection-id}} --profile {{profile}}`
