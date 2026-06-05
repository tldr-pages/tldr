# gh attestation

> Descarga y verifica las certificaciones de los artefactos para garantizar su integridad y procedencia.
> Más información: <https://cli.github.com/manual/gh_attestation>.

- Descarga certificaciones para un archivo local asociado a un repositorio específico:

`gh {{[at|attestation]}} download {{ruta/al/artefacto.bin}} {{[-R|--repo]}} {{propietario}}/{{repositorio}}`

- Descarga certificaciones para una imagen de contenedor OCI asociada a una organización:

`gh {{[at|attestation]}} download oci://{{imagen_uri}} {{[-o|--owner]}} {{nombre_de_la_organización}}`

- Verifica un artefacto local en línea con respecto a las certificaciones de un repositorio específico:

`gh {{[at|attestation]}} verify {{ruta/al/artefacto.bin}} {{[-R|--repo]}} {{propietario}}/{{repositorio}}`

- Verifica un artefacto, requiriendo que haya sido firmado por un flujo de trabajo reutilizable específico para una mayor seguridad:

`gh {{[at|attestation]}} verify {{ruta/al/artefacto.bin}} {{[-o|--owner]}} {{nombre_de_la_organización}} --signer-workflow {{propietario}}/{{repositorio}}/{{ruta/a/workflow.yml}}`

- Verifica un artefacto y generar los resultados detallados de la verificación en formato JSON para su uso en motores de políticas:

`gh {{[at|attestation]}} verify {{ruta/al/artefacto.bin}} {{[-o|--owner]}} {{nombre_de_la_organización}} --format json`

- Realiza una verificación totalmente sin conexión utilizando un paquete descargado y un archivo raíz de confianza personalizado:

`gh {{[at|attestation]}} verify {{ruta/al/artefacto.bin}} {{[-b|--bundle]}} {{ruta/a/bundle.jsonl}} --custom-trusted-root {{ruta/a/trusted_root.jsonl}}`

- Guarda la raíz de confianza de los certificados de firma en un archivo para la verificación sin conexión:

`gh {{[at|attestation]}} trusted-root > {{ruta/a/trusted_root.jsonl}}`
