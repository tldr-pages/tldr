# gst-launch-1.0 fakesink

> Կեղծ լվացարան, որը կուլ է տալիս ամեն ինչ:.
> Օգտակար է ստուգելու համար, թե խողովակաշարի որ հատվածն է կոտրվում:.
> Լրացուցիչ տեղեկություններ. <https://gstreamer.freedesktop.org/documentation/coreelements/fakesink.html>:.

- Սպառեք տվյալները խողովակաշարից՝ առանց դրանք դուրս բերելու.:

`gst-launch-1.0 {{pipeline}} ! fakesink`

- Տպել տեղեկատվությունը ստացված տվյալների վերաբերյալ.:

`gst-launch-1.0 {{[-v|--verbose]}} {{pipeline}} ! fakesink silent=false`
