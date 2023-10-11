# gh browse

> Open a GitHub repository in the browser or print the URL.
> More information: <https://cli.github.com/manual/gh_browse>.

- Open the homepage of the current repository in the default web browser:

`gh browse`

- Open the homepage of a specific repository in the default web browser:

`gh browse {{owner}}/{{repository}}`

- Open the settings page of the current repository in the default web browser:

`gh browse --settings`

- Open the wiki of the current repository in the default web browser:

`gh browse --wiki`

- Open a specific issue or pull request in the web browser:

`gh browse {{issue_number|pull_request_number}}`

- Open a specific branch in the web browser:

`gh browse --branch {{branch_name}}`

- Open a specific file or directory of the current repository in the web browser:

`gh browse {{path/to/file_or_directory}}`

- Print the destination URL without open the web browser:

`gh browse --no-browser`
