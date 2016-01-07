# findmyiphone
Python script to determine current location of any icloud Apple devices using icloud.com and Find My Phone web application, then alert you when changes are detected from specified GPS locations. 
After determining the GPS longitude and latitude it uses a scew value to determine if in range of the specified locations or if it's Unknown. Tested against icloud.com as of Jan 2016. Requires Python 2.7 and curl. 
To use: Edit the credentials json file, data.txt, to logon to icloud.com and change to dataemily.txt. Will loop through all Apple devices returned. Determine your GPS co-ords using google maps and update the homelat, homelong variables in the script, edit the dataemily.txt credential json file and update the TO and mail addresses some you can be notified of changes. If you have multiple apple ID's edit the data.txt and datamsg.txt and the for loop for two additional Apple ID's to use.
