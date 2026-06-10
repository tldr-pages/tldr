#գոդոտ

> Բաց կոդով 2D և 3D խաղերի շարժիչ:.
> Լրացուցիչ տեղեկություններ. <https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html>:.

- Գործարկեք նախագիծը, եթե ընթացիկ գրացուցակը պարունակում է `project.godot` ֆայլ, հակառակ դեպքում բացեք ծրագրի կառավարիչը.:

`godot`

- Խմբագրել նախագիծը (ընթացիկ գրացուցակը պետք է պարունակի `project.godot` ֆայլ).:

`godot {{[-e|--editor]}}`

- Բացեք ծրագրի կառավարիչը, նույնիսկ եթե ընթացիկ գրացուցակը պարունակում է `project.godot` ֆայլ.:

`godot {{[-p|--project-manager]}}`

- Արտահանել նախագիծ թողարկման համար՝ օգտագործելով տվյալ արտահանման նախադրյալը (նախադրվածը պետք է սահմանվի նախագծում).:

`godot --export-release {{preset}} {{output_path}}`

- Կատարեք ինքնուրույն GDScript ֆայլ (սկրիպտը պետք է ժառանգի `SceneTree` կամ `MainLoop`):

`godot {{[-s|--script]}} {{script.gd}}`
