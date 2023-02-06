# git request-pull

> Létrehoz egy kérést, amely arra kéri az upstream projektet, hogy a változtatásokat a saját fájába húzza be. További információ: <https://git-scm.com/docs/git-request-pull>.

- Készítsen egy kérést, amely összefoglalja a v1.1-es kiadás és egy megadott ág közötti változásokat:

`git request-pull {{v1.1}} {{https://example.com/project}} {{branch_name}}`

- A `foo` ágon lévő v0.1-es kiadás és a helyi `bar` ág közötti változásokat összefoglaló kérés készítése:

`git request-pull {{v0.1}} {{https://example.com/project}} {{foo:bar}}`
