# pw-loopback

> Ferramenta para Cria dispositivos de loopback no pipewire.
> Mais informações: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Cria um dispositivo de loopback com o comportamento padrão de loopback:

`pw-loopback`

- Cria um dispositivo de loopback que se conecta automaticamente aos alto-falantes:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}'`

- Cria um dispositivo de loopback que se conecta automaticamente ao microfone:

`pw-loopback -m '{{[FL FR]}}' --playback-props='{{media.class=Audio/Source}}'`

- Cria um dispositivo fictício que não se conecta automaticamente a nada:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}' --playback-props='{{media.class=Audio/Source}}'`

- Cria um dispositivo de loopback que se conecta automaticamente aos alto-falantes e troca os canais esquerdo e direito entre o dispositivo de entrada e o de saída:

`pw-loopback --capture-props='{{media.class=Audio/Sink audio.position=[FL FR]}}' --playback-props='{{audio.position=[FR FL]}}'`

- Cria um dispositivo de loopback que se conecta automaticamente ao microfone e troca os canais esquerdo e direito entre o dispositivo de entrada e o de saída:

`pw-loopback --capture-props='{{audio.position=[FR FL]}}' --playback-props='{{media.class=Audio/Source audio.position=[FL FR]}}'`
