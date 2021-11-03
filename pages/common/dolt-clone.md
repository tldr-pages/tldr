# dolt clone

> Clone a repository into a new directory.
> More information: <https://docs.dolthub.com/interfaces/cli#dolt-clone>.

- Clone an existing repository into a specific directory (defaults to the repository name):

`dolt clone {{repository_url}} {{directory_name}}`

- Clone an existing repository and add a specific remote (defaults to origin):

`dolt clone --remote {{remote_name}} {{repository_url}}`

- Clone a branch in the repository (defaults to all branches):

`dolt clone --branch {{branch_name}} {{repository_url}}`

- Clone a repository, using an AWS region (uses the profile's default region if none is provided):

`dolt clone --aws-region {{region_name}} {{repository_url}}`

- Clone a repository, using an AWS credentials file:

`dolt clone --aws-creds-file {{creds_file}} {{repository_url}}`

- Clone a repository, using an AWS credentials profile (uses the default profile if none is provided):

`dolt clone --aws-creds-profile {{profile_name}} {{repository_url}}`

- Clone a repository, using an AWS credentials type:

`dolt clone --aws-creds-type {{creds_type}} {{repository_url}}`
