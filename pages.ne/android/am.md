# am

> एन्ड्रोइड गतिविधि प्रबन्धक।
> थप जानकारी: <https://developer.android.com/studio/command-line/adb#am>.

- एक विशेष गतिविधि सुरु गर्नुहोस्:

`am start -n {{com.android.settings/.Settings}}`

- एउटा गतिविधि सुरु गर्नुहोस् र यसलाई [d] डाटा पास गर्नुहोस्:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- एक विशिष्ट कार्य र [c] श्रेणीसँग (category) मेल खाने गतिविधि सुरु गर्नुहोस्:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- एउटा उद्देश्यलाई URI मा रूपान्तरण गर्नुहोस्:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
