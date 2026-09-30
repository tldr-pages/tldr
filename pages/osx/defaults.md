# defaults

> Get and set macOS application preferences, system-wide and per-user.
> More information: <https://keith.github.io/xcode-man-pages/defaults.1.html>.

- Show all user preferences:

`defaults read`

- Show the value of a specific preference key in a domain:

`defaults read {{com.apple.dock}} {{tilesize}}`

- Write a preference value (e.g. show hidden files in Finder):

`defaults write {{com.apple.finder}} {{AppleShowAllFiles}} -bool {{true}}`

- Delete a preference key (reverts to the system default):

`defaults delete {{com.apple.dock}} {{tilesize}}`

- Search all domains for preferences containing a string:

`defaults find {{dark}}`
