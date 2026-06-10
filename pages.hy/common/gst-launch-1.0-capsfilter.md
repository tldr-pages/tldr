# gst-launch-1.0 capsfilter

> Զտել խողովակաշարի հնարավորությունները:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/coreelements/capsfilter.html>:.

- Զտեք միայն գորշ գույնի ձևաչափը թույլատրելու համար.:

`gst-launch-1.0 {{videotestsrc}} ! capsfilter caps=video/x-raw,format=GRAY8 ! {{videoconvert ! autovideosink}}`

- Արեք նույնը, բայց կարճ ձևով.:

`gst-launch-1.0 {{videotestsrc}} ! video/x-raw,format=GRAY8 ! {{videoconvert ! autovideosink}}`

- Սահմանափակեք տեսանյութի հնարավորությունները որոշակի չափերով.:

`gst-launch-1.0 {{videotestsrc}} ! video/x-raw,width={{640}},height={{480}} ! {{videoconvert ! autovideosink}}`

- Նշեք որոշակի շրջանակի արագություն.:

`gst-launch-1.0 {{videotestsrc}} ! video/x-raw,framerate={{30}}/1 ! {{videoconvert ! autovideosink}}`
