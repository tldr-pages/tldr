# defaults

> Access OS X user defaults

- read system default value

`defaults read {{domain}} {{key}}`

- read default values of applications

`defaults read -app {{app_name}} {{key}}`

- write key value

`defaults write {{domain}} {{key}} {{-type}} {{value}}`

- Speed up Mission Control animations

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- __[caution]__ delete all defaults of domain

`defaults delete {{domain}}`