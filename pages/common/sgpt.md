# sgpt

> Command-line productivity tool powered by OpenAI's GPT models.
> More information: <https://github.com/TheR1D/shell_gpt#readme>.

- Use it as a search engine, asking for the mass of the sun:

`sgpt "{{mass of the sun}}"`

- Execute Shell commands, and apply `chmod 444` to all files in the current directory:

`sgpt --shell "{{make all files in current directory read only}}"`

- Generate code, solving classic fizz buzz problem:

`sgpt --code "{{solve fizz buzz problem using Python}}"`

- Start a chat session with a unique session name:

`sgpt --chat {{session_name}} "{{please remember my favorite number: 4}}"`

- Start a `REPL` (Read–eval–print loop) session:

`sgpt --repl {{command}}`

- Display help:

`sgpt --help`
