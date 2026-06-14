#շերտ

> Փոխազդեք Stripe հաշվի հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.stripe.com/stripe-cli>:.

- Հետևեք հաշվի գործունեության տեղեկամատյաններին.:

`stripe logs tail`

- Լսեք իրադարձությունները՝ զտելով `charge.succeeded` անունով իրադարձությունները և դրանք փոխանցելով localhost:3000/events:

`stripe listen --events="{{charge.succeeded}}" --forward-to="{{localhost:3000/events}}"`

- Ուղարկեք փորձնական webhook իրադարձություն.:

`stripe trigger {{charge.succeeded}}`

- Ստեղծեք հաճախորդ.:

`stripe customers create --email="{{test@example.com}}" --name="{{Jenny Rosen}}"`

- Տպել JSON-ում.:

`stripe listen --print-json`
