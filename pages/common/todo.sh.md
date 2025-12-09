# todo.sh

> Simple and extensible shell script for managing your `todo.txt` file.
> More information: <https://github.com/todotxt/todo.txt-cli>.

- List every item:

`todo.sh ls`

- Add an item with project and context tags:

`todo.sh add '{{description}} +{{project}} @{{context}}'`

- Mark an item as [do]ne:

`todo.sh do {{item_no}}`

- Remove an item:

`todo.sh rm {{item_no}}`

- Set an item's [pri]ority (A-Z):

`todo.sh pri {{item_no}} {{priority}}`

- Replace an item:

`todo.sh replace {{item_no}} '{{new_description}}'`
