# gst-launch-1.0

> GStreamer पाइपलाइन बनाएं और चलाएं।
> यह भी देखें: `gst-inspect-1.0`, `ffmpeg`।
> अधिक जानकारी: <https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html>।

- एक विंडो में परीक्षण वीडियो चलाएं:

`gst-launch-1.0 videotestsrc ! autovideosink`

- परीक्षण ऑडियो चलाएं और विस्तृत आउटपुट सक्षम करें:

`gst-launch-1.0 audiotestsrc {{[-v|--verbose]}} ! autoaudiosink`

- एक विंडो में मीडिया फ़ाइल चलाएं:

`gst-launch-1.0 playbin uri={{प्रोटोकॉल}}://{{होस्ट}}/{{फ़ाइल/का/पथ}}`

- मीडिया फ़ाइल को दोबारा एन्कोड करें:

`gst-launch-1.0 filesrc location={{फ़ाइल/का/पथ}} ! {{फ़ाइल_प्रकार}}demux ! {{कोडेक_प्रकार}}dec ! {{कोडेक_प्रकार}}enc ! {{फ़ाइल_प्रकार}}mux ! filesink location={{फ़ाइल/का/पथ}}`

- फ़ाइल को RTSP सर्वर पर स्ट्रीम करें:

`gst-launch-1.0 filesrc location={{फ़ाइल/का/पथ}} ! rtspclientsink location=rtsp://{{होस्ट_आईपी}}/{{फ़ाइल/का/पथ}}`

- `mp4` जैसे कंटेनरों के लिए, जिन्हें अंतिम रूप देना ज़रूरी है, `<Ctrl c>` से पाइपलाइन बंद होने पर End Of Stream इवेंट अनिवार्य रूप से भेजें:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} videotestsrc ! x264enc ! mp4mux ! filesink location={{फ़ाइल.mp4/का/पथ}}`

- परीक्षण वीडियो और परीक्षण ऑडियो को एक साथ मल्टीप्लेक्स करके फ़ाइल में सहेजें:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} videotestsrc ! {{x264enc}} ! {{एलिमेंट_नाम}}. audiotestsrc ! {{opusenc}} ! {{एलिमेंट_नाम}}. {{matroskamux}} name={{एलिमेंट_नाम}} ! filesink location={{फ़ाइल.mkv/का/पथ}}`

- डीबग आउटपुट सक्षम करें और पाइपलाइन को `.dot` फ़ाइल में सहेजें, जिसे बाद में `dot` जैसे उपकरणों से रेंडर किया जा सकता है:

`GST_DEBUG={{1..5}} GST_DEBUG_DUMP_DOT_DIR={{निर्देशिका/का/पथ}} gst-launch-1.0 {{पाइपलाइन}}`
