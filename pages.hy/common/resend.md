# նորից ուղարկել

> Ուղարկեք և կառավարեք նամակներ հրամանի տողից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/resend/resend-cli#commands>:.

- Մուտք գործեք նորից ուղարկել (բացում է բրաուզերը նույնականացման համար).:

`resend login`

- Մուտք գործեք ուղղակիորեն API բանալիով (CI/գործակալների համար).:

`resend login --key {{re_xxxxxxxxx}}`

- Ուղարկել էլ.:

`resend emails send --from {{email@example.com}} --to {{recipient@example.com}} --subject "{{subject}}" --text "{{message}}"`

- Ստեղծեք ձևանմուշ.:

`resend templates create --name "{{Welcome}}" --subject "{{subject}}" --html "{{<h1>Hello</h1>}}"`

- Ուղարկեք նամակ՝ օգտագործելով ձևանմուշ.:

`resend emails send --to {{recipient@example.com}} --template {{template_id}}`

- Ցուցակեք հաստատված տիրույթները.:

`resend domains {{[ls|list]}}`

- Ցույց տալ վավերացման ընթացիկ կարգավիճակը.:

`resend whoami`

- Ստուգեք CLI տարբերակը, API բանալին և տիրույթի կարգավիճակը.:

`resend doctor`
