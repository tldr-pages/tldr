# flyctl

> Գործիք flyctl.io-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/superfly/flyctl>:.

- Մուտք գործեք Fly հաշիվ.:

`flyctl auth login`

- Գործարկեք հավելված որոշակի Dockerfile-ից (կանխադրված ուղին ընթացիկ աշխատանքային գրացուցակն է).:

`flyctl launch --dockerfile {{path/to/dockerfile}}`

- Բացեք ընթացիկ տեղակայված հավելվածը լռելյայն վեբ դիտարկիչում.:

`flyctl open`

- Տեղադրեք Fly հավելվածները կոնկրետ Dockerfile-ից.:

`flyctl deploy --dockerfile {{path/to/dockerfile}}`

- Բացեք Fly Web UI-ն ընթացիկ հավելվածի համար վեբ բրաուզերում.:

`flyctl dashboard`

- Թվարկեք բոլոր հավելվածները մուտք գործած Fly հաշվի մեջ.:

`flyctl apps list`

- Դիտեք կոնկրետ գործող հավելվածի կարգավիճակը.:

`flyctl status --app {{app_name}}`

- Ցուցադրման տարբերակը:

`flyctl version`
