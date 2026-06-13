# git request-pull

> Générer une requête demandant au projet en amont d'inclure les modifications dans son arborescence.
> Plus d'informations : <https://git-scm.com/docs/git-request-pull>.

- Produire une requête résumant les changements entre la version v1.1 et le master :

`git request-pull {{v1.1}} {{https://example.com/project}} {{master}}`

- Produire une requête résumant les changements entre la version v1.1 sur la branche master et la branche locale foo :

`git request-pull {{v0.1}} {{https://example.com/project}} {{master:foo}}`
