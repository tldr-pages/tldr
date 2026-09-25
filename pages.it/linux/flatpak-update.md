# flatpak update

> Aggiorna applicazioni flatpak e runtime.
> Maggiori informazioni: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-update>.

- Aggiorna tutte le applicazioni e i runtime installati (usa `-y` per confermare automaticamente tutti i prompt):

`flatpak update`

- Aggiorna solo un'app specifica:

`flatpak update {{com.example.app}}`

- Aggiorna/Ripristina a un commit specifico (vedi anche flatpak remote-info e flatpak mask):

`flatpak update --commit {{COMMIT}} {{com.example.app}}`
