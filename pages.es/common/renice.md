# renice

> Modifica la prioridad/niceness de los procesos en ejecución.
> Los valores de niceness van de -20 (más favorable al proceso) a 19 (menos favorable al proceso).
> Vea también: `nice`.
> Más información: <https://manned.org/renice.1p>.

- Aumenta/disminuye la prioridad del [p]roceso:

`renice -n {{3}} -p {{pid}}`

- Aumenta/disminuye la prioridad de todos los procesos de un [u]suario:

`renice -n {{-4}} -u {{uid|usuario}}`

- Aumenta/disminuye la prioridad de todos los procesos que pertenecen a un [g]rupo:

`renice -n {{5}} -g {{grupo_de_procesos}}`
