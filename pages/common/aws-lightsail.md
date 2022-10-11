# aws lightsail

> CLI for Lightsail.
> You can manage your Lightsail resources using the cli.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html>.

- List all Amazon Lightsail virtual private servers, or instances:

`aws lightsail get-instances`

- List all Lightsail bundles (instance plans):

`aws lightsail list-bundles`


- List all available instance images, or blueprints:

`aws lightsail list-blueprints`

- Create an instance:

`aws lightsail create-instances --instance-names {{name}} --availability-zone {{ap-southeast-1a}} --bundle-id {{nano_2_0}} --blueprint-id {{nodejs}}`

- Get instance state:

`aws lightsail get-instance-state --instance-name {{name}}`

- Stop instance:

`aws lightsail stop-instance --instance-name {{name}}`

- Delete instance:

`aws lightsail delete-instance --instance-name {{name}}`