# npx

> Execute binaries from `npm` packages(most of the cli tools) .

- Execute the npm packages binaries(Package will be installed if it does not exist in node_modules or $PATH):

`npx {{module_name}}`

- Want to use multiple binaries, define the package name to be installed, then execute the binaries:

`npx -p {{package_name}} {{module_name}}`

- View help contents:

`npx --help`
