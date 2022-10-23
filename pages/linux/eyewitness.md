# eyewitness

> Python based tool to gather screenshots of websites, as well as additional information such as header info and default credentials if possible.
> More information: <https://www.christophertruncer.com/eyewitness-triage-tool>.

- Scan a single website using --single flag:

`eyewitness --single {{website}}`

- Scan multiple urls from file and output to foldername:

`eyewitness -f {{filename}} -d {{foldername}}`

- Scan muliple urls from xml file (nmap and nessus xml file format) and output to folername:

`eyewitness -x {{filename}} -d {{foldername}}`

- Scan multiple urls from file providing a specific useragent such as Mozilla/4.0: 

`eyewitness -f {{filename}} --useragent {{Mozilla/4.0}}`

- Scan multiple urls from file using --jitter flag to randomize accessing each url with a base number of seconds:

`eyewitness -f {{filename}} --jitter {{seconds}}
