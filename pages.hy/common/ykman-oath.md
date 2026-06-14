# ykman երդում

> Կառավարեք OATH YubiKey հավելվածը:.
> `keyword`-ը կարող է լինել անվանման կամ թողարկողի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>:.

- Ցուցադրել OATH հավելվածի մասին ընդհանուր տեղեկություններ.:

`ykman oath info`

- Փոխեք գաղտնաբառը, որն օգտագործվում է OATH հաշիվները պաշտպանելու համար (ավելացրեք `--clear` այն հեռացնելու համար).:

`ykman oath access change`

- Ավելացնել նոր հաշիվ (թողարկողը պարտադիր չէ).:

`ykman oath accounts add {{[-i|--issuer]}} {{issuer}} {{name}}`

- Թվարկեք բոլոր հաշիվները (դրանց թողարկողների հետ).:

`ykman oath accounts list`

- Թվարկեք բոլոր հաշիվները իրենց ընթացիկ TOTP/HOTP կոդերով (ըստ ցանկության՝ ցանկը զտելով հիմնաբառով).:

`ykman oath accounts code {{keyword}}`

- Վերանվանել հաշիվը.:

`ykman oath accounts rename {{keyword}} {{issuer:name|name}}`

- Ջնջել հաշիվը.:

`ykman oath accounts delete {{keyword}}`

- Ջնջել բոլոր հաշիվները և վերականգնել գործարանային կարգավորումները.:

`ykman oath reset`
