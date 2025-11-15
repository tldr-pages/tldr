# gcloud auth

> Grant and revoke authorization to `gcloud` and manage credentials.
> See also: `gcloud`.
> More information: <https://cloud.google.com/sdk/gcloud/reference/auth>.

- Authorize Google Cloud access for the `gcloud` CLI with Google Cloud user credentials and set the current account as active:

`gcloud auth login`

- Authorize Google Cloud access similar to `gcloud auth login` but with service account credentials:

`gcloud auth activate-service-account`

- Manage Application Default Credentials (ADC) for Cloud Client Libraries:

`gcloud auth application-default`

- Display a list of Google Cloud accounts currently authenticated on your system:

`gcloud auth list`

- Display the current account's access token:

`gcloud auth print-access-token`

- Remove access credentials for an account:

`gcloud auth revoke`
