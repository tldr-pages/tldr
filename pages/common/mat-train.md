# mat train

> Run the full MultiAgentTrainer pipeline: ingest data sources, build a corpus, and run training experiments.
> More information: <https://github.com/sroomberg/MultiAgentTrainer>.

- Run the full pipeline with default settings:

`mat train`

- Limit the number of training experiments:

`mat train --max-experiments {{count}}`

- Write output to a custom directory:

`mat train --output-dir {{path/to/output}}`

- Label the run for identification in `mat watch` and `mat status`:

`mat train --name {{label}}`

- Ingest an extra repository without editing the config (repeatable):

`mat train --repo {{owner/repo}}`

- Use a custom configuration file:

`mat train --config {{path/to/config.yaml}}`
