# pw-loopback

> ایجاد دستگاه‌های loopback در PipeWire.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- ایجاد دستگاه loopback با رفتار پیش‌فرض:

`pw-loopback`

- ایجاد دستگاه loopback که خودکار به بلندگوها متصل می‌شود:

`pw-loopback {{[-i|--capture-props]}} '{{media.class=Audio/Sink}}'`

- ایجاد دستگاه loopback که خودکار به میکروفون متصل می‌شود:

`pw-loopback {{[-o|--playback-props]}} '{{media.class=Audio/Source}}'`

- ایجاد دستگاه loopback ساختگی که خودکار به چیزی متصل نمی‌شود:

`pw-loopback {{[-i|--capture-props]}} '{{media.class=Audio/Sink}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source}}'`

- اجبار گره‌ها به داشتن پورت‌های مشخص:

`pw-loopback {{[-m|--channel-map]}} '[{{FL FR}}]'`

- ایجاد دستگاه loopback که خودکار به بلندگوها متصل می‌شود و کانال‌های چپ و راست را بین مقصد و منبع جابه‌جا می‌کند:

`pw-loopback {{[-i|--capture-props]}} '{{media.class=Audio/Sink audio.position=[FL FR]}}' {{[-o|--playback-props]}} '{{audio.position=[FR FL]}}'`

- ایجاد دستگاه loopback که خودکار به میکروفون متصل می‌شود و کانال‌های چپ و راست را بین مقصد و منبع جابه‌جا می‌کند:

`pw-loopback {{[-i|--capture-props]}} '{{audio.position=[FR FL]}}' {{[-o|--playback-props]}} '{{media.class=Audio/Source audio.position=[FL FR]}}'`

- تعیین نام برای گره loopback:

`pw-loopback {{[-n|--name]}} "{{node_name}}"`
