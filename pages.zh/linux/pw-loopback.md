# pw-loopback

> 在 PipeWire 中创建环回设备。
> 更多信息：<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>。

- 创建一个具有默认环回行为的环回设备：

`pw-loopback`

- 创建一个自动连接到扬声器的环回设备：

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}'`

- 创建一个自动连接到麦克风的环回设备：

`pw-loopback -m '{{[FL FR]}}' --playback-props='{{media.class=Audio/Source}}'`

- 创建一个不自动连接到任何设备的虚拟环回设备：

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}' --playback-props='{{media.class=Audio/Source}}'`

- 创建一个自动连接到扬声器并在接收端和源之间交换左右声道的环回设备：

`pw-loopback --capture-props='{{media.class=Audio/Sink audio.position=[FL FR]}}' --playback-props='{{audio.position=[FR FL]}}'`

- 创建一个自动连接到麦克风并在接收端和源之间交换左右声道的环回设备：

`pw-loopback --capture-props='{{audio.position=[FR FL]}}' --playback-props='{{media.class=Audio/Source audio.position=[FL FR]}}'`