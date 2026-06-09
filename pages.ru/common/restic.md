# restic

> Быстрая программа для резервного копирования с шифрованием.
> Подробнее: <https://restic.readthedocs.io/en/stable/manual_rest.html#usage-help>.

- Создать репозиторий для резервных копий в указанном локальном каталоге:

`restic init {{[-r|--repo]}} {{path/to/repository}}`

- Создать резервную копию каталога в репозитории:

`restic {{[-r|--repo]}} {{path/to/repository}} backup {{path/to/directory}}`

- Показать снимки резервных копий хранящиеся в репозитории:

`restic {{[-r|--repo]}} {{path/to/repository}} snapshots`

- Восстановить конкретный снимок резервной копии в целевой каталог:

`restic {{[-r|--repo]}} {{path/to/repository}} restore {{latest|snapshot_id}} --target {{path/to/target}}`

- Восстановить определённый путь из конкретного снимка в целевой каталог:

`restic {{[-r|--repo]}} {{path/to/repository}} restore {{snapshot_id}} --target {{path/to/target}} --include {{path/to/restore}}`

- Очистить репозиторий, оставив только самый свежий снимок для каждой уникальной резервной копии:

`restic forget --keep-last 1 --prune`
