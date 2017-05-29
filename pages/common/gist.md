# gist

> Upload code to https://gist.github.com.

- Create a gist from any number of text files:

`gist {{file.txt}} {{file2.txt}}`

- Create a private gist with a description:

`gist -p -d {{"A meaningful description"}} {{file.txt}} `

- Read contents from STDIN and create a gist from it:

`{{echo "hello world"}} | gist`

- List your public and private gists:

`gist -l`

- Use the id from the gist URL to modify or include a file:

`gist -u {{GIST_ID}} {{file.txt}}`
