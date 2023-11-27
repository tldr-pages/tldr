# chatgpt

> Shell script to use OpenAI's ChatGPT and DALL-E from the terminal. 
> More information <https://github.com/0xacx/chatGPT-shell-cli>

- Start ChatGPT in chat mode

`chatgpt`

- Give ChatGPT a prompt to answer to:

`chatgpt -p "What is the regex to match an email address?"`

- Start ChatGPT in chat mode using a specific model:

`chatgpt -m gpt-4 `

- Start ChatGPT in chat mode with an initial prompt:

`chatgpt -i "You are Rick, from Rick and Morty. Respond to questions using his mannerism and include insulting jokes."`

- Pipe the result of a command to ChatGPT as a prompt:

`echo "How to view running processes on Ubuntu?" | chatgpt`

- Generate an image using DALL-E

`chatgpt -p "image: A white cat"`
