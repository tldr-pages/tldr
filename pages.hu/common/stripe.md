# stripe

> Interakció egy Stripe-fiókkal. További információ: <https://github.com/stripe/stripe-cli>.

- Kövesse a fiókon végzett tevékenységek naplózását:

`stripe logs tail`

- Események figyelése, a `charge.succeeded` nevű események szűrése és továbbítása a localhost:3000/events címre:

`stripe listen --events="{{charge.succeeded}}" --forward-to="{{localhost:3000/events}}"`

- Teszt webhook esemény küldése:

`stripe trigger {{charge.succeeded}}`

- Ügyfél létrehozása:

`stripe customers create --email="{{test@example.com}}" --name="{{Jenny Rosen}}"`

- JSON-ba nyomtatás:

`stripe listen --print-json`
