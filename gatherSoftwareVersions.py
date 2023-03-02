strFilter = ["Pit","VR-","Hex","Cal","Ant"]
#filtered_view = []
filtered_view = ['Pitch Commander 3.2.3:3.2.3','Pitch pRTI 5.5.1.0:5.5.1.0','VR-Engage version VR-Engage 1.7d:VR-Engage 1.7d','RTDynamics VR-Forces Plug-in R16e.28414-MilitaryEdition-VRF VC1',
'VR-Forces 4.10i:4.10i','VR-Vantage 2.8g:2.8g','TDL for VR-Forces 4.10i v1.4.1a-2917-58:','HexChat:2.13.3','Calytrix Technologies CNR:6.0.0.117','AntiMicro:2.20.2']
unfiltered_view = []

stripped_name = []
stripped = []
split_strip = []
split_strip2 = []
split_strip3 = []
split_strip_posn = []
split_strip_count = []
stripped_text = []

strMSVC_VRE = " MSVC++15.0"
strMSVC_VRF = " 64"
strMSVC_VRV = "-bit"

import re

#call powershell script to get source input file
#unfiltered_view = open('list_software.txt').readlines()

def remove_all_msvc():
    for i in unfiltered_view:
        stripMSVC = i.replace(strMSVC_VRE,"").replace(strMSVC_VRF,"").replace(strMSVC_VRV,"")
        stripped_name.append(stripMSVC)
    return stripped_name

def software_filter():
    strip_count = 0
#    stripped = remove_all_msvc()
#   for i in strFilter:
#        for j in stripped:
#            formatString = j.replace('\n',"")
#            if (j.find(i) !=-1 and j not in filtered_view):
#                filtered_view.append(formatString)
#    return filtered_view
    for i in filtered_view:
        strip_posn = i.index(":")
        text_length = len(i)
        strip_count = text_length - (strip_posn+1)
        strip_start = strip_posn - strip_count
        for j in strip_count:
            for k in strip_start:
                updated_text = 
        split_strip2.append(updated_text)
    return split_strip2

# remove powershell file

softwareVersions = software_filter()
print(f"Installed key software versions :{softwareVersions}")