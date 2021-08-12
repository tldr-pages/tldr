# pueue parallel

> Setați cantitatea de activități paralele permise.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Setați numărul maxim de activități permise pentru a rula în paralel, în grupul implicit:

`pueue parallel {{max_number_of_parallel_tasks}}`

- Setați numărul maxim de sarcini permise pentru a rula în paralel, într-un anumit grup:

`pueue parallel --group {{group_name}} {{maximum_number_of_parallel_tasks}}`
