# todo

> Um gerenciador de tarefas simples, de interface de linha de comando e em conformidade com os padrões.
> Mais informações: <https://todoman.readthedocs.io/en/stable/man.html>.

- Lista tarefas iniciáveis:

`todo list --startable`

- Adiciona uma nova tarefa à lista de trabalho:

`todo new {{coisas_para_fazer}} --list {{trabalho}}`

- Adiciona um local para uma tarefa com um ID provido:

`todo edit --location {{nome_local}} {{id_tarefa}}`

- Mostra detalhes sobre uma tarefa:

`todo show {{id_tarefa}}`

- Marca tarefas com os IDs especificados como concluídas:

`todo done {{id_tarefa1 id_tarefa2 ...}}`

- Exclui uma tarefa:

`todo delete {{task_id}}`

- Exclui tarefas concluídas e redefine os IDs das tarefas restantes:

`todo flush`
