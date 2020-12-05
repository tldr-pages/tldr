# slapt-src

> A utility to automate building of slackbuilds.
> SlackBuild sources need to be configured in the slapt-srcrc file.

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
