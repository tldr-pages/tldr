# bg

> Reanuda un trabajo suspendido (por ejemplo, usando `<Ctrl z>`) y lo deja ejecutándose en segundo plano.
> Vea también: `jobs`, `fg`, `disown`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-bg>.

- Reanuda el último trabajo suspendido y lo deja ejecutándose en segundo plano:

`bg`

- Reanuda un trabajo específico y lo deja ejecutarse en segundo plano (usa `jobs` para obtener el número de trabajo):

`bg %{{numero_de_trabajo}}`
