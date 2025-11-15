# aws configure

> Gestiona la configuración para la CLI de AWS.
> Más información: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configura AWS CLI interactivamente (crea una nueva configuración o actualiza la predeterminada):

`aws configure`

- Configura un perfil con nombre para la CLI de AWS de forma interactiva (crea un perfil nuevo o actualiza uno existente):

`aws configure --profile {{nombre_del_perfil}}`

- Muestra el valor de una variable de configuración específica:

`aws configure get {{nombre}}`

- Muestra el valor de una variable de configuración en un perfil específico:

`aws configure get {{nombre}} --profile {{nombre_del_perfil}}`

- Establece el valor de una variable de configuración específica:

`aws configure set {{nombre}} {{valor}}`

- Establece el valor de una variable de configuración en un perfil específico:

`aws configure set {{nombre}} {{valor}} --profile {{nombre_del_perfil}}`

- Lista las entradas de configuración:

`aws configure list`

- Lista las entradas de configuración para un perfil específico:

`aws configure list --profile {{nombre_del_perfil}}`
