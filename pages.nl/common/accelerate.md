# Accelerate

> Accelerate is een bibliotheek waarmee dezelfde PyTorch-code kan worden uitgevoerd op elke gedistribueerde configuratie.
> Meer informatie: <https://huggingface.co/docs/accelerate/index>.

- Toon informatie over de omgeving:

`accelerate env`

- Maak interactief een configuratiebestand:

`accelerate config`

- Druk de geschatte GPU-geheugenkosten af van het uitvoeren van een Hugging Face model met verschillende gegevenstypen:

`accelerate estimate-memory {{name/model}}`

- Test een Accelerate configuratiebestand:

`accelerate test --config_file {{pad/naar/config.yaml}}`

- Voer een model uit op CPU met Accelerate:

`accelerate launch {{pad/naar/script.py}} {{--cpu}}`

- Voer een model uit op multi-GPU met Accelerate, met 2 machines:

`accelerate launch {{pad/naar/script.py}} --multi_gpu --num_machines {{2}}`
