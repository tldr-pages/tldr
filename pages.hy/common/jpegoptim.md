# jpegoptim

> Օպտիմալացնել JPEG պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/jpegoptim>:.

- Օպտիմիզացրեք JPEG պատկերների մի շարք՝ պահպանելով բոլոր առնչվող տվյալները.:

`jpegoptim {{image1.jpeg image2.jpeg image3.jpeg ...}}`

- Օպտիմիզացրեք JPEG պատկերները՝ հեռացնելով բոլոր ոչ էական տվյալները.:

`jpegoptim {{[-s|--strip-all]}} {{image1.jpeg image2.jpeg image3.jpeg ...}}`

- Ստիպեք, որ ելքային պատկերները լինեն առաջադեմ.:

`jpegoptim --all-progressive {{image1.jpeg image2.jpeg image3.jpeg ...}}`

- Ստիպեք ելքային պատկերներին ունենալ ֆիքսված առավելագույն ֆայլի չափ.:

`jpegoptim {{[-S|--size]}} {{250k}} {{image1.jpeg image2.jpeg image3.jpeg ...}}`
