# pnmnlfilt

> Կիրառեք ոչ գծային զտիչ PNM պատկերի վրա:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmnlfilt.html>:.

- Կիրառեք «ալֆա կտրված միջին» ֆիլտրը նշված ալֆա և շառավիղ արժեքներով PNM պատկերի վրա.:

`pnmnlfilt {{0.0..0.5}} {{radius}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Կիրառեք «օպտիմալ գնահատման հարթեցում» ֆիլտրը նշված աղմուկի շեմով և շառավղով PNM պատկերի վրա.:

`pnmnlfilt {{1.0..2.0}} {{radius}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Կիրառեք «եզրերի ընդլայնում» ֆիլտրը նշված ալֆայով և շառավղով PNM պատկերի վրա.:

`pnmnlfilt {{-0.9..(-0.1)}} {{radius}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
