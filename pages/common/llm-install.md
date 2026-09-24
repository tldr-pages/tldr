# llm install

> Install Python packages in the same environment as LLM, typically to add plugins.
> More information: <https://llm.datasette.io/en/stable/help.html#llm-install-help>.

- Install a plugin from PyPI:

`llm install {{plugin_name}}`

- Upgrade a plugin to its latest version:

`llm install {{[-U|--upgrade]}} {{plugin_name}}`

- Install a local plugin in editable mode:

`llm install {{[-e|--editable]}} {{path/to/plugin_directory}}`

- Reinstall a plugin even if it is already up to date:

`llm install --force-reinstall {{plugin_name}}`

- Include pre-release versions when installing a plugin:

`llm install --pre {{plugin_name}}`
