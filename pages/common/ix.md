# ix

> An alias used for ix.io pastebin service.
> More information: <http://ix.io/>.

- Define an alias for ix.io:

`alias ix="curl -F 'f:1=<-' ix.io"`

- Add the alias in bashrc and re-source it:

`printf '%s\n' "alias ix=\"curl -F 'f:1=<-' ix.io\"" >> "$HOME/.bashrc" && source "$HOME/.bashrc"`

- Create a pastebin short url from a command line:

`{{command}} | ix`
