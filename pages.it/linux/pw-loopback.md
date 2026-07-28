# pw-loopback

> Crea dispositivi loopback in PipeWire.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- Crea un dispositivo loopback con comportamento predefinito:

`pw-loopback`

- Crea un dispositivo loopback che si connette automaticamente agli altoparlanti:

`pw-loopback {{[-i|--capture-props]}} '{{media.class=Audio/Sink}}'`

- Crea un dispositivo loopback che si connette automaticamente al microfono:

`pw-loopback {{[-o|--playback-props]}} '{{media.class=Audio/Source}}'`

- Crea un dispositivo loopback fittizio che non si connette automaticamente a nulla:

`pw-loopback {{[-i|--capture-props]}} '{{media.class=Audio/Sink}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source}}'`

- Forza i nodi ad avere porte specifiche:

`pw-loopback {{[-m|--channel-map]}} '[{{FL FR}}]'`

- Crea un dispositivo loopback che si connette automaticamente agli altoparlanti e scambia i canali sinistro e destro tra sink e source:

`pw-loopback {{[-i|--capture-props]}} '{{media.class=Audio/Sink audio.position=[FL FR]}}' {{[-o|--playback-props]}} '{{audio.position=[FR FL]}}'`

- Crea un dispositivo loopback che si connette automaticamente al microfono e scambia i canali sinistro e destro tra sink e source:

`pw-loopback {{[-i|--capture-props]}} '{{audio.position=[FR FL]}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source audio.position=[FL FR]}}'`

- Dai un nome al nodo loopback:

`pw-loopback {{[-n|--name]}} "{{nome_nodo}}"`
