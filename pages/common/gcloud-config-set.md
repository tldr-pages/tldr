# gcloud config set

> Set a property in the Google Cloud CLI configuration.
> Properties control various aspects of Google Cloud CLI behavior.
> More information: <https://cloud.google.com/sdk/gcloud/reference/config/set>.

- Set the project property in the core section:

`gcloud config set project {{project_id}}`

- Set the compute zone for future operations:

`gcloud config set compute/zone {{zone_name}}`

- Disable prompting to make gcloud suitable for scripting:

`gcloud config set disable_prompts true`

- View the list of properties currently in use:

`gcloud config list`

- Unset a previously set property:

`gcloud config unset {{property_name}}`

- Create a new configuration profile:

`gcloud config configurations create {{configuration_name}}`

- Switch between different configuration profiles:

`gcloud config configurations activate {{configuration_name}}`
