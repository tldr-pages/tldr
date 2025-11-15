# git init

> Initialiseer een nieuwe lokale Git-repository.
> Meer informatie: <https://git-scm.com/docs/git-init>.

- Initialiseer een nieuwe lokale repository:

`git init`

- Initialiseer een repository met de opgegeven naam voor de initiële branch:

`git init {{[-b|--initial-branch]}} {{branch_naam}}`

- Initialiseer een repository die SHA256 gebruikt voor object-hashes (vereist Git-versie 2.29+):

`git init --object-format sha256`

- Initialiseer een eenvoudige repository, geschikt voor gebruik als externe SSH-server:

`git init --bare`
