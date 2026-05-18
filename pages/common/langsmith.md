# langsmith

> Command-line interface for LangSmith, a platform for debugging and monitoring LLM applications.
> More information: <https://docs.smith.langchain.com/how_to_guides/setup/cli>.

- Log in to LangSmith:

`langsmith login`

- Log out of LangSmith:

`langsmith logout`

- Display the current LangSmith configuration:

`langsmith whoami`

- Create a new LangSmith dataset from a CSV file:

`langsmith datasets create --name {{dataset_name}} --file {{path/to/file.csv}}`

- Run a test suite against a dataset:

`langsmith test run --dataset {{dataset_name}}`
