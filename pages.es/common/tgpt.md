# tgpt

> Habla con un chatbot de IA sin necesidad de claves API.
> Proveedores disponibles: `openai`, `opengpts`, `koboldai`, `phind`, `llama2`, `blackboxai`.
> Más información: <https://github.com/aandrew-me/tgpt>.

- Chatea con el proveedor por defecto (GPT-3.5-turbo):

`tgpt "{{prompt}}"`

- Inicia el modo interactivo [m]ultilínea:

`tgpt --multiline`

- Genera [i]mágenes y las guarda en el directorio actual:

`tgpt --image "{{prompt}}"`

- Genera [c]ódigo con el proveedor por defecto (GPT-3.5-turbo):

`tgpt --code "{{prompt}}"`

- Chatea con un proveedor específico silenciosamente (sin animaciones):

`tgpt --provider {{openai|opengpts|koboldai|phind|llama2|blackboxai}} --quiet --whole "{{prompt}}"`

- Genera y ejecuta comandos de intérprete utilizando un proveedor específico (con confirmación):

`tgpt --provider {{llama2}} --shell "{{prompt}}"`

- Pregunta con una clave de API, modelo, longitud máxima de respuesta, temperatura y `top_p` (necesario cuando se utiliza el proveedor `openai`):

`tgpt --provider openai --key "{{api_key}}" --model "{{gpt-3.5-turbo}}" --max-length {{10}} --temperature {{0.7}} --top_p {{0.9}} "{{prompt}}"`

- Alimenta un archivo como pre-entrada adicional:

`tgpt --provider {{blackboxai}} "{{prompt}}" < {{ruta/al/archivo}}`
