# pw-loopback

> 在 PipeWire 中创建环回设备。
> 更多信息：<https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- 使用默认的环回行为创建环回设备：

`pw-loopback`

- 创建一个自动连接到扬声器的环回设备：

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}'`

- 创建一个自动连接到麦克风的环回设备：

`pw-loopback -m '{{[FL FR]}}' --playback-props='{{media.class=Audio/Source}}'`

- 创建一个不会自动连接到任何设备的虚拟环回设备：

`pw-loopback -m '{{[FL FR]}}' --capture-props='{{media.class=Audio/Sink}}' --playback-props='{{media.class=Audio/Source}}'`

- 创建一个自动连接到扬声器并交换输入输出设备左右声道的环回设备：

`pw-loopback --capture-props='{{media.class=Audio/Sink audio.position=[FL FR]}}' --playback-props='{{audio.position=[FR FL]}}'`

- 创建一个自动连接到麦克风并交换输入输出设备左右声道的环回设备：

`pw-loopback --capture-props='{{audio.position=[FR FL]}}' --playback-props='{{media.class=Audio/Source audio.position=[FL FR]}}'`
