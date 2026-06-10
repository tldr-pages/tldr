# pammixin interlace

> Միավորել պատկերի յուրաքանչյուր տող իր երկու հարևանների հետ:.
> Տես նաև՝ `pamdeinterlace`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pammixinterlace.html>:.

- Միավորել յուրաքանչյուր տող պատկերի մեջ իր երկու հարևանների հետ.:

`pammixinterlace {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Օգտագործեք նշված զտման մեխանիզմը.:

`pammixinterlace {{[-f|-filter]}} {{linear|fir|ffmpeg}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Միացրեք ադապտիվ զտման ռեժիմը, այսինքն՝ փոփոխեք միայն պիքսելները, որոնք ակնհայտորեն սանրված օրինակի մաս են կազմում.:

`pammixinterlace {{[-a|-adaptive]}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`
