import shodan
import os
import json
import time

SHODAN_API_KEY = ''

api = shodan.Shodan(SHODAN_API_KEY)

criteria = ''
userInput = ''
data = ''

def inputFunc():
    global userInput
    userInput = input('Please enter the criteria you want to search for(type \'search\' when you are done:   ').lower()
   
def checkInput():
    global criteria
    global userInput
    while userInput != 'search':
        inputFunc()
        if userInput != 'search':
            criteria = criteria + ' ' + userInput
        else:
            break

def dataFunc(criteriaString, dataDump):
    print('running dataFunc')
    try:
        criteriaString = criteriaString.replace(' ', '')
        with open('ShodanSearch' + criteriaString + time.strftime('%a%d%b%Y\'%H.%M.%S%p\'' + '.json'), 'w') as f:
            json.dump(dataDump, f, indent=2)
    except:
        print('Error creating log file')
        return 0

if __name__ == '__main__':
    checkInput()

criteria = criteria.lstrip()
print(f'Searching shodan for {criteria}. . .')

try:
    results = api.search(f'{criteria}')

    print(f'Results found: {results["total"]}')
    for result in results['matches']:
        data = (f'IP: {result["ip_str"]}\n{result["data"]}\n\n')
        print(data)
        dataFunc(criteria, data)
except shodan.APIError as e:
    print(f'Error: {e}')

