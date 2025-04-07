# recon-ng

> Automated reconnaissance and information gathering tool.
> After installation use `recon-ng` to begin using this tool.
> More information: <https://github.com/lanmaster53/recon-ng/wiki>.

- Create a workspace:

`workspaces create {{workspace_name}}`

- Search marketplace for modules used to accomplish different reconnaissance tasks:

`marketplace search`

- Install all available modules (Some may need api keys to completely function):

`marketplace install all`

- Load the profiler module. This module is used to scan the web for profiles matching the target, scrape them, and store them:

`modules load profiler`

- Used to insert the target's username. After entering this command, enter the desired username of your search and leave the rest of the options blank:

`db insert profiles`

- To run the current module:

`run`
