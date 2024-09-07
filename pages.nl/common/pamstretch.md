# pamstretch

> Vergroot een PAM afbeelding door te interpoleren tussen pixels.
> Bekijk ook: `pamstretch-gen`, `pamenlarge`, `pamscale`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

- Vergroot een PAM afbeelding met een gehele factor:

`pamstretch {{N}} {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.pam}}`

- Vergroot een PAM afbeelding met de gespecificeerde factoren in de horizontale en verticale richtingen:

`pamstretch -xscale {{XN}} -yscale {{YN}} {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.pam}}`
