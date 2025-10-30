# emaint

> Perform Portage maintenance tasks.
> More information: <https://wiki.gentoo.org/wiki/Portage#emaint>.

- Synchronize repositories that are set to auto-sync (default for most repositories):

`sudo emaint sync {{[-a|--auto]}}`

- Synchronize a specific repository:

`sudo emaint sync {{[-r|--repo]}} {{repository}}`

- Synchronize all repositories:

`sudo emaint sync --allrepos`

- Clear the Portage resume list:

`sudo emaint cleanresume {{[-f|--fix]}}`

- Clean Portage logs:

`sudo emaint logs {{[-C|--clean]}}`
