# git column

> Display data in columns.
> More information: <https://git-scm.com/docs/git-column>.

- Format `stdin` as multiple columns:

`ls | git column --mode={{column}}`

- Format `stdin` as multiple columns with a maximum width of `100`:

`ls | git column --mode=column --width={{100}}`

- Format `stdin` as multiple columns with a maximum padding of `30`:

`ls | git column --mode=column --padding={{30}}`
