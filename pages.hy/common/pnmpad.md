# pnmpad

> Ավելացնել եզրագծեր PNM պատկերին:.
> Տես նաև՝ `pnmmargin`, `pamcut`, `pamcomp`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmpad.html>:.

- Նկարին ավելացրեք նշված չափերի սահմանները.:

`pnmpad {{[-l|-left]}} {{100}} {{[-ri|-right]}} {{150}} {{[-t|-top]}} {{123}} {{[-bo|-bottom]}} {{456}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Պատկերը տեղադրեք նշված չափի մեջ.:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-he|-height]}} {{500}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Պատկերի լայնությունը լրացրեք նշված չափի վրա՝ վերահսկելով աջ և ձախ ներդիրների հարաբերակցությունը.:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-ha|-halign]}} {{0.7}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Պահեք պատկերի լայնությունը՝ օգտագործելով նշված գույնը.:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-c|-color]}} {{red}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
