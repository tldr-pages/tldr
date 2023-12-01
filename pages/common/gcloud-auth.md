# gcloud CLI Authorization and Credentials

> Grant and revoke authorization to the gcloud CLI and manage credentials.
> More information: <https://cloud.google.com/sdk/docs/cheatsheet#authorization_and_credentials>.

- Authorize Google Cloud access for the gcloud CLI with Google Cloud user credentials and set the current account as active:

`gcloud auth login`

- Authorize Google Cloud access similar to gcloud auth login but with service account credentials:

`gcloud auth activate-service-account`

- Manage your Application Default Credentials (ADC) for Cloud Client Libraries:

`gcloud auth application-default`

- List all credentialed accounts:

`gcloud auth list`

- Display the current account's access token:

`gcloud auth print-access-token`

- Remove access credentials for an account:

`gcloud auth revoke`
