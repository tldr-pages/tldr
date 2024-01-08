# perlbrew

> Manage perl installations in the home directory.
> See also: `asdf`.
> More information: <https://github.com/gugod/App-perlbrew>.

- Initialize a perlbrew environment:

`perlbrew init`

- List available perl versions:

`perlbrew available`

- Install/uninstall a Perl version:

`perlbrew {{install|uninstall}} {{version}}`

- List perl installations:

`perlbrew list`

- Switch to an installation and set it as default:

`perlbrew switch perl-{{version}}`

- Use the system perl again:

`perlbrew off`

- List installed CPAN modules for the installation in use:

`perlbrew list-modules`

- Clone CPAN modules from one installation to another:

`perlbrew clone-modules {{source_installation}} {{destination_installation}}`
