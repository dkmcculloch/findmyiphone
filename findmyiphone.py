#!/usr/local/bin/python2.7
#####  Written by David McCulloch, Seattle WA dkmcculloch github user    ############
#####  Jan 2016   ######
import os,json,datetime,time
import smtplib
import string, sys
import cgitb
cgitb.enable()
sys.stderr = sys.stdout

print 'Content-Type: text/plain'
print

FROM = "contact@getacert.com"
TO = "xxx@gmail.com"
TOTX = "xxxx@messaging.sprintpcs.com"
SUBJECT = ""
BODY = ""

body = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        BODY), "\r\n")

#print body
#server = smtplib.SMTP()
#server.connect()
#server.sendmail(FROM, TO, body)

homelong=-122.32119346
homelat=47.687311708
homeagainlat=47.688509
homeagainlong=-122.3217604
#-122.322945657
#47.6893560192
#8310 5th Ave NE, Seattle, WA 98115, USA
#Friend
emilyhomelong=-122.323060697
emilyhomelat=47.6893581916
swcarparklat=47.682918
swcarparklong=-122.316805
schoollat=47.6822085539
schoollat2=47.6823844063
schoollong=-122.295388011
schoollong2=-122.29343947
#http://maps.google.com/?q=47.6823844063,-122.29343947
#http://maps.google.com/?q=47.6825629224,-122.294286766
#8309 5th Ave NE, Seattle, WA 98115, USA

skew = 0.0012
skewschool = 0.002
#credsfile = '$(cat data.txt)'
#Credentials to logon is post with json data
david = '$(cat data.txt)'
#credsfile = '$(cat dataemily.txt)'
emily = '$(cat dataemily.txt)'
#credsfile = '$(cat datamsg.txt)'
amber = '$(cat datamsg.txt)'

def opencheckfile(file,status):
   if not os.path.exists(file):
     open(file, 'w').close()

   with open(file) as f:
     line = f.readline()
     if line == status:
        print "Status - " + status + " Unchanged"
        return 0
     else:
        print "Status - " + status + " changed from " + str(line)
        with open(file,'w') as w:
           w.write(status)
           w.close()
        return 1
     

for credsfile in [david, emily, amber]:
#for credsfile in [emily]:
#for credsfile in [amber]:
 CURLFIRST = 'curl -s -k -X POST -c cookies.txt -H "$(cat headers.txt)" -A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko
) Chrome/47.0.2526.80 Safari/537.36" --data-binary "' + credsfile + '" https://setup.icloud.com/setup/ws/1/login?clientBuildNumber=15G.98d4967&client
Id=D9D9E03F-7D13-439D-B0F1-1CCB3A71DEEC'
 result = os.popen(CURLFIRST).read()
 serverfind = json.loads(result)
 URL = serverfind['webservices']['findme']['url']
 #print "CURLFIRST**********************"
 #print serverfind
 #print "CURLFIRST**********************"

 CURLSECOND = 'curl -s -k -X POST -b cookies.txt -H "$(cat headers.txt)" -A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Geck
o) Chrome/47.0.2526.80 Safari/537.36" --data-binary "$(cat data2.txt)" ' + URL + '/fmipservice/client/web/refreshClient?clientBuildNumber=15G78&clien
tId=D9D9E03F-7D13-439D-B0F1-1CCB3A71DEEC&dsid=141259400' 
 result = os.popen(CURLSECOND).read()
 data = json.loads(result)
 #print "******** CURLSECOND content START**********************"
 #print data['content']
 #print "******** CURLSECOND content END**********************"
 for x in range(0, len(data['content'])):
  #print data['content'][x]['id']
  print data['content'][x]['name']
  name = data['content'][x]['name']
  #fixed = name.decode('utf-8')

  #print data['content'][x]['batteryStatus']
  id = data['content'][x]['id']
  postdata = """
{"serverContext":
{"minCallbackIntervalInMS":5000,"prefsUpdateTime":1380344848009,"maxDeviceLoadTime":60000,"classicUser":false,"sessionLifespan":900000,"enableMapStat
s":true,"preferred Language":"en-us","info":"wywMwgE8FCjo2Uqkxjj8+F4gssWb2uNItoe0EQiv+tGBiispOXfYmHURk8q/tikN","isHSA":false,"timezone":{"tzCurrentNa
me":"Pacific Standard Time","previousTransition":1446368399999,"previousOffset":-25200000,"currentOffset":-28800000,"tzName":"US/Pacific"},"cloudUser
":true,"maxLocatingTime":90000,"maxCallbackIntervalInMS":60000,"macCount":0,"enable2FAFamilyActions":false,"minTrackLocThresholdInMts":100,"enable2FA
FamilyRemove":false,"authToken":null,"serverTimestamp":1451509574566,"imageBaseUrl":"https://statici.icloud.com","deviceLoadStatus":"200","clientId":
"Y2xpZW50XzE0MTI1OTQwMF8xNDUxNTA5NTY4MjY1","lastSessionExtensionTime":null,"trackInfoCacheDurationInSecs":86400,"enable2FAErase":false,"callbackInter
valInMS":2000,"validRegion":true,"showSllNow":false,"prsId":141259400,"id":"server_ctx"},"clientContext":{"appName":"iCloud Find (Web)","appVersion":
"2.0","timezone":"US/Pacific","inactiveTime":4866,"apiVersion":"3.0","fmly":true,"shouldLocate":true,"selectedDevice":"%s"}}
""" % (id)
  CURLWAKE = 'curl -s -k -X POST -b cookies.txt -H "$(cat headers.txt)" -A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko
) Chrome/47.0.2526.80 Safari/537.36" -d \'' + postdata + '\' ' + URL + '/fmipservice/client/web/refreshClient?clientBuildNumber=15G78&clientId=D9D9E0
3F-7D13-439D-B0F1-1CCB3A71DEEC&dsid=141259400'
  results = os.popen(CURLWAKE).read()
  time.sleep(4)
  results = os.popen(CURLWAKE).read()
  data = json.loads(results)
  if data['content'][x]['batteryStatus'] != 'Unknown':
   name = data['content'][x]['name'].split()[0][:-1]
   model = data['content'][x]['modelDisplayName']
   print "Getting " + name + " - " + model + " location..."
   time.sleep(1) # Wait for location update for updated location
   bstatus = data['content'][x]['batteryStatus']
   #print bstatus
   blevel = data['content'][x]['batteryLevel']
   #print blevel
   id = data['content'][x]['id']
   if data['content'][x]['location'] :
      CURLFORTH = 'curl -s -k -X POST -b cookies.txt -H "$(cat headers.txt)" -A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like 
