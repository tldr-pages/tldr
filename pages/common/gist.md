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

- Update existing gists with the `GIST_ID` in the URL:

`gist -u {{GIST_ID}} {{file.txt}}`
