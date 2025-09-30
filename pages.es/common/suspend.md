# suspend

> Suspende la ejecución del intérprete de comandos actual.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-suspend>.

- Suspende el intérprete de comandos actual (útil para cuando está con intérpretes de comandos anidados como `su`):

`{{bash}} <Intro> suspend`

- Ejecuta en un terminal separado para continuar desde la suspensión si `suspend` fue usado en un intérprete de comandos no anidado:

`pkill -CONT bash`

- Fuerza la suspensión, incluso si esto bloquea el sistema:

`suspend -f`
