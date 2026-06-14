# gixy-next

> Վերլուծեք NGINX կազմաձևման ֆայլերը անվտանգության և կատարողականի սխալ կազմաձևումների համար:.
> Լրացուցիչ տեղեկություններ. <https://gixy.io/usage/>:.

- Վերլուծեք `nginx` կոնֆիգուրացիան (կանխադրված ուղին՝ `/etc/nginx/nginx.conf`):

`gixy-next {{path/to/nginx.conf}}`

- Վերլուծեք ստացված կազմաձևման աղբանոցը `stdin`-ի միջոցով (`-`):

`cat {{path/to/nginx-dump.conf}} | gixy-next -`

- Գործարկել միայն հատուկ ստուգումներ (ստորակետերով բաժանված).:

`gixy-next --tests {{http_splitting,ssrf,version_disclosure}} {{path/to/nginx.conf}}`

- Բաց թողնել հատուկ ստուգումները (ստորակետերով բաժանված).:

`gixy-next --skips {{low_keepalive_requests,worker_rlimit_nofile_vs_connections}} {{path/to/nginx.conf}}`

- Զեկուցեք միայն որոշակի ծանրության կամ ավելի բարձր խնդիրների մասին.:

`gixy-next {{-l|-ll|-lll}} {{path/to/nginx.conf}}`

- Արդյունք որպես չգունավոր տեքստ կամ մեքենայաընթեռնելի JSON:

`gixy-next {{[-f|--format]}} {{text|json}} {{path/to/nginx.conf}}`
