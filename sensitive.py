# This is a test python file, which includes sensitive information from ROCKYOU password dataset, and some URLs. 

INTERNAL_URL = 'http://jira.agile.bns/'
POTENTIAL_PASSWORD_LIST = ['123456', 'shadow', 'monkey']

print("Internal URL is: "+INTERNAL_URL)

i = 1
for(item in POTENTIAL_PASSWORD_LIST):
    print("Potential password "+i+": "+item)
    i+=1
    
print("This is a test script.")
