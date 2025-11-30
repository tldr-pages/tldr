# gist

> Upload code to <https://gist.github.com>.
> More information: <https://github.com/defunkt/gist>.

- Log in to gist on this computer:

`gist --login`

- Create a gist from any number of text files:

`gist {{file.txt}} {{file2.txt}}`

- Create a private gist with a description:

`gist {{[-p|--private]}} {{[-d|--description]}} "{{A meaningful description}}" {{file.txt}}`

- Read contents from `stdin` and create a gist from it:

`{{echo "hello world"}} | gist`

- List your public and private gists:

`gist {{[-l|--list]}}`

- List all public gists for any user:

`gist {{[-l|--list]}} {{username}}`

- Update a gist using the ID from URL:

`gist {{[-u|--update]}} {{GIST_ID}} {{file.txt}}`
