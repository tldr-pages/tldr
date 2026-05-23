# repo

> Manage multiple Git repositories.
> Complements Git by simplifying work across multiple repositories.
> More information: <https://source.android.com/docs/setup/reference/repo>.

- Initialize a repo client in the current directory using a manifest repository:

`repo init -u {{https://android.googlesource.com/platform/manifest}}`

- Download new changes and update the working files for all projects:

`repo sync`

- Show the status of files in all projects:

`repo status`

- Create a new branch for development in the current project:

`repo start {{branch_name}} .`

- Upload changes from the current project to the review server:

`repo upload .`
