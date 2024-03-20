# colima

> Contenedores en tiempo de ejecución para macOS y Linux con una configuración mínima.
> Más información: <https://github.com/abiosoft/colima>.

- Inicia el daemon en segundo plano:

`colima start`

- Crea un archivo de configuración y lo usa:

`colima start --edit`

- Inicia y configura containerd (instala `nerdctl` para usar containerd a través de `nerdctl`):

`colima start --runtime containerd`

- Inicia con Kubernetes (se requiere `kubectl`):

`colima start --kubernetes`

- Personaliza el recuento de CPU, memoria RAM y espacio en disco (en GiB):

`colima start --cpu {{número}} --memory {{memoria}} --disk {{espacio_de_almacenamiento}}`

- Usa Docker a través de Colima (se requiere Docker):

`colima start`

- Lista contenedores con su información y estado:

`colima list`

- Muestra estado de tiempo de ejecución:

`colima status`
