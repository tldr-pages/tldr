# checkov

> Checkov es una herramienta de análisis estático de código para Infraestructura como Código (IaC).
> También es una herramienta de análisis de composición de software (SCA) para imágenes y paquetes de código abierto.
> Más información: <https://www.checkov.io/1.Welcome/Quick%20Start.html>.

- Analiza un directorio que contenga IaC (Terraform, Cloudformation, ARM, Ansible, Bicep, Dockerfile, etc):

`checkov --directory {{ruta/al/directorio}}`

- Escanea un archivo IaC, omitiendo bloques de código en la salida:

`checkov --compact --file {{ruta/al/archivo}}`

- Lista todas las comprobaciones de todos los tipos de IaC:

`checkov --list`
