# uv publish

> Загружать дистрибутивы в индекс.
> Больше информации: <https://docs.astral.sh/uv/reference/cli/#uv-publish>.

- Опубликовать пакеты из каталога `dist/` (поведение по умолчанию):

`uv publish`

- Опубликовать в определённый репозиторий:

`uv publish --publish-url {{https://upload.pypi.org/legacy/}}`

- Опубликовать с определённым именем пользователя и паролем:

`uv publish {{[-u|--username]}} {{имя_пользователя}} {{[-p|--password]}} {{пароль}}`

- Опубликовать с использованием API-токена:

`uv publish {{[-t|--token]}} {{ваш_api_токен}}`

- Опубликовать определённые файлы дистрибутивов:

`uv publish {{путь/к/dist/*.whl}} {{путь/к/dist/*.tar.gz}}`

- Опубликовать на TestPyPI для тестирования:

`uv publish --publish-url https://test.pypi.org/legacy/`
