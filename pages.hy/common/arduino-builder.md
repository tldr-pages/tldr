# arduino-builder

> Կազմել arduino էսքիզներ:.
> ՀԵՌԱՑՄԱՆ ԶԳՈՒՇԱՑՈՒՄ. այս գործիքը աստիճանաբար հեռացվում է հօգուտ `arduino`-ի:.
> Լրացուցիչ տեղեկություններ. <https://github.com/arduino/arduino-builder>:.

- Կազմել էսքիզ.:

`arduino-builder -compile {{path/to/sketch.ino}}`

- Նշեք վրիպազերծման մակարդակը (կանխադրված՝ 5):

`arduino-builder -debug-level {{1..10}}`

- Նշեք հատուկ կառուցման գրացուցակ.:

`arduino-builder -build-path {{path/to/build_directory}}`

- Օգտագործեք կառուցման ընտրանքային ֆայլ՝ ամեն անգամ ձեռքով `-hardware`, `-tools` և այլն նշելու փոխարեն՝:

`arduino-builder -build-options-file {{path/to/build.options.json}}`

- Միացնել բառացի ռեժիմը.:

`arduino-builder -verbose {{true}}`
