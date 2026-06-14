# glab ռեպո

> Աշխատեք GitLab պահեստների հետ:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/repo/_index.md>:.

- Ստեղծեք նոր պահոց (եթե պահեստի անունը սահմանված չէ, լռելյայն անունը կլինի ընթացիկ գրացուցակի անունը).:

`glab repo create {{name}}`

- Կլոնավորել պահեստը.:

`glab repo clone {{owner}}/{{repository}}`

- Պատառաքաղել և կլոնավորել պահեստը.:

`glab repo fork {{owner}}/{{repository}} {{[-c|--clone]}}`

- Դիտեք պահեստը լռելյայն վեբ բրաուզերում.:

`glab repo view {{owner}}/{{repository}} {{[-w|--web]}}`

- Որոնեք որոշ պահեստներ GitLab օրինակում.:

`glab repo search {{[-s|--search]}} {{search_string}}`
