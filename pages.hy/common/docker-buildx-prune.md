# docker buildx սալորաչիր

> Հեռացրեք կառուցման քեշը:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/buildx/prune/>:.

- Հեռացրեք կառուցման քեշը ներկայումս ակտիվ շինարարի համար.:

`docker buildx prune`

- Հեռացրեք քեշի գրառումները հատուկ ֆիլտրի հիման վրա.:

`docker buildx prune --filter "{{type=source.local}}"`

- Հեռացրեք ամենաքիչ օգտագործված քեշի գրառումները, քանի դեռ քեշի չափը որոշակի սահմանից ցածր է.:

`docker buildx prune --max-used-space {{128mb}}`

- Հեռացրեք ամենաքիչ օգտագործված քեշի գրառումները, քանի դեռ որոշակի քանակությամբ ազատ սկավառակի տարածություն է հասանելի.:

`docker buildx prune --reserved-space {{2gb}}`
