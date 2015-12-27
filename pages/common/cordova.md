# cordova

> Mobile apps with HTML, CSS & JS

- Create a cordova project

`cordova create {{path}}`

- Create a detailed cordova project

`cordova create {{path}} {{package.name}} {{project.name}}`

- Display the current workspace status

`cordova info`

- Add a cordova platform

`cordova platform add {{platform}}`

- Update a cordova platform

`cordova platform update {{platform}}`

- Remove a cordova platform

`cordova platform remove {{platform}}`

- Show platform list

`cordova platform list`

- Add a cordova plugin from cordova plugin market

`cordova plugin add {{pluginid}}`

- Add a cordova plugin from local path

`cordova plugin add {{path}}`

- Add a cordova plugin from git url

`cordova plugin add {{giturl}}`

- Remove a cordova plutin

`cordova plugin remove {{pluginid}}`

- Show plugin list

`cordova plugin list`

- Copies files for specified platforms, or all platforms

`cordova prepare {{--ios}}`

- Builds the app for specified platforms, or all platforms

`cordova compile {{--debug}} {{--emulator}} {{--android}}`

- Run project

`cordova run {{--ios}}`

- Run project with a local webserver

`cordova serve {{8000}}`

