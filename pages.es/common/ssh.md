# ssh

> Secure Shell es un protocolo para conectarse de forma segura a sistemas remotos.
> Puede usarse para iniciar sesión o ejecutar comandos en un servidor remoto.
> Más información: <https://man.openbsd.org/ssh>.

- Conecta a un servidor remoto:

`ssh {{usuario}}@{{host_remoto}}`

- Conecta a un servidor remoto con una [i]dentidad específica (clave privada):

`ssh -i {{ruta/al/archivo_clave}} {{usuario}}@{{host_remoto}}`

- Conecta a un servidor con IP `10.0.0.1` y usando un [p]uerto específico:

`ssh {{usuario}}@10.0.0.1 -p {{2222}}`

- Ejecuta un comando en un servidor remoto con asignación de [t]ty para interacción:

`ssh {{usuario}}@{{host_remoto}} -t {{comando}} {{argumentos_del_comando}}`

- Túnel SSH: reenvío de puerto [D]inámico (proxy SOCKS en `localhost:1080`):

`ssh -D {{1080}} {{usuario}}@{{host_remoto}}`

- Túnel SSH: reenvía un puerto específico (`localhost:9999` a `example.org:80`) desactivando la asignación de pseudo-[T]ty y la ejecució[N] de comandos remotos:

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{usuario}}@{{host_remoto}}`

- SSH [J]umping: conecta a través de un jumphost a un servidor remoto (se pueden especificar múltiples saltos separados por comas):

`ssh -J {{usuario}}@{{jump_host}} {{usuario}}@{{host_remoto}}`

- Cierra una sesión colgada:

`<Intro><~><.>`
