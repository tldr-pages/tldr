# eselect repository

> Un modulo `eselect` per la configurazione dei repository ebuild per Portage.
> Dopo aver abilitato un repository, è necessario eseguire `emerge --sync nome_repo` per scaricare gli ebuild.
> Maggiori informazioni: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- Elenca tutti i repository ebuild registrati su <https://repos.gentoo.org>:

`eselect repository list`

- Elenca i repository abilitati:

`eselect repository list -i`

- Abilita un repository dall'elenco per nome o indice dal comando `list`:

`eselect repository enable {{nome|indice}}`

- Abilita un repository non registrato:

`eselect repository add {{nome}} {{rsync|git|mercurial|svn|...}} {{sync_uri}}`

- Disabilita i repository senza rimuovere il loro contenuto:

`eselect repository disable {{repo1 repo2 ...}}`

- Disabilita i repository e rimuove il loro contenuto:

`eselect repository remove {{repo1 repo2 ...}}`

- Crea un repository locale e lo abilita:

`eselect repository create {{nome}} {{path/to/repo}}`
