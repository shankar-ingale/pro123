import re
import sys

#Taking Log File as input argument
#filename=sys.argv[1]

#Compiling regular expressions to match for Cancelled or Failed
reg=re.compile(r'Flash cancelled')
reg1=re.compile(r'Flash failed')
reg2=re.compile(r'Flash Success')

filename='Test.log'
#Reading the Log file
with open(filename,'r') as fp:
    content=fp.readlines()

#Creating 'Test.csv' file to write te analysis output
with open('Test.csv','w') as fp:
    for line in content:
        line_value=line.split('  ')
        match_failed=reg1.findall(line_value[0])
        match_cancelled=reg.findall(line_value[0])
        match_Success=reg2.findall(line_value[0])
        if match_cancelled:
            print ('Flash is Cancelled\n')
            fp.writelines('Flash is Cancelled')
            break
        if match_failed:
            print ('Flash is Failed\n')
            fp.writelines('Flash is Failed')
            break
        if match_failed:
            print ('Flash is Success\n')
            fp.writelines('Flash is Success')
            break
        else:
            pass
            

    


