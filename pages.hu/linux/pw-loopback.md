# pw-loopback

> Eszköz loopback eszközök létrehozására a pipewire-ben. További információ: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Hozzon létre egy loopback eszközt az alapértelmezett loopback viselkedéssel:

`pw-loopback`

- Hozzon létre egy loopback eszközt, amely automatikusan csatlakozik a hangszórókhoz:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}'`

- Hozzon létre egy olyan loopback eszközt, amely automatikusan csatlakozik a mikrofonhoz:

`pw-loopback -m '{{[FL FR]}}' --playback-props='{{media.class=Audio/Source}}'`

- Létrehoz egy dummy loopback-eszközt, amely nem csatlakozik automatikusan semmihez:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}' --playback-props='{{media.class=Audio/Source}}'`

- Hozzon létre egy olyan loopback-eszközt, amely automatikusan csatlakozik a hangszórókhoz, és felcseréli a bal és jobb csatornát a nyelő és a forrás között:

`pw-loopback --capture-props='{{media.class=Audio/Sink audio.position=[FL FR]}}' --playback-props='{{audio.position=[FR FL]}}'`

- Hozzon létre egy olyan loopback eszközt, amely automatikusan csatlakozik a mikrofonhoz, és felcseréli a bal és jobb csatornát a nyelő és a forrás között:

`pw-loopback --capture-props='{{audio.position=[FR FL]}}' --playback-props='{{media.class=Audio/Source audio.position=[FL FR]}}'`
