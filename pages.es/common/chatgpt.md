# chatgpt

> Shell script para usar ChatGPT de OpenAI y DALL-E desde la terminal.
> Más información: <https://github.com/0xacx/chatGPT-shell-cli>.

- Comienza en modo chat:

`chatgpt`

- Da un [p]rompt para responder:

`chatgpt --prompt "{{¿Cuál es la expresión regular para emparejar una dirección de correo electrónico?}}"`

- Inicia en modo chat utilizando un [m]odelo específico (por defecto es `gpt-3.5-turbo`):

`chatgpt --model {{gpt-4}}`

- Inicia en modo chat con un prompt [i]nicial:

`chatgpt --init-prompt "{{Tú eres Rick, de Rick y Morty. Responde a las preguntas usando su amaneramiento e incluye chistes insultantes.}}"`

- Envía el resultado de un comando a ChatGPT como un prompt:

`echo "{{¿Cómo ver los procesos en ejecución en Ubuntu?}}" | chatgpt`

- Genera una imagen utilizando DALL-E:

`chatgpt --prompt "{{image: Un gato blanco}}"`
