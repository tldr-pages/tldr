# ibmcloud login

> Log in to the IBM Cloud.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>.

- Log in by using an interactive prompt:

`ibmcloud login`

- Log in to a specific API endpoint (default is `cloud.ibm.com`):

`ibmcloud login -a {{api_endpoint}}`

- Log in by providing username, password and the targeted region as parameters:

`ibmcloud login -u {{username}} -p {{password}} -r {{us-south}}`

- Log in with an API key, passing it as an argument:

`ibmcloud login --apikey {{api_key_string}}`

- Log in with an API key, passing it as a file:

`ibmcloud login --apikey @{{path/to/api_key_file}}`

- Log in with a federated ID (single sign-on):

`ibmcloud login --sso`
