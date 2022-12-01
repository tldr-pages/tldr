# fossil commit

> Commit files to a Fossil repository.
> More information: <https://fossil-scm.org/home/help/commit>.

- Create a new version containing all the changes in the current checkout; user will be prompted for a comment:

`fossil commit`

- Create a new version containing all the changes in the current checkout, using the specified comment:

`fossil commit --comment "{{comment}}"`

- Create a new version containing all the changes in the current checkout with a comment read from a specific file:

`fossil commit --message-file {{path/to/commit_message_file}}`

- Create a new version containing changes from the specified files; user will be prompted for a comment:

`fossil commit {{path/to/file1 path/to/file2 ...}}`
