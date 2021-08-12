# stripe

> Interacționați cu un cont Stripe.
> Mai multe informaţii: <https://github.com/stripe/stripe-cli>

- Urmați jurnalele de activitate din cont:

`stripe logs tail`

- Ascultați evenimentele, filtrând evenimentele cu numele `charge.a reușit” și redirecționându-le la localhost:3000/evenimente:

`stripe listen --events="{{charge.succeeded}}" --forward-to="{{localhost:3000/events}}"`

- Trimite un eveniment webhook test:

`stripe trigger {{charge.succeeded}}`

- Creaţi un client:

`stripe customers create --email="{{test@example.com}}" --name="{{Jenny Rosen}}"`

- Imprimare la JSON:

`stripe listen --print-json`
