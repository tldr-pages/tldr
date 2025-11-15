# slapt-src

> A utility to automate building of slackbuilds.
> SlackBuild sources need to be configured in the slapt-srcrc file.
> More information: <https://github.com/jaos/slapt-src>.

- Update the list of available slackbuilds and versions:

`slapt-src {{[-u|--update]}}`

- List all available slackbuilds:

`slapt-src {{[-l|--list]}}`

- Fetch, build and install the specified slackbuild(s):

`slapt-src {{[-i|--install]}} {{slackbuild_name}}`

- Locate slackbuilds by their name or description:

`slapt-src {{[-s|--search]}} {{search_term}}`

- Display information about a slackbuild:

`slapt-src {{[-w|--show]}} {{slackbuild_name}}`
