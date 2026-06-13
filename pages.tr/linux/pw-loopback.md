# pw-loopback

> PipeWire'da geri döngü cihazları yaratma aracı.
> Daha fazla bilgi için: <https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- Varsayılan geri döngü davranışına sahip bir geri döngü cihazı yarat:

`pw-loopback`

- Hoparlörlere otomatik olarak bağlanan bir geri döngü cihazı yarat:

`pw-loopback {{[-m|--channel-map]}} '{{[FL FR]}}' {{[-i|--capture-props]}} '{{media.class=Audio/Sink}}'`

- Mikrofona otomatik olarak bağlanan bir geri döngü cihazı yarat:

`pw-loopback {{[-m|--channel-map]}} '{{[FL FR]}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source}}'`

- Hiçbir şeye otomatik olarak bağlanmayan salak bir geri döngü cihazı yarat:

`pw-loopback {{[-m|--channel-map]}} '{{[FL FR]}}' {{[-i|--capture-props]}} '{{media.class=Audio/Sink}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source}}'`

- Hoparlörlere otomatik olarak bağlanan ve taban-kaynak arasında sağ-sol kanalların yerini değiştiren bir geri döngü cihazı yarat:

`pw-loopback {{[-i|--capture-props]}} '{{media.class=Audio/Sink audio.position=[FL FR]}}' {{[-o|--playback-props]}} '{{audio.position=[FR FL]}}'`

- Mikrofona otomatik olarak bağlanan ve taban-kaynak arasında sağ-sol kanalların yerini değiştiren bir geri döngü cihazı yarat:

`pw-loopback {{[-i|--capture-props]}} '{{audio.position=[FR FL]}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source audio.position=[FL FR]}}'`
