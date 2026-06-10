#թեյ

> Փոխազդել Gitea սերվերների հետ:.
> Լրացուցիչ տեղեկություններ. <https://gitea.com/gitea/tea>:.

- Մուտք գործեք Gitea սերվեր.:

`tea login add --name "{{name}}" --url "{{url}}" --token "{{token}}"`

- Ցուցադրել բոլոր պահեստները.:

`tea repos ls`

- Ցուցադրել խնդիրների ցանկը.:

`tea issues ls`

- Ցուցադրել խնդիրների ցանկը կոնկրետ պահեստի համար.:

`tea issues ls --repo "{{repository}}"`

- Ստեղծեք նոր թողարկում.:

`tea issues create --title "{{title}}" --body "{{body}}"`

- Ցուցադրել բաց ձգման հարցումների ցանկը.:

`tea pulls ls`

- Բացեք ընթացիկ պահոցը զննարկիչում.:

`tea open`
