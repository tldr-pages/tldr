# devenv

> Entornos de desarrollo rápidos, declarativos, reproducibles y componibles utilizando Nix.
> Más información: <https://devenv.sh>.

- Inicializa el entorno:

`devenv init`

- Entra en el entorno de desarrollo con hermeticidad relajada (estado de ser hermético):

`devenv shell --impure`

- Obtén información detallada sobre el entorno actual:

`devenv info --verbose`

- Inicia procesos con `devenv`:

`devenv up --config /{{archivo}}/{{ruta}}/`

- Limpia las variables de entorno y vuelve a entrar en el intérprete de comandos en el modo sin conexión:

`devenv --clean --offline`

- Borra las generaciones anteriores del intérprete de comandos:

`devenv gc`
