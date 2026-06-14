# scrcpy

> Ցուցադրել և կառավարել ձեր Android սարքը աշխատասեղանի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Genymobile/scrcpy>:.

- Ցուցադրել միացված սարքի հայելին.:

`scrcpy`

- Անջատեք սարքի էկրանը և կանխեք այն քնելուց հայելու ընթացքում.:

`scrcpy {{[-S|--turn-screen-off]}} {{[-w|--stay-awake]}}`

- Ցուցադրել որոշակի սարքի հայելին՝ հիմնվելով դրա ID-ի կամ IP հասցեի վրա (գտեք այն `adb devices` հրամանի ներքո).:

`scrcpy {{[-s|--serial]}} {{0123456789abcdef|192.168.0.1:5555}}`

- Ցույց տալ հպումները ֆիզիկական սարքի վրա.:

`scrcpy {{[-t|--show-touches]}}`

- Ձայնագրեք ցուցադրման էկրանը.:

`scrcpy {{[-r|--record]}} {{path/to/file.mp4}}`

- Նշեք թիրախային գրացուցակը ֆայլերը սարքի վրա քաշելու և թողնելու համար (ոչ APK).:

`scrcpy --push-target {{path/to/directory}}`

- Դիտեք հեռախոսի տեսախցիկը (պահանջում է Android 12 կամ ավելի նոր).:

`scrcpy --video-source camera`

- Ստեղծեք Video4Linux2 սարք հեռախոսի տեսախցիկից (`v4l2loopback` պետք է տեղադրվի).:

`scrcpy --video-source camera --camera-size {{1920x1080}} --v4l2-sink {{/dev/video0}} --no-playback`
