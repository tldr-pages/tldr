# ibmcloud config

> Modify or read out values in the IBM Cloud CLI configuration.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_config>.

- Set HTTP request timeout to 30 seconds:

`ibmcloud config --http-timeout 30`

- Enable trace output for HTTP requests:

`ibmcloud config --trace true`

- Trace HTTP requests to a specific file:

`ibmcloud config --trace {{path/to/trace_file}}`

- Disable color output:

`ibmcloud config --color false`

- Set the locale to a specific language:

`ibmcloud config --locale {{zh_Hans}}`

- Enable automatic SSO one-time passcode acceptance:

`ibmcloud config --sso-otp auto`
