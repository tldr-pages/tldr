# pod

> Gestor de dependencias para proyectos Swift y Objective-C Cocoa.
> Más información: <https://guides.cocoapods.org/terminal/commands.html>.

- Crea un Podfile para el proyecto actual con los contenidos por defecto:

`pod init`

- Descarga e instala todos los pods definidos en el Podfile (que no hayan sido instalados antes):

`pod install`

- Lista todos los pods disponibles:

`pod list`

- Muestra los pods obsoletos (de los instalados actualmente):

`pod outdated`

- Actualiza todos los pods instalados a su versión más reciente:

`pod update`

- Actualiza un pod específico (previamente instalado) a su versión más reciente:

`pod update {{nombre_del_pod}}`

- Elimina CocoaPods de un proyecto Xcode:

`pod deintegrate {{proyecto_xcode}}`
