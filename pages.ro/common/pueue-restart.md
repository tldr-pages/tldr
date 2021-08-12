# pueue restart

> Reporniți activitățile.
> Mai multe informaţii: <https://github.com/Nukesor/pueue>

- Reporniți o anumită sarcină:

`pueue restart {{task_id}}`

- Reporniți mai multe sarcini simultan și porniți-le imediat (nu enqueue):

`pueue restart --start-immediately {{task_id}} {{task_id}}`

- Reporniți o anumită sarcină dintr-o altă cale:

`pueue restart --edit-path {{task_id}}`

- Editați o comandă înainte de a reporni:

`pueue restart --edit {{task_id}}`

- Reporniți o activitate în loc (fără a pune în așteptare ca o sarcină separată):

`pueue restart --in-place {{task_id}}`

- Reporniți toate sarcinile eșuate și ascundeți-le:

`pueue restart --all-failed --stashed`
