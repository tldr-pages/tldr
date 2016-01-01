# defaults

> Access OS X user defaults

- read all defaults

`defaults read -app {{app-name}}`

- read specific defaults

`defaults read -app {{app-name}} {{key}}`

- write key value

`defaults write -app {{app-name}} {{key}} {{-type}} {{value}}`

- delete all defaults

`defaults delete -app {{app-name}}`