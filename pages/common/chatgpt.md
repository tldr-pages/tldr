# chatgpt

> Shell script to use OpenAI's ChatGPT and DALL-E from the terminal.
> More information: <https://github.com/0xacx/chatGPT-shell-cli>.

- Start in chat mode:

`chatgpt`

- Give a prompt to answer to:

`chatgpt {{[-p|--prompt]}} "{{What is the regex to match an email address?}}"`

- Start in chat mode using a specific model (default is `gpt-3.5-turbo`):

`chatgpt {{[-m|--model]}} {{gpt-4}}`

- Start in chat mode with an initial prompt:

`chatgpt {{[-i|--init-prompt]}} "{{You are Rick, from Rick and Morty. Respond to questions using his mannerism and include insulting jokes.}}"`

- Pipe the result of a command to `chatgpt` as a prompt:

`echo "{{How to view running processes on Ubuntu?}}" | chatgpt`

- Generate an image using DALL-E:

`chatgpt {{[-p|--prompt]}} "{{image: A white cat}}"`
