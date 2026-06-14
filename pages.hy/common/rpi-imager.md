# rpi-պատկեր

> Ֆլեշ պատկերները պահեստավորման սարքերի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/raspberrypi/rpi-imager>:.

- Գրեք կոնկրետ պատկեր որոշակի բլոկային սարքի վրա.:

`rpi-imager --cli {{path/to/image.zip}} {{/dev/sdX}}`

- Գրեք կոնկրետ պատկեր բլոկ սարքի վրա՝ անջատելով ստուգիչ գումարի ստուգումը.:

`rpi-imager --cli --disable-verify {{path/to/image.zip}} {{/dev/sdX}}`

- Գրեք կոնկրետ պատկեր բլոկ սարքի վրա, որը ստուգումը գործարկելիս ակնկալում է որոշակի ստուգիչ գումար.:

`rpi-imager --cli --sha256 {{expected_hash}} {{path/to/image.zip}} {{/dev/sdX}}`
