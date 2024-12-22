# llm

> Interactúa con modelos grandes de lenguaje (LLMs) a través de APIs y modelos remotos que pueden instalarse y ejecutarse en su máquina.
> Más información: <https://llm.datasette.io/en/stable/help.html>.

- Configura una clave API de OpenAI:

`llm keys set openai`

- Ejecuta un prompt:

`llm "{{Diez nombres divertidos para un pelícano}}"`

- Ejecuta un prompt de [s]istema contra un archivo:

`cat {{ruta/al/archivo.py}} | llm --system "{{Explica este código}}"`

- Instala paquetes de PyPI en el mismo entorno que LLM:

`llm install {{paquete1 paquete2 ...}}`

- Descarga y ejecuta un prompt frente a un [m]odelo:

`llm --model {{orca-mini-3b-gguf2-q4_0}} "{{¿Cuál es la capital de Francia?}}"`

- Crea un prompt de [s]istema y lo [s]alva como una plantilla:

`llm --system '{{Eres una torta de queso sensible}}' --save {{torta_de_queso_sensible}}`

- Establece un chat interactivo con un [m]odelo específico utilizando una plan[t]illa específica:

`llm chat --model {{chatgpt}} --template {{torta_de_queso_sensible}}`
