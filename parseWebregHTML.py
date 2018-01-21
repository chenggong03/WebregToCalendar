# PLAN:
# Get page and find all xml table data under list-id-table, parse them into data
# (name: course no., type; note: title, section code, instructor, grade option,
# unit; days: days; location: bldg, room) if it’s empty, auto fill with data
# before it. Store temporarily in memory.
# Use requests lib (not working) to get pass authentication and beautiful soup
# to extract data.
# Store info in a temporary .ics file, and execute the .ics file. And delete the
# temporary file.

import requests
from bs4 import BeautifulSoup
import settings

# url = "https://act.ucsd.edu/webreg2/main?p1=WI18&p2=UN#tabs-0"
url = "https://a4.ucsd.edu/tritON/Authn/UserPassword"
# url = "https://act.ucsd.edu/webreg2/start"
data = {
'urn:mace:ucsd.edu:sso:username' : settings.PID,
'urn:mace:ucsd.edu:sso:password' : settings.PASS,
'initAuthMethod' : "urn:mace:ucsd.edu:sso:studentsso",
'submit' : "submit",
'urn:mace:ucsd.edu:sso:authmethod' : "urn:mace:ucsd.edu:sso:studentsso"
}
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

s = requests.Session()
response = s.get(url)
cookies = dict(response.cookies)
response = s.post(url, data=data, headers=headers, cookies=cookies)

soup = BeautifulSoup(response.text, 'html.parser')

print(response.url)
print(response.status_code)
print("_____________________________")
#print(response.content)
