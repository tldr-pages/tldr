# systemctl

> systemd सिस्टम और सेवा प्रबंधक को नियंत्रित करें।
> अधिक जानकारी: <https://www.freedesktop.org/software/systemd/man/systemctl.html>।

- सभी चल रही सेवाएँ दिखाएं:

`systemctl status`

- विफल इकाइयों की सूची:

`systemctl --failed`

- सेवा को चालना/रोकना/पुनरारंभ करना/रीलोड करना:

`systemctl {{start|stop|restart|reload}} {{इकाई}}`

- एक इकाई की स्थिति दिखाएं:

`systemctl status {{इकाई}}`

- एक इकाई को बूटअप पर स्वचलित रूप से चालाने/रोकने के लिए सक्षम/अक्षम करें:

`systemctl {{enable|disable}} {{इकाई}}`

- एक इकाई को सक्षम/अक्षम करने और मैन्युअल सक्रियण से रोकने/हटाने के लिए मास्क/अनमास्क करें:

`systemctl {{mask|unmask}} {{इकाई}}`

- systemd को पुनः लोड करें, नई या बदली गई इकाइयों के लिए स्कैन करें:

`systemctl daemon-reload`

- क्या किसी इकाई को सक्षम किया गया है, यह जाँचें:

`systemctl is-enabled {{इकाई}}`
