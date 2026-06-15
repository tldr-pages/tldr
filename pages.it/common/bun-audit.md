# bun audit

> Controlla i pacchetti installati per vulnerabilità di sicurezza conosciute.
> Maggiori informazioni: <https://bun.com/docs/pm/cli/audit>.

- Controlla tutte le dipendenze di un progetto con un file `bun.lock`:

`bun audit`

- Mostra solo le vulnerabilità con gravità pari o superiore al livello specificato:

`bun audit --audit-level {{low|moderate|high|critical}}`

- Controlla solo le dipendenze di produzione:

`bun audit --prod`

- Ignora un CVE specifico:

`bun audit --ignore {{CVE-XXXX-YYYY}}`

- Stampa il report JSON grezzo:

`bun audit --json`
