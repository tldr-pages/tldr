# dvc տարբերություն

> Ցուցադրել փոփոխությունները DVC-ով հետևված ֆայլերում և տեղեկագրքերում:.
> Լրացուցիչ տեղեկություններ. <https://doc.dvc.org/command-reference/diff>:.

- Համեմատեք DVC հետագծված ֆայլերը Git-ի տարբեր ստորաբաժանումներից, պիտակներից և ճյուղերից ընթացիկ աշխատանքային տարածքից.:

`dvc diff {{commit_hash/tag/branch}}`

- Համեմատեք DVC-ի հետագծված ֆայլերի փոփոխությունները 1 Git commit-ից մյուսի հետ.:

`dvc diff {{revision1}} {{revision2}}`

- Համեմատեք DVC հետագծված ֆայլերը՝ դրանց վերջին հեշի հետ միասին.:

`dvc diff --show-hash {{commit}}`

- Համեմատեք DVC հետևված ֆայլերը՝ ցուցադրելով ելքը որպես JSON.:

`dvc diff --show-json --show-hash {{commit}}`

- Համեմատեք DVC հետևված ֆայլերը՝ ցուցադրելով ելքը որպես Markdown.:

`dvc diff --show-md --show-hash {{commit}}`
