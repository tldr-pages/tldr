# nvram

> Manipulate firmware variables.
> More information: <https://ss64.com/osx/nvram.html>.

- [p]rint all the variables stored in the NVRAM:

`nvram -p`

- [p]rint all the variables stored in the NVRAM using [x]ML format:

`nvram -xp`

- Modify the value of a firmware variable:

`sudo nvram {{name}}="{{value}}"`

- [d]elete a firmware variable:

`sudo nvram -d {{name}}`

- [c]lear all the firmware variables:

`sudo nvram -c`

- Set a firmware variable from a specific [x]ML [f]ile:

`sudo nvram -xf {{path/to/file.xml}}`
