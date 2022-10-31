# pw-loopback

> PipeWire'da geri döngü cihazları yaratma aracı.
> Daha fazla bilgi için: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Varsayılan geri döngü davranışına sahip bir geri döngü cihazı yarat:

`pw-loopback`

- Hoparlörlere otomatik olarak bağlanan bir geri döngü cihazı yarat:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}'`

- Mikrofona otomatik olarak bağlanan bir geri döngü cihazı yarat:

`pw-loopback -m '{{[FL FR]}}' --playback-props='{{media.class=Audio/Source}}'`

- Hiçbir şeye otomatik olarak bağlanmayan salak bir geri döngü cihazı yarat:

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}' --playback-props='{{media.class=Audio/Source}}'`

- Hoparlörlere otomatik olarak bağlanan ve taban-kaynak arasında sağ-sol kanalların yerini değiştiren bir geri döngü cihazı yarat:

`pw-loopback --capture-props='{{media.class=Audio/Sink audio.position=[FL FR]}}' --playback-props='{{audio.position=[FR FL]}}'`

- Mikrofona otomatik olarak bağlanan ve taban-kaynak arasında sağ-sol kanalların yerini değiştiren bir geri döngü cihazı yarat:

`pw-loopback --capture-props='{{audio.position=[FR FL]}}' --playback-props='{{media.class=Audio/Source audio.position=[FL FR]}}'`
