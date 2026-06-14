#դոկկու

> Docker-ով աշխատող մինի-Heroku (PaaS):.
> Հեշտությամբ տեղադրեք բազմաթիվ հավելվածներ ձեր սերվերի վրա տարբեր լեզուներով՝ օգտագործելով մեկ `git-push` հրամանը:.
> Լրացուցիչ տեղեկություններ. <https://dokku.com/docs/deployment/application-deployment/>:.

- Ցուցակեք գործող հավելվածները.:

`dokku apps`

- Ստեղծեք հավելված.:

`dokku apps:create {{app_name}}`

- Հեռացնել հավելվածը.:

`dokku apps:destroy {{app_name}}`

- Տեղադրեք plugin:

`dokku plugin:install {{full_repo_url}}`

- Կապել տվյալների բազան հավելվածին.:

`dokku {{db}}:link {{db_name}} {{app_name}}`
