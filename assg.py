"""
7.1 Write a program that prompts for a file name,then opens that file and reads through the file,
and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
"""
"""
fname = input("Enter file name: ")
try:
  fh = open(fname)
except:
  print('File does noty exist')
  quit()
data = fh.read()
data = data.rstrip()
print(data.upper())
"""




"""
7.2 Write a program that prompts for a file name,
then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the linesand compute the average of those values
and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
when you are testing below enter mbox-short.txt as the file name.
"""
"""
fname = input("Enter file name: ")
try:
   fh = open(fname)
except:
  print('File does noty exist')
  quit()
count = 0
total = 0
for line in fh:
   if not line.startswith("X-DSPAM-Confidence:"):
     continue
   count = count +1
   index = line.find('0')
   number = float(line[index:])
   total = total + number
avg = total/count
print('Average spam confidence:', avg)
print("Done")
"""




"""
8.4 Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see
if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
"""
"""
fhandler = open('romeo.txt')
wordsList = list()
for line in fhandler:
  words = line.split()
 for word in words:
    if word not in wordsList:
      wordsList.append(word)
wordsList.sort()
print(wordsList)
"""



"""
8.5 Open the file mbox-short.txt and read it line by line.
When you find a line that starts with 'From ' like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split()
and print out the second word in the line (i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
"""
"""
count = 0
fhandler = open('mbox-short.txt')
for line in fhandler:
  if not line.startswith('From'): continue
  if  line.startswith('From:'): continue
  else:
    count = count + 1
    l = line.strip().split()
    address = l[1]
    print (address)
print("There were", count, "lines in the file with From as the first word")
"""



"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
"""
fhandler = open('mbox-short.txt')
emails = dict()
for line in fhandler:
  if not line.startswith('From'): continue
  if  line.startswith('From:'): continue
  else:
    l = line.strip().split()
    address = l[1]
    emails[address] = emails.get(address, 0)+1
biggestCount = None
biggestSender = None
for email,count in emails.items():
  if biggestCount is None or count > biggestCount:
    biggestCount = count
    biggestSender = email
print(biggestSender, biggestCount)
"""




"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
"""
fhandler = open('mbox-short.txt')
sendingHour = dict()
for line in fhandler:
  if not line.startswith('From'): continue
  if  line.startswith('From:'): continue
  else:
    l = line.strip().split()
    time = l[5]
    t = time.split(':')
    hour = t[0]
    sendingHour[hour] = sendingHour.get(hour, 0)+1
sortedHours = sorted(sendingHour.items())
for hour, count in sortedHours:
  print(hour, count)
"""




"""
python 3: Week 2(Chapter 11)>>>
Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.
Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_938803.txt (There are 91 values and the sum ends with 245)
The basic outline of this problem is to read the file, look for integers using the re.findall(),
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
"""
"""
import re
Total = 0
fhandler = open('actual.txt')
for line in fhandler:
  ints = re.findall('[0-9]+', line)
  for n in ints:
    num = int(n)
    Total = Total + num
print(Total)
"""




"""
python 3: Week 3(Chapter 11)>>>
Exploring the HyperText Transport Protocol
You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the response headers:
1)Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
Make sure to change the code to retrieve the above URL - the values are different for each URL.
2)Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
"""
"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
"""




"""
python 3: Week 4(Chapter 12)>>>
Scraping Numbers from HTML using BeautifulSoup In this assignment 
you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers and compute the sum of the numbers in the file.
Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_938805.html (Sum ends with 95)
The file is a table of names and comment counts.
You can ignore most of the data in the file except for lines like the following:
<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
"""
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
tds = soup.select('td:last-child')
for td in tds[1:]:
  num = int(td.text)
  sum = sum + num
print(sum)
"""
#OR
"""
sum=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    y=str(tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        sum=sum+i
print(sum)
"""
#OR
"""
s = sum(int(td.text) for td in soup.select('td:last-child')[1:])
print(s)
"""




