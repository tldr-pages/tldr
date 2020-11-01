# electron-packager

> A tool used to build Electron app executables for Windows, Linux and MacOS.
> Requires a valid package.json in the application directory.
> More information: <https://github.com/electron/electron-packager>.

- Package an application for the current architecture and platform:

`electron-packager "{{path/to/app}}" "{{app_name}}"`

- Package an application for all architectures and platforms:

`electron-packager "{{path/to/app}}" "{{app_name}}" --all`

- Package an application for 64-bit Linux:

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{linux}}" --arch="{{x64}}"`

- Package an application for ARM MacOS:

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{darwin}}" --arch="{{arm64}}"`