Gecko) Chrome/47.0.2526.80 Safari/537.36" -d \'' + postdata + '\' ' + URL + '/fmipservice/client/web/refreshClient?clientBuildNumber=15G78&clientId=D
9D9E03F-7D13-439D-B0F1-1CCB3A71DEEC&dsid=141259400'
      resultwithlocation = os.popen(CURLFORTH).read()
      datawithlocation = json.loads(resultwithlocation)
      timestamp = datawithlocation['content'][x]['location']['timeStamp']
      date = datetime.datetime.fromtimestamp(float(timestamp) / 1000) 
      now = datetime.datetime.now()
      tdelta = now - date

      #print date
      #print tdelta.total_seconds()
      long = datawithlocation['content'][x]['location']['longitude']
      #print long
      lat = datawithlocation['content'][x]['location']['latitude']
      #print lat
      CURLTHIRD = "curl -s " + "http://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(long) + "&sensor=false"
      result2 = os.popen(CURLTHIRD).read()
      data2 = json.loads(result2)
      #print data
      #print(data['results']['address_components'])
      locationdetails = ""
      if tdelta > datetime.timedelta(minutes=1):
         print "old data checked " + str(tdelta) + ' ago'
         locationdetails = "old data checked " + str(tdelta) + ' ago'
      print "-" + name + ' ' + 'phone is ' + bstatus + ' battery at ' + str("{0:.0f}%".format(blevel * 100)) 
      locationdetails += "-" + name + ' ' + 'phone is ' + bstatus + ' battery at ' + str("{0:.0f}%".format(blevel * 100)) 
      print("address " + data2['results'][0]['formatted_address'])
      locationdetails += "\naddress " + data2['results'][0]['formatted_address']
      address = data2['results'][0]['formatted_address']
      print "http://maps.google.com/?q=" + str(lat) + ',' + str(long)
      googlemap = "\n\nhttp://maps.google.com/?q=" + str(lat) + ',' + str(long)
      locationdetails += "\nhttp://maps.google.com/?q=" + str(lat) + ',' + str(long)
      if abs(long-emilyhomelong) < skew:
          print "Emily's house"
          location = "Emily's house"
          #print(round(abs(long-emilyhomelong),7))
          #print(round(abs(lat-emilyhomelat),7))
          #   emilystatus = open('emily.txt', 'r')
      elif abs(long-homelong) < skew and abs(lat-homelat) < skew:
          print "Home"
          location = "Home"
          #print(round(abs(long-homelong),7))
          #print(round(abs(lat-homelat),7))
      elif abs(long-schoollong) < skewschool and abs(lat-schoollat) < skewschool:
          print "School"
          location = "School"
      elif abs(long-schoollong2) < skewschool and abs(lat-schoollat2) < skewschool:
          print "School"
          location = "School"
      elif abs(long-swcarparklong) < skewschool and abs(lat-swcarparklat) < skewschool:
          print "Safeway"
          location = "Safeway"
          #print(round(abs(long-schoollong),7))
      else:
          print "Unknown location "
          location = "Unknown"
      #print(abs(long-homeagainlong))
      #print(abs(lat-homeagainlat))
      outfile = credsfile.split(' ',1)[1].strip(')') + '-' + model + '.out'
      #print outfile
      statuschg = opencheckfile(outfile,location)
      if statuschg:
         print "Alerting"
         battery = str("{0:.0f}%".format(blevel * 100))
         SUBJECT = name + " " + model + "(" + bstatus + "-" + battery + ") " + location
         #BODY = locationdetails
         BODY = address + googlemap + "\n\n" + str(tdelta)
         body = string.join((
           "From: %s" % FROM,
           "To: %s,%s" % (TO,TOTX),
           "%s" % SUBJECT,
           "",
           BODY), "\r\n")
         #print body
         server = smtplib.SMTP()
         server.connect()
         server.sendmail(FROM, TOTX, body)

      print "-----------------------------"
   else:
      print "Need to post device data"
