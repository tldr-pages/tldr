# ansible-inventory

> Отображать или выгружать инвентарь Ansible.
> Смотрите также: `ansible`.
> Больше информации: <https://docs.ansible.com/projects/ansible/latest/cli/ansible-inventory.html>.

- Показать инвентарь по умолчанию:

`ansible-inventory --list`

- Показать пользовательский инвентарь:

`ansible-inventory --list {{[-i|--inventory-file]}} {{путь/к/файлу_или_скрипту_или_каталогу}}`

- Показать инвентарь по умолчанию в формате YAML:

`ansible-inventory --list {{[-y|--yaml]}}`

- Выгрузить инвентарь по умолчанию в файл:

`ansible-inventory --list --output {{путь/к/файлу}}`
