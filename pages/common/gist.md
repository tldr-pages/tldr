# gist

> Upload code to https://gist.github.com.
> More information: <https://github.com/defunkt/gist>.

- Login in gist on this computer:

`gist --login`

- Create a gist from any number of text files:

`gist {{file.txt}} {{file2.txt}}`

- Create a private gist with a description:

`gist --private --description "{{A meaningful description}}" {{file.txt}} `

- Read contents from stdin and create a gist from it:

`{{echo "hello world"}} | gist`

- List your public and private gists:

`gist --list`

- List all public gists for any user:

`gist --list {{username}}`

- Update a gist using the id from URL:

`gist --update {{GIST_ID}} {{file.txt}}`
