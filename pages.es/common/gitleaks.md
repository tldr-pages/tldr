# gitleaks

> Detecta secretos y claves API filtradas en repositorios Git.
> Más información: <https://github.com/gitleaks/gitleaks>.

- Escanea un repositorio remoto:

`gitleaks detect --repo-url {{https://github.com/nombre_usuario/repositorio.git}}`

- Escanea un directorio local:

`gitleaks detect --source {{ruta/al/repositorio}}`

- Envia los resultados del análisis a un archivo JSON:

`gitleaks detect --source {{ruta/al/repositorio}} --report {{ruta/a/informe.json}}`

- Utiliza un archivo de reglas personalizado:

`gitleaks detect --source {{ruta/al/repositorio}} --config-path {{ruta/a/config.toml}}`

- Inicia la búsqueda a partir de una confirmación específica:

`gitleaks detect --source {{ruta/al/repositorio}} --log-opts {{--since=identificador_confirmación}}`

- Escanea cambios no confirmados antes de una confirmación:

`gitleaks protect --staged`

- Muestra una salida detallada que indica qué partes se identificaron como fugas durante el análisis:

`gitleaks protect --staged --verbose`
