# pixiecore

> Կառավարեք մեքենաների ցանցի բեռնումը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/danderson/netboot/tree/main/pixiecore>:.

- Սկսեք PXE boot server, որն ապահովում է `netboot.xyz` boot պատկեր.:

`pixiecore {{quick}} xyz --dhcp-no-bind`

- Սկսեք նոր PXE բեռնման սերվեր, որն ապահովում է Ubuntu-ի բեռնման պատկեր.:

`pixiecore {{quick}} ubuntu --dhcp-no-bind`

- Թվարկեք բոլոր հասանելի բեռնման պատկերները արագ ռեժիմի համար.:

`pixiecore quick --help`
