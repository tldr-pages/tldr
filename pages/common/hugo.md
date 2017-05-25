# hugo

> Hugo is a fast and flexible static site generator.

- Create a new Hugo site:

`hugo new site {{path/to/site}}`

- Create a new Hugo theme (you may also download one from https://themes.gohugo.io/):

`hugo new theme {{theme_name}}`

- Create a new page:

`hugo new {{section_name}}/{{filename}}`

- Build your site to the `./public/` directory:

`hugo`

- Build your site including pages that are marked as a "draft":

`hugo --buildDrafts`

- Build your site to a given directory:

`hugo --destination {{path/to/destination}}`

- Build your site, start up a webserver to serve it, and automatically reload when pages are edited:

`hugo server`
