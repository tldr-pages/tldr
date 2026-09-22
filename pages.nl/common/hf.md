# hf

> Interactie met Hugging Face Hub.
> Log in, beheer de lokale cache, download of upload bestanden.
> Meer informatie: <https://huggingface.co/docs/huggingface_hub/guides/cli>.

- Log in bij Hugging Face Hub:

`hf auth login`

- Toon de naam van de ingelogde gebruiker:

`hf auth whoami`

- Log uit:

`hf auth logout`

- Print informatie over de omgeving:

`hf env`

- Download bestanden uit een repository en print het pad (laat bestandsnamen weg om de volledige repository te downloaden):

`hf download --repo-type {{repo_type}} {{repo_id}} {{bestandsnaam1 bestandsnaam2 ...}}`

- Upload een volledige map of een bestand naar Hugging Face:

`hf upload --repo-type {{repo_type}} {{repo_id}} {{pad/naar/lokaal_bestand_of_map}} {{pad/naar/repo_bestand_of_map}}`

- Scan de cache om gedownloade repositories en hun schijfgebruik te bekijken:

`hf cache ls`
