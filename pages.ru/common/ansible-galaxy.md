# ansible-galaxy

> Выполнять различные операции с ролями и коллекциями Ansible.
> Больше информации: <https://docs.ansible.com/projects/ansible/latest/cli/ansible-galaxy.html>.

- Вывести список установленных ролей или коллекций:

`ansible-galaxy {{role|collection}} list`

- Найти роль с различными уровнями подробности (`-v` указывается в конце):

`ansible-galaxy role search {{ключевое_слово}} -v{{vvvvv}}`

- Установить или удалить роль(и):

`ansible-galaxy role {{install|remove}} {{имя_роли1 имя_роли2 ...}}`

- Создать новую роль:

`ansible-galaxy role init {{имя_роли}}`

- Получить информацию о роли:

`ansible-galaxy role info {{имя_роли}}`

- Установить или удалить коллекцию(и):

`ansible-galaxy collection {{install|remove}} {{имя_коллекции1 имя_коллекции2 ...}}`

- Показать справку о ролях или коллекциях:

`ansible-galaxy {{role|collection}} {{[-h|--help]}}`
