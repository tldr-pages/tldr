# mat

> Collect data from multiple sources, run autonomous LLM training experiments, and fine-tune models.
> Companion to `agent-tester`. See also: `mat-train`, `mat-finetune`.
> More information: <https://github.com/sroomberg/MultiAgentTrainer>.

- List configured data sources:

`mat sources`

- Ingest data sources and build a corpus without training:

`mat ingest`

- Run the full pipeline (ingest → corpus → train):

`mat train`

- Watch multiple training runs in real-time:

`mat watch`

- Show historical training run results:

`mat status`

- Fine-tune a model on the ingested corpus:

`mat finetune start`
