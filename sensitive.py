# This is a test python file, which includes sensitive information from ROCKYOU password dataset, and some URLs. 

INTERNAL_URL1 = 'http://jira.agile.bns/'
INTERNAL_URL2 = 'http://jira.agile.com/'
INTERNAL_URL3 = 'http://jira.agile.bns/' + 'https://jira.agile.bns/' + 'ftp://jira.agile.bns/'
INTERNAL_URL3 = 'http://jira.agile.bns/' + 'www.google.com' + 'jira.agile.bns/'
POTENTIAL_PASSWORD_LIST = ['123456', 'shadow', 'monkey']

print("Internal URL1 is: "+INTERNAL_URL1)
print("Internal URL2 is: "+INTERNAL_URL2)
print("Internal URL3 is: "+INTERNAL_URL3)

i = 1
for(item in POTENTIAL_PASSWORD_LIST):
    print("Potential password "+i+": "+item)
    i+=1
    
print("This is a test script.")
