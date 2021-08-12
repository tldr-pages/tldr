# godot

> Un motor de joc cu sursă deschisă 2D și 3D.
> Mai multe informaţii: <https://godotengine.org/>

- Rulați un proiect dacă directorul curent conține un fișier `project.godot, altfel deschideți managerul de proiect:

`godot`

- Editează un proiect (directorul curent trebuie să conțină un fișier `project.godot”):

`godot -e`

- Deschide managerul de proiect chiar daca directorul curent contine un fisier `project.godot:

`godot -p`

- Exportați un proiect pentru o presetare de export dată (presetarea trebuie definită în proiect):

`godot --export {{preset}} {{output_path}}`

- Execută un fișier GDScript independent (script-ul trebuie să moștenească de la `Scenetre` sau `Mainloop`):

`godot -s {{script.gd}}`
