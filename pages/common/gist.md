# gist

> Upload code to https://gist.github.com

- Upload any number of files:

`gist {{file.txt}} {{file2.txt}}`

- Upload a private file with a description:

`gist -p {{file.txt}} -d {{"A meaningful description"}}`

- Read contents from STDIN with a name:

`{{echo hello world}} | gist -f {{name.rb}}`

- List public and private gists for authed user

`gist -l`

- Update existing gists with the `GIST_ID` in the URL:

`gist -u {{GIST_ID}} {{file.txt}}`
