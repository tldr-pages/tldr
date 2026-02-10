# copilot

- Communiceer met GitHub Copilot.
- Meer informatie: <https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli>.

- Start de interactieve modus:

`copilot`

- Sta alle bestandswijzigingen toe:

`copilot --allow-tool write`

- Hervat de recenste sessie:

`copilot --continue`

- Hervat een eerdere sessie met behulp van een sessiekiezer:

`copilot --resume`

- Gebruik een specifiek model:

`copilot --model "{{gpt-5}}"`

- Sta alle Git-commando's toe, behalve `git push`:

`copilot --allow-tool 'shell(git:*)' --deny-tool 'shell(git push)'`

- Voer een prompt direct uit zonder interactieve modus, terwijl `copilot` alle commando's mag uitvoeren:

`copilot {{[-p|--prompt]}} "{{Haal de bug uit main.js}}" --allow-all-tools`
