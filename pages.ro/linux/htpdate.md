# htpdate

> Sincronizați data și ora locală prin anteturile HTTP de la serverele web.
> Mai multe informaţii: <http://www.vervest.org/htp/>

- Sincronizați data și ora:

`sudo htpdate {{host}}`

- Efectuați simularea sincronizării, fără nici o acțiune:

`htpdate -q {{host}}`

- Compensați driftul ceasului systematisch:

`sudo htpdate -x {{host}}`

- Setați ora imediat după sincronizare:

`sudo htpdate -s {{host}}`
