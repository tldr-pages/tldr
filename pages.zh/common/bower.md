# bower

> 前端web开发的包管理方案.
> bower已经成为过去时，推荐使用webpack、yarn、parcel
> 详见: <https://bower.io/>.

- Install a project's dependencies, listed in its bower.json:

`bower install`

- Install one or more packages to the bower_components directory:

`bower install {{package}} {{package}}`

- Uninstall packages locally from the bower_components directory:

`bower uninstall {{package}} {{package}}`

- List local packages and possible updates:

`bower list`

- Display help information about a bower command:

`bower help {{command}}`

- Create a bower.json file for your package:

`bower init`

- Install a specific dependency version, and add it to bower.json:

`bower install {{local_name}}={{package}}#{{version}} --save`
