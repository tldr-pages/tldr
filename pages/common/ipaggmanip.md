# ipaggmanip

> Manipulate aggregate statistics produced by `ipaggcreate`.
> More information: <https://read.seas.harvard.edu/~kohler/ipsumdump/aggmanipman.html>.

- Combine labels equal in their {{16}} high-order bits:

`ipaggmanip -p {{16}} {{path/to/file}}`

- Remove labels with a count smaller than {{100}} and output a random sample of at most {{5}} such labels:

`ipaggmanip --cut-smaller {{100}} --cull-labels {{5}} {{path/to/file}}`

- Replace each label's count with 1 if it is non-zero:

`ipaggmanip -P {{path/to/file}}`
