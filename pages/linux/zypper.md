# zypper

> SUSE & openSUSE package management utility.

- Synchronize list of packages and versions available:

`zypper refresh`

- Install a new package:

`zypper install {{package}}`

- Remove a package:

`zypper remove {{package}}`

- Upgrade installed packages to newest available versions on Leap:

`zypper update`

- Upgrade installed packages to newest available versions on Tumbleweed:
  
`zypper dist-upgrade`

  Note: DO NOT update Tumbleweed through the YaST GUI or with `zypper update`
  
  Doing so can result in orphaned packages and other problems.

- Search package via keyword:

`zypper search {{keyword}}`
