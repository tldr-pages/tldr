# gcloud CLI Authorization and Credentials

> The official CLI tool for Google Cloud Platform.
> More information: <https://cloud.google.com/sdk/docs/cheatsheet#authorization_and_credentials>.

Authorization and Credentials
Grant and revoke authorization to the gcloud CLI and manage credentials.

`gcloud auth login`: Authorize Google Cloud access for the gcloud CLI with Google Cloud user credentials and set the current account as active (https://cloud.google.com/sdk/gcloud/reference/auth/login)

`gcloud auth activate-service-account`: Authorize Google Cloud access similar to gcloud auth login but with service account credentials (https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)

`gcloud auth application-default`: Manage your Application Default Credentials (ADC) for Cloud Client Libraries (https://cloud.google.com/sdk/gcloud/reference/auth/application-default)

`gcloud auth list`: List all credentialed accounts (https://cloud.google.com/sdk/gcloud/reference/auth/list)

`gcloud auth print-access-token`: Display the current account's access token (https://cloud.google.com/sdk/gcloud/reference/auth/print-access-token)

`gcloud auth revoke`: Remove access credentials for an account (https://cloud.google.com/sdk/gcloud/reference/auth/revoke)
