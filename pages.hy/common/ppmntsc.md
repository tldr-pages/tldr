# ppmntsc

> PPM պատկերի RGB գույները համատեղելի դարձրեք NTSC կամ PAL գունային համակարգերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmntsc.html>:.

- Դարձրեք RGB գույները PPM պատկերում համատեղելի NTSC գունային համակարգերի հետ.:

`ppmntsc {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- PPM պատկերի RGB գույները համատեղելի դարձրեք PAL գունային համակարգերի հետ.:

`ppmntsc --pal {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Տպեք մուտքագրված պատկերի անօրինական պիքսելների քանակը `stderr`:

`ppmntsc {{[--verb|--verbose]}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Արտադրեք միայն օրինական/անօրինական/ուղղված պիքսելները, մյուս պիքսելները դրեք սևի.:

`ppmntsc --{{legalonly|illegalonly|correctedonly}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`
