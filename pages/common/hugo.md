# hugo

> Hugo is a Fast and Flexible Static Site Generator.

- Create a new hugo site:

`hugo new site {{path/to/site}}`

- Create a new hugo theme (you may also download one from [https://themes.gohugo.io/]()):

`hugo new theme {{theme_name}}`

- Create a new page:

`hugo new {{section_name}}/{{filename}}{{.ext}}`

- Build your site to the `./public/` directory:

`hugo`

- Build your site to a different destination:

`hugo --destination {{path/to/destination}}`

- Build your site, start up a webserver to serve it, and watch for changes:

`hugo server`

- Build and serve content marked as draft:

`hugo server --buildDrafts`
