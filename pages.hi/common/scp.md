# scp

> सुरक्षित प्रति।
> SSH पर सिक्योर कॉपी प्रोटोकॉल का उपयोग करके होस्ट के बीच फ़ाइलों की प्रतिलिपि बनाएँ।
> अधिक जानकारी: <https://man.openbsd.org/scp>।

- स्थानीय फ़ाइल को दूरस्थ होस्ट पर कॉपी करें:

`scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- रिमोट होस्ट से कनेक्ट करते समय एक विशिष्ट पोर्ट का उपयोग करें:

`scp -P {{port}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- किसी फ़ाइल को दूरस्थ होस्ट से स्थानीय निर्देशिका में कॉपी करें:

`scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- किसी निर्देशिका की सामग्री को दूरस्थ होस्ट से स्थानीय निर्देशिका में पुन: कॉपी करें:

`scp -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- स्थानीय होस्ट के माध्यम से स्थानांतरित होने वाले दो दूरस्थ होस्ट के बीच फ़ाइल की प्रतिलिपि बनाएँ:

`scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_directory}}`

- दूरस्थ होस्ट से कनेक्ट करते समय एक विशिष्ट उपयोगकर्ता नाम का उपयोग करें:

`scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_directory}}`

- दूरस्थ होस्ट के साथ प्रमाणीकरण के लिए विशिष्ट ssh निजी कुंजी का उपयोग करें:

`scp -i {{~/.ssh/private_key}} {{local_file}} {{remote_host}}:{{/path/remote_file}}` 
