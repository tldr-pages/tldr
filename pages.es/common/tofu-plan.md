# tofu plan

> Genera y muestra los planes de ejecución de OpenTofu.
> Más información: <https://opentofu.org/docs/cli/commands/plan/>.

- Genera y muestra el plan de ejecución en el directorio actual:

`tofu plan`

- Muestra un plan para destruir todos los objetos remotos que existen actualmente:

`tofu plan -destroy`

- Muestra un plan para actualizar el estado de Tofu y los valores de salida:

`tofu plan -refresh-only`

- Especifica valores para las variables de entrada:

`tofu plan -var '{{nombre1}}={{valor1}}' -var '{{nombre2}}={{valor2}}'`

- Centra la atención de Tofu solo en un subconjunto de recursos:

`tofu plan -target {{tipo_recurso.nombre_recurso[índice instancia]}}`

- Obtiene un plan en formato JSON:

`tofu plan -json`

- Escribe un plan en un archivo específico:

`tofu plan -no-color > {{ruta/al/archivo}}`
