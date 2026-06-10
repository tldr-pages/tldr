# gixy

> Վերլուծել `nginx` կազմաձևման ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/dvershinin/gixy#usage>:.

- Վերլուծեք `nginx` կոնֆիգուրացիան (կանխադրված ուղի՝ `/etc/nginx/nginx.conf`):

`gixy`

- Վերլուծեք `nginx` կոնֆիգուրացիան, բայց բաց թողեք կոնկրետ թեստերը.:

`gixy --skips {{http_splitting}}`

- Վերլուծեք `nginx` կոնֆիգուրացիան՝ հատուկ խստության մակարդակով.:

`gixy {{-l|-ll|-lll}}`

- Վերլուծեք `nginx` կազմաձևման ֆայլերը կոնկրետ ճանապարհին.:

`gixy {{path/to/configuration_file_1 path/to/configuration_file_2 ...}}`
