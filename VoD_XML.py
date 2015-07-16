#!/usr/bin/python
import hashlib
import os
import glob
import random

# get Main Asset file name
for mainAssetFile in glob.glob('*main*'):

# get Main Asset file MD5 Checksum
    hasher2 = hashlib.md5()
    with open(mainAssetFile, 'rb') as afile2:
        buf2 = afile2.read()
        hasher2.update(buf2)
mainAssetCheckSum = (hasher2.hexdigest())

# gets main video asset file size
mainAssetFileSize = os.path.getsize(mainAssetFile)

#get preview Asset file name
for previewAssetFile in glob.glob('*preview*'):
# get preview asset MD5 Checksum
    hasher = hashlib.md5()
    with open(previewAssetFile, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
previewAssetCheckSum = (hasher.hexdigest())

# gets main video asset file size
previewAssetFileSize = os.path.getsize(previewAssetFile)

# get preview Asset file name
for posterAssetFile in glob.glob('*poster*'):
# get poster asset MD5 Checksum
    hasher3 = hashlib.md5()
    with open(posterAssetFile, 'rb') as afile3:
        buf3 = afile3.read()
        hasher3.update(buf3)
posterAssetCheckSum = (hasher3.hexdigest())

#get Poster asset file size
posterAssetFileSize = os.path.getsize(posterAssetFile)

#gets videoPackage, Summary, RuningTime, AssetID info from txt file
for summaryFile in glob.glob('*.txt'):
    fin=open(summaryFile)
    l1SummaryFile = fin.readline()
    l2SummaryFile = fin.readline()
    l3SummaryFile = fin.readline()
# removes the line description
videoPackage1 = l1SummaryFile.replace("#MODULE-NAME: ", "");
summary1 = l2SummaryFile.replace("#MODULE-SUMMARY: ", "");
runningTime1 = l3SummaryFile.replace("#MODULE-RUNTIME: ", "");

# removes carriage return from read line
videoPackage = videoPackage1.rstrip('\n')
summary = summary1.rstrip('\n')
runningTime = runningTime1.rstrip('\n')

assetID  = random.randrange(1000000000000000,9999999999999999)
assetID2 = assetID+1
assetID3 = assetID+2
assetID4 = assetID+3
assetID5 = assetID+4

videoPackageXML = videoPackage.rstrip('\n') + ".xml"

f = open(videoPackageXML,"a") #creates and writes to xml file
f.write('<?xml version="1.0" encoding="ISO-8859-1"?> \n'
'<!DOCTYPE ADI SYSTEM "ADI.DTD"> \n'
'\n'
'<ADI> \n'
'<Metadata> \n'
'<AMS Asset_Name="' + mainAssetFile + '" Provider="MS_Communications" Product="MOD" Version_Major="1" Version_Minor="0" Description="' + mainAssetFile + ' asset package" Creation_Date="2014-06-01" Provider_ID="m2s2.com" Asset_ID="UNVA' + str(assetID) + '" Asset_Class="package"  /> \n'
'    <App_Data App="MOD" Name="Metadata_Spec_Version" Value="CableLabsVOD1.1" /> \n'
'    <App_Data App="MOD" Name="Provider_Content_Tier" Value="LOCAL_NEWREL_CONTENT" /> \n'
'</Metadata> \n'
'\n'
'<Asset> \n'
'<Metadata> \n'
'<AMS Asset_Name="' + videoPackage + '" Provider="MS_Communications" Product="MOD" Version_Major="1" Version_Minor="0" Description="' + videoPackage + '" Creation_Date="2014-07-01" Provider_ID="m2s2.com" Asset_ID="UNVA' + str(assetID2) + '" Asset_Class="title" /> \n'
'<App_Data App="MOD" Name="Title" Value="Introduction" /> \n'
'<App_Data App="MOD" Name="Title_Brief" Value="Introduction" /> \n'
'<App_Data App="MOD" Name="Closed_Captioning" Value="N" /> \n'
'<App_Data App="MOD" Name="Summary_Short" Value="' + summary +'" /> \n'
'<App_Data App="MOD" Name="Summary" Value="' + summary +'" /> \n'
'<App_Data App="MOD" Name="Rating" Value="NR" /> \n'
'<App_Data App="MOD" Name="Display_Run_Time" Value="' + runningTime + '" /> \n'
'<App_Data App="MOD" Name="Run_Time" Value="00:' + runningTime + '" /> \n'
'<App_Data App="MOD" Name="Year" Value="2014" /> \n'
'<App_Date App="MOD" Name="Actors" Value="none" /> \n'
'<App_Data App="MOD" Name="Director" Value="Crawley,Melinda" /> \n'
'<App_Data App="MOD" Name="Studio" Value="MS Communications" /> \n'
'<App_Data App="MOD" Name="Genre" Value="Instructional" /> \n'
'<App_Data App="MOD" Name="Category" Value="Tutorials,New Releases/Movies A to Z" /> \n'
'<App_Data App="MOD" Name="Provider_Asset_ID" Value="40600" /> \n'
'<App_Data App="MOD" Name="Licensing_Window_Start" Value="2014-01-01" /> \n'
'<App_Data App="MOD" Name="Licensing_Window_End" Value="2025-12-31" /> \n'
'<App_Data App="MOD" Name="Contract_Name" Value="Contract Name" /> \n'
'<App_Data App="MOD" Name="Royalty_Percent" Value="0" /> \n'
'<App_Data App="MOD" Name="Royalty_Minimum" Value="0" /> \n'
'<App_Data App="MOD" Name="Royalty_Flat_Rate" Value="0" /> \n'
'<App_Data App="MOD" Name="Box_Office" Value="26" /> \n'
'<App_Data App="MOD" Name="Billing_ID" Value="A35GA" /> \n'
'<App_Data App="MOD" Name="Suggested_Price" Value="0.00" /> \n'
'<App_Data App="MOD" Name="Maximum_Viewing_Length" Value="01:00:00" /> \n'
'<App_Data App="MOD" Name="Type" Value="title" /> \n'
'</Metadata> \n'
'\n'
'<Asset> \n'
'<Metadata> \n'
'<AMS Asset_Name="Minerva_' + videoPackage + '_movie" Provider="MS_Communications" Product="MOD" Version_Major="1" Version_Minor="0" Description="' + videoPackage +' feature asset" Creation_Date="2014-07-01" Provider_ID="m2s2.com" Asset_ID="' + str(assetID3) + '" Asset_Class="movie" /> \n'
'      <App_Data App="MOD" Name="Audio_Type" Value="Stereo" /> \n'
'      <App_Data App="MOD" Name="Type" Value="movie" /> \n'
'      <App_Data App="MOD" Name="Run_Time" Value="00:' + runningTime + '" /> \n'
'      <App_Data App="MOD" Name="Encryption" Value="N" /> \n'
'      <App_Data App="MOD" Name="HDContent" Value="N" /> \n'
'      <App_Data App="MOD" Name="Content_FileSize" Value="' + str(mainAssetFileSize) + '" /> \n'
'      <App_Data App="MOD" Name="Content_CheckSum" Value="' + str(mainAssetCheckSum) + '" /> \n'
'      <App_Data App="MOD" Name="Viewing_Can_Be_Resumed" Value="Y" /> \n'
'</Metadata> \n'
'<Content Value="' + str(mainAssetFileSize) + '" /> \n'
'</Asset> \n'
'\n'
'<Asset> \n'
'	<Metadata> \n'
'<AMS Asset_Name="Minerva_' + videoPackage + '_preview" Provider="MS_Communications" Product="MOD" Version_Major="1" Version_Minor="0" Description="' + videoPackage + ' trailer asset" Creation_Date="2014-07-01" Provider_ID="m2s2.com" Asset_ID="UNVA' + str(assetID4) + '" Asset_Class="preview" /> \n'
'	<App_Data App="MOD" Name="Rating_Type" Value="MPAA" /> \n'
'	<App_Data App="MOD" Name="Rating" Value="NR" /> \n'
'	<App_Data App="MOD" Name="Run_Time" Value="00:00:30" /> \n'
'        <App_Data App="MOD" Name="Type" Value="preview" /> \n'
'        <App_Data App="MOD" Name="Audio_Type" Value="Stereo" /> \n'
'        <App_Data App="MOD" Name="Languages" Value="en" /> \n'
'        <App_Data App="MOD" Name="Content_FileSize" Value="' + str(previewAssetFileSize) + '" /> \n'
'        <App_Data App="MOD" Name="Content_CheckSum" Value="' + str(previewAssetCheckSum) +'" /> \n'
' </Metadata> \n'
'	<Content Value="' + posterAssetFile + '" /> \n'
' </Asset> \n'
'\n'
'<Asset> \n'
'	<Metadata> \n'
'<AMS Asset_Name="' + videoPackage + '_poster" Provider="MS_Communications" Product="MOD" Version_Major="1" Version_Minor="0" Description="' + videoPackage + ' artwork asset" Creation_Date="2014-07-01" Provider_ID="m2s2.com" Asset_ID="UNVA' + str(assetID5) + '" Asset_Class="poster"/> \n'
'        <App_Data App="MOD" Name="Content_FileSize" Value="' + str(posterAssetFileSize) + '" /> \n'
'        <App_Data App="MOD" Name="Content_CheckSum" Value="' + str(posterAssetCheckSum) + '" /> \n'
'        <App_Data App="MOD" Name="Image_Aspect_Ratio" Value="180x280" /> \n'
'        <App_Data App="MOD" Name="Type" Value="poster" /> \n'
'	     </Metadata> \n'
'		<Content Value="' + posterAssetFile + '" /> \n'
'	</Asset>\n'
'</Asset> \n'
'</ADI> '
)
f.close()
