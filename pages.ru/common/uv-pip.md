# uv pip

> Предоставлять pip-подобные команды для установки, удаления и управления пакетами.
> Больше информации: <https://docs.astral.sh/uv/reference/cli/#uv-pip>.

- Установить пакет:

`uv pip install {{пакет}}`

- Установить пакеты из файла зависимостей:

`uv pip install {{[-r|--requirements]}} {{requirements.txt}}`

- Установить пакет определённой версии:

`uv pip install {{пакет==1.2.3}}`

- Удалить пакет:

`uv pip uninstall {{пакет}}`

- Зафиксировать зависимости из `pyproject.toml` в `requirements.txt`:

`uv pip compile pyproject.toml {{[-o|--output-file]}} requirements.txt`

- Вывести список установленных пакетов:

`uv pip list`

- Показать информацию об установленном пакете:

`uv pip show {{пакет}}`

- Синхронизировать окружение с файлом зависимостей (установить/удалить для точного соответствия):

`uv pip sync {{requirements.txt}}`
