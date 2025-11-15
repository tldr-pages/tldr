# accelerate

> Una biblioteca que permite ejecutar el mismo código PyTorch en cualquier configuración distribuida.
> Más información: <https://huggingface.co/docs/accelerate/index>.

- Imprime información del entorno:

`accelerate env`

- Crea interactivamente un archivo de configuración:

`accelerate config`

- Imprime el coste estimado en memoria de la GPU al ejecutar un modelo Hugging Face con distintos tipos de datos:

`accelerate estimate-memory {{nombre/modelo}}`

- Prueba un archivo de configuración de Accelerate:

`accelerate test --config_file {{ruta/a/config.yaml}}`

- Ejecuta un modelo en CPU con Accelerate:

`accelerate launch {{ruta/a/script.py}} {{--cpu}}`

- Ejecuta un modelo en multi-GPU con Accelerate, con 2 máquinas:

`accelerate launch {{ruta/a/script.py}} --multi_gpu --num_machines 2`
