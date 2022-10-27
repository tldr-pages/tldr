# cp

> फाइलहरू र डिरेक्टोरीहरू सार्नुहोस।
> थप जानकारी: <https://www.gnu.org/software/coreutils/cp>.

- एउटा स्थान बाट अर्को स्थानमा फाइलहरु सार्नुहोस :

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- फाइलको नाम उही राखेर अर्को डिरेक्टोरमा फाइलहरु सार्नुहोस :

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- पुनरावर्ती रूपमा डाइरेक्टरीमा भएका सबै चीजहरुलाइ अर्को स्थानमा सार्नुहोस(यदि स्थान पहिले देखि नै छ भने,डाइरेक्टर भित्र सार्नुहोस ):

`cp -R {{path/to/source_directory}} {{path/to/target_directory}}`

- पुनरावर्ती रूपमा एउटा डाइरेक्टरी सार्नुहोस, शब्दमय रुपमा (फाइलहरु सार्दा सार्दै सरिरहेको पनि देखिन्छ ):

`cp -vR {{path/to/source_directory}} {{path/to/target_directory}}`

- अन्तरक्रियात्मक रुपमा अर्को स्थानमा पाठ्य फाइलहरू सार्नुहोस (अधिलेखन गर्नु अघि प्रयोगकर्तालाई सोध्छ ):

`cp -i {{*.txt}} {{path/to/target_directory}}`

- सार्नु अघि प्रतीकात्मक लिङ्कहरू पछ्याउनुहोस्:

`cp -L {{link}} {{path/to/target_directory}}`
