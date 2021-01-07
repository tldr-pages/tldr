# git column

> Display data in columns.
> More information: <https://git-scm.com/docs/git-column>.

- List files and folders in the current directory, formatted as columns:

`ls | git column --mode=column`

- List files and folders in the current directory, formatted as columns with a maximum width of `100`:

`ls | git column --mode=column --width={{100}}`

- List files and folders in the current directory, formatted as columns with a maximum padding of `30`:

`ls | git column --mode=column --padding={{30}}`
