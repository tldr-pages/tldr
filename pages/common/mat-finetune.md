# mat finetune

> Fine-tune a model on the corpus ingested by MultiAgentTrainer.
> Supports open-source models via HuggingFace/LoRA and managed models via AWS Bedrock.
> More information: <https://github.com/sroomberg/MultiAgentTrainer>.

- Start fine-tuning on the default ingested corpus:

`mat finetune start`

- Fine-tune using a specific corpus file:

`mat finetune start --corpus {{path/to/corpus.txt}}`

- Start a named fine-tuning job:

`mat finetune start --name {{job_name}}`

- List all fine-tuning jobs and their identifiers:

`mat finetune list`

- Check the status of a fine-tuning job:

`mat finetune status {{job_id}}`

- Cancel a running Bedrock fine-tuning job:

`mat finetune cancel {{job_arn}}`
