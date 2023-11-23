# settings

> एंड्रॉइड ओएस के बारे में जानकारी प्राप्त करें।
> अधिक जानकारी: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>।

- `global` नेमस्पेस में सेटिंग्स की एक सूची प्रदर्शित करें:

`settings list {{global}}`

- किसी विशिष्ट सेटिंग का मान प्राप्त करें:

`settings get {{global}} {{airplane_mode_on}}`

- किसी सेटिंग का विशिष्ट मान सेट करें:

`settings put {{system}} {{screen_brightness}} {{42}}`

- एक विशिष्ट सेटिंग हटाएँ:

`settings delete {{secure}} {{screensaver_enabled}}`
