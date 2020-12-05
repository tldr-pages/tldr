# slapt-src

> a utility to make querying, retrieving, and building slackbuilds as
> easy as working with binary packages with slapt-src.

- Update the list of available slackbuilds and versions:

`slapt-src --update`

- List all available slackbuilds:

`slapt-src --list`

- Fetch, build and install the specified slackbuild(s):

`slapt-src --install {{slackbuild_name}}`

- Locate slackbuilds of interest by their name or description:

`slapt-src --search {{search_term}}`

- Show information about a slackbuild:

`slapt-src --show {{slackbuild_name}}`
