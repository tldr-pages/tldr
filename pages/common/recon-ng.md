# recon-ng

> Automated reconnaissance and information gathering tool.
> More information: <https://github.com/lanmaster53/recon-ng/wiki>.

- Start the tool:

`recon-ng`

- Create a workspace:

`workspaces create {{workspace_name}}`

- Search the marketplace for modules used to accomplish different reconnaissance tasks:

`marketplace search`

- Install all available modules (some may need API keys to function completely):

`marketplace install all`

- Load the profiler module. It is used to scan the web for profiles matching the target, scrape them, and store them:

`modules load profiler`

- Insert the target's username. After entering this command, enter the desired username of the search and leave the rest of the options blank:

`db insert profiles`

- Run the current module:

`run`
