# transcrypt

> Transparently encrypt files within a Git repository.
> More information: <https://github.com/elasticdog/transcrypt>.

- Initialize an unconfigured repository:

`transcrypt`

- List the currently encrypted files:

`git ls-crypt`

- Display the credentials of a configured repository:

`transcrypt {{[-d|--display]}}`

- Initialize and decrypt a fresh clone of a configured repository:

`transcrypt {{[-c|--cipher]}} {{cipher}}`

- Rekey to change the encryption cipher or password:

`transcrypt {{[-r|--rekey]}}`
