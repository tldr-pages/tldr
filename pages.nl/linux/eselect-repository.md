# eselect repository

> Een `eselect`-module voor het configureren van ebuild-repositories voor Portage.
> Na het inschakelen van een repository moet je `emerge --sync repo_name` uitvoeren om ebuilds te downloaden.
> Meer informatie: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- Toon alle ebuild-repositories geregistreerd op <https://repos.gentoo.org>:

`eselect repository list`

- Toon ingeschakelde repositories:

`eselect repository list -i`

- Schakel een repository uit de lijst in op naam of index van de `list`-opdracht:

`eselect repository enable {{naam|index}}`

- Schakel een niet-geregistreerde repository in:

`eselect repository add {{naam}} {{rsync|git|mercurial|svn|...}} {{sync_uri}}`

- Schakel repositories uit zonder hun inhoud te verwijderen:

`eselect repository disable {{repo1 repo2 ...}}`

- Schakel repositories uit en verwijder hun inhoud:

`eselect repository remove {{repo1 repo2 ...}}`

- Maak een lokale repository aan en schakel deze in:

`eselect repository create {{naam}} {{pad/naar/repo}}`
