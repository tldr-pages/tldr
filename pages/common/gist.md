# gist

> Upload code to https://gist.github.com.
> More information: <https://github.com/defunkt/gist>.

- Login in gist on this computer:

`gist --login`

- Create a gist from any number of text files:

`gist {{file.txt}} {{file2.txt}}`

- Create a private gist with a description:

`gist -p -d "{{A meaningful description}}" {{file.txt}} `

- Read contents from stdin and create a gist from it:

`{{echo "hello world"}} | gist`

- List your public and private gists:

`gist -l`

- List all public gists for any user:

`gist -l {{username}}`

- Update a gist using the id from URL:

`gist -u {{GIST_ID}} {{file.txt}}`
