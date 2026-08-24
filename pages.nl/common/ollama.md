# ollama

> Een groot taalmodel-runner.
> Voor een lijst van beschikbare modellen, zie <https://ollama.com/library>.
> Meer informatie: <https://docs.ollama.com/cli>.

- Start de daemon die vereist is om andere commando's uit te voeren:

`ollama serve`

- Voer een model uit en praat ermee:

`ollama run {{model}}`

- Voer een model uit met één prompt en zet nadenken uit:

`ollama run {{model}} --think=false "{{prompt}}"`

- Toon gedownloade modellen:

`ollama {{[ls|list]}}`

- Pull een specifiek model:

`ollama pull {{model}}`

- Toon actieve modellen:

`ollama ps`

- Verwijder een model:

`ollama rm {{model}}`

- Maak een model van een `Modelfile`:

`ollama create {{nieuwe_model_naam}} {{[-f|--file]}} {{pad/naar/Modelfile}}`
