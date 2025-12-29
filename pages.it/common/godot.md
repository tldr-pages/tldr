# godot

> Motore di gioco open source 2D e 3D.
> Maggiori informazioni: <https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html>.

- Esegue un progetto se la directory corrente contiene un file `project.godot`, altrimenti apre il project manager:

`godot`

- Modifica un progetto (la directory corrente deve contenere un file `project.godot`):

`godot {{[-e|--editor]}}`

- Apre il project manager anche se la directory corrente contiene un file `project.godot`:

`godot {{[-p|--project-manager]}}`

- Esporta un progetto per il rilascio usando un preset di esportazione specificato (il preset deve essere definito nel progetto):

`godot --export-release {{preset}} {{output_path}}`

- Esegue un file GDScript standalone (lo script deve ereditare da `SceneTree` o `MainLoop`):

`godot {{[-s|--script]}} {{script.gd}}`