"""
python 3: Week 4(Chapter 12)>>>
In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
The program will use urllib to read the HTML from the data files below,extract the href= values from the anchor tags,
scan for a tag that is in a particular position relative to the first name in the list, follow that link
and repeat the process a number of times and report the last name you find.
Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1).
Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Somaya.html
Find the link at position 18 (the first name is 1). Follow that link.
Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: H
Strategy:
The web pages tweak the height between the links and hide the page after a few seconds 
to make it difficult for you to do the assignment without writing a Python program.
But frankly with a little effort and patience you can overcome these attempts 
to make it a little harder to complete the assignment without writing a Python program. But that is not the point.
The point is to write a clever Python program to solve the program.
"""
"""
#imports
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Prompts
url = input('URL: ')
position = int(input('Position: '))-1
count = int(input('Count: '))
print('\n')

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

while count > 0:
  #Get link at specified position
  #Print the Name and link
  link = tags[position].get('href', None)
  print(tags[position].contents[0])
  print('Retrieving: ',link)

  #Follow the link and scrap it
  #Repeat the Process
  html = urllib.request.urlopen(link, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  count = count - 1
"""




"""
python 3: Week 5(Chapter 13)>>>
Extracting Data from XML
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and 
then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_938807.xml (Sum ends with 20)
Data Format and Approach:
You are to look through all the <comment> tags and find the <count> values sum the numbers.
The closest sample code that shows how to parse XML is geoxml.py.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML
for any tag named 'count' with the following line of code: counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details.
You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
"""
"""
import urllib.request, urllib.parse, urllib.error
import ssl                                             #Transport Layer Security
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
xmlText = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xmlText)
commentsList = tree.findall('comments/comment')
countSum = 0

for comment in commentsList:
  c = int(comment.find('count').text)
  countSum = countSum + c

print('Count', countSum)
"""




"""
python 3: Week 6(Chapter 13)>>>
Extracting Data from JSON
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below:
Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_938808.json (Sum ends with 49)
The closest sample code that shows how to parse JSON and extract a list is json2.py.
You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.
"""
"""
import ssl
import json
import urllib.request, urllib.parse, urllib.error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL: ')
encodedData = urllib.request.urlopen(url, context = ctx)
decodedData = encodedData.read().decode()
parsedData = json.loads(decodedData)
countTotal = 0
#count = parsedData['comments'][0]['count']
for item in parsedData['comments']:
  #print (item['count'])
  count = int(item['count'])
  countTotal = countTotal + count
print(countTotal)
"""




"""
python 3: Week 6(Chapter 13)>>>
Calling a JSON API
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
The program will prompt for a location, contact a web service and retrieve JSON for the web service
and parse that data,and retrieve the first place_id from the JSON. 
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

>>>>>>API End Points:
To complete this assignment, you should use this API endpoint that has a static subset of the Google Data: http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like.
If you visit the URL with no parameters, you get "No address..." response.

>>>>>>To call the API:
you need to include a key= parameter and provide the address that you are requesting as the address= parameter
that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above.
You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

>>>>>>Test Data / Sample Execution:
You can test to see if your program is working with a location of "South Federal University"
which will have a place_id of "ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2290 characters
Place id ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ

>>>>>>Turn In:
Please run your program to find the place_id for this location: Old Dominion University

>>>>>>Hint: The first seven characters of the place_id are "ChIJRTm ..."
Make sure to retreive the data from the URL specified above and not the normal Google API.
Your program should work with the Google API - but the place_id may not match for this assignment.
"""
"""
import  ssl
import  json
import urllib.request, urllib.parse, urllib.error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceURL = 'http://py4e-data.dr-chuck.net/json?'

loc = input('Enter Location: ')

url = serviceURL + urllib.parse.urlencode({'loc: loc'})

encodedData = urllib.request.urlopen(url, context = ctx)
decodedData = encodedData.read().decode()

print('Retrieved', len(decodedData), 'characters')

parsedData = json.loads(decodedData)

if not parsedData or 'status' not in parsedData or parsedData['status'] != 'OK':
  print('==== Failure To Retrieve ====')
  print(decodedData)

print(json.dumps(parsedData, indent=4))
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address

    if api_key is not False:
      parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    place_id = js['results'][0]['place_id']
    print('place_id', place_id)























