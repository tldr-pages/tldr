#հերոկու

> Ստեղծեք և կառավարեք Heroku հավելվածները:.
> Լրացուցիչ տեղեկություններ. <https://devcenter.heroku.com/articles/heroku-cli#get-started-with-the-heroku-cli>:.

- Մուտք գործեք ձեր Heroku հաշիվ.:

`heroku login`

- Ստեղծեք Heroku հավելված.:

`heroku create`

- Ցույց տալ տեղեկամատյանները հավելվածի համար.:

`heroku logs --app {{app_name}}`

- Գործարկեք միանվագ գործընթաց դինոյի ներսում (Heroku վիրտուալ մեքենա).:

`heroku run {{process_name}} --app {{app_name}}`

- Թվարկեք dynos (Heroku վիրտուալ մեքենաներ) հավելվածի համար.:

`heroku ps --app {{app_name}}`

- Մշտապես ոչնչացնել հավելվածը.:

`heroku destroy --app {{app_name}}`
