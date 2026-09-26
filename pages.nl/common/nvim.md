# nvim

> Neovim, een programmeurs tekstbewerker gebaseerd op Vim, welke verschillende modi aanbiedt voor verschillende soorten tekstmanipulatie.
> Op `<i>` drukken in de normale modus, gaat naar de invoermodus. `<Esc>` of `<Ctrl c>` gaat terug naar de normale modus, die geen reguliere tekstinvoer accepteert.
> Zie ook: `vim`, `vimtutor`, `vimdiff`.
> Meer informatie: <https://neovim.io/>.

- Open een bestand:

`nvim {{pad/naar/bestand}}`

- Ga naar de modus om tekst aan te passen (insert mode):

`<Esc><i>`

- Kopieer ("yank") of knip ("delete") de huidige regel (plak het met `<p>`):

`<Esc>{{<y><y>|<d><d>}}`

- Ga naar de normale modus en maak de laatste operatie ongedaan:

`<Esc><u>`

- Zoek naar een patroon in het bestand (druk op `<n>`/`<N>` om naar de volgende/vorige overeenkomst te gaan):

`<Esc></>{{zoek_patroon}}<Enter>`

- Voer een reguliere expressie vervanging uit in het volledige bestand:

`<Esc><:>%s/{{reguliere_expressie}}/{{vervanging}}/g<Enter>`

- Ga naar de normale modus, sla (write) het bestand op en sluit af:

`{{<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>}}`

- Sluit af zonder op te slaan:

`<Esc><:>q!<Enter>`
