# git commit-graph

> Записує та перевіряє файл графіку комітів Git.
> Більше інформації: <https://git-scm.com/docs/git-commit-graph>.

- Записує файл графіку комітів для спакованих комітів у локальній директорії `.git`:

`git commit-graph write`

- Записує файл графіку комітів, що містить набір усіх досяжних комітів:

`git show-ref --hash | git commit-graph write --stdin-commits`

- Записує файл графіку комітів, що містить усі коміти у поточному файлі графіку комітів разом з тими, до яких можна отримати доступ з `HEAD`:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`
