# hugo

> Template-based static site generator. Uses modules, components, and themes.
> More information: <https://gohugo.io>.

- Create a new Hugo site:

`hugo new site {{path/to/site}}`

- Create a new Hugo theme (themes may also be downloaded from https://themes.gohugo.io/):

`hugo new theme {{theme_name}}`

- Create a new page:

`hugo new {{section_name}}/{{filename}}`

- Build a site to the `./public/` directory:

`hugo`

- Build a site including pages that are marked as a "draft":

`hugo --buildDrafts`

- Build a site to a given directory:

`hugo --destination {{path/to/destination}}`

- Build a site, start up a webserver to serve it, and automatically reload when pages are edited:

`hugo server`
