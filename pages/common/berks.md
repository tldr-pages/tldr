# berks

> Chef cookbook dependency manager.
> More information: <https:/https://docs.chef.io/workstation/26.1/tools/berkshelf/#berkshelf-cli>.

- Install cookbook dependencies into a local repo:

`berks install`

- Update a specific cookbook and its dependencies:

`berks update {{cookbook}}`

- Upload a cookbook to the Chef server:

`berks upload {{cookbook}}`

- View the dependencies of a cookbook:

`berks contingent {{cookbook}}`
