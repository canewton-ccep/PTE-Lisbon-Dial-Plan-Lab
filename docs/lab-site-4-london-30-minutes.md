# Lab Site 4 – London [ 30 Minutes]

## Overview
!!! info
      This site is similar to Dallas, aside from that this site exists in a different country, so we must cater for entirely different +E.164 dialing habits. This setup of US/UK will not be that common, but the concepts are important and common for sites in Europe where countries are geographically much closer and may share resources. We will need to create a new trunk on our local gateway to cater for the different E.164 dialing habits that this country has; again to allow for granularity of configuration changes. Because of the different country, the reception at this site is also physically located here, however users here still need to be able to dial 0 and hit this localized reception desk instead of the reception at New York. The customer also noted that many staff are mistakenly dialing the reception at New York using its 4-digit extension number that they found on some documentation, so they need to prevent this from occurring.

![London call paths](assets/diagrams/05-london-call-paths.png)

## Configuration Steps

### Add PSTN Numbers

1\. Continuing on Workstation 1, Webex Control Hub. From Control Hub, Navigate to MANAGEMENT > Locations. On the **Locations** page select **London** location.

2\. On London location page, go to **PSTN** tab and click **Configure PSTN Services**.

![](assets/docx-image-224.png)

Now it will give you PSTN configuration options. Click **Manage** for PSTN Configuration > PSTN connection.

![](assets/docx-image-225.png)

3\. It will take you to PSTN Connection Type configuration page, select **Premises-based PSTN** and click **Next**.

![](assets/docx-image-226.png)

4\. On the next page, drop down the option for **Routing Choice** and select **None**. Check mark the option to confirm routing choice changes and click **Next**. We will come back and configure this later!

![](assets/docx-image-227.png)

5\. On the next page, Click **Add Numbers now.** Make sure Location has been selected as **London** and the Number type is selected as **PSTN number** and click **Next**.

6\. On the next page will need to enter the PSTN numbers for the location, minimize the browser (and other applications), and on the desktop of workstation 1, find the TEXT file named **DID\_Numbers\_LON.txt.** It will have some fake DID Numbers pregenerated for you to use in this lab. Select all of them, copy and paste them into **Enter phone numbers** field on Control Hub as shown below. Some Numbers might be marked in Red; this is because that number is either already used or taken by someone else within Webex Calling. You can remove all those numbers marked in Red by clicking the cross button next to them, or by clicking the **Clear Errors** button. Click **Save**.

![](assets/docx-image-228.png)

7\. Click **Close** on the following page and you will be taken to the Numbers page where you can see all the numbers you have just added.

### Assign Main Number

!!! info
      Let's assign a main number to the location. Without this set, Webex Calling will not allow any outgoing calls.

1\. From control hub, navigate to Locations, and choose your **London** location  

![](assets/docx-image-229.png)

2\. Click on the PSTN Tab, and select one of the PSTN numbers you just added & click save. The number will still be available for assignment whatever you wish to use it for!  

![](assets/docx-image-230.png)

### Configure Site Dial Plan Settings

!!! info
      Now we must set our site routing prefix, the trunk for internal calls, and enforce outbound dial digit of 9 just like our previous sites to ensure things work as desired

1\. Go to Locations and choose London location. Under calling tab, click Internal dialing  

![](assets/docx-image-231.png)

2\. and set a site routing prefix of 44. Turn on Calls to on premises extensions and choose the same internal calls route group we set up earlier and save.  

![](assets/docx-image-232.png)

3\. Go back to the calling tab and open the external dialing menu  

![](assets/docx-image-233.png)

4\. Set outbound dial digit of 9 and enforce it. Hit save  

![](assets/docx-image-234.png)

### Assign numbers to users

!!! info
      For this site, our telephony users will be **Stefan Mauk & Ricardo Filice**. We must assign them the +E.164 numbers we just ordered.

1\. Continuing on Workstation 1, Webex Control Hub. Navigate to **MANAGEMENT > Users.** On Users page, choose user **Ricardo Filice**.

2\. On the **Ricardo Filice** user summary page, scroll down a little and click **Edit Licenses**

![](assets/docx-image-235.png)

3\. On Edit services for [rfilice@cbXXX.dc-YY.com](mailto:rfilice@cbXXX.dc-YY.com) page, observe that no “Webex calling professional” license is assigned. Click the **Edit Licenses** button

![](assets/docx-image-236.png)

4\. On the next page, go to **Calling** tab, check mark options for **Webex Calling** and **Professional** and click **Save.**

![](assets/docx-image-237.png)

5\. On the next page, drop down the option for **Location** and choose **London**. Now drop down the option for **Phone Number** and choose any +E.164 phone number. For **Extension** enter last 4 digits of the assigned DID number. Click **Save**. Click **Close**.

![](assets/docx-image-238.png)

6\. Repeat the process again for **Stefan Mauk** with a different number.

7\. Now, go to **SERVICES** > **PSTN & Routing** page. On the **Numbers** page observe that the London extension numbers show with the site routing code of 44.   

![](assets/docx-image-239.png)

### Create PSTN Trunk

!!! info
      This site will access PSTN Via the gateway physically located at New York. For this, we should create an extra trunk for our EU Dial plan PSTN Calls. See the diagram below for the desired end state. Note that in this lab, there is no carrier side PSTN available so calls will not work; but we can still simulate our Webex Calling configuration and see the dial plan working from Webex Calling's perspective, delivering the call request to the gateway; where it will then fail because of a lack of onward PSTN Connection.

![](assets/docx-image-240.png)

!!! important
      There are some scripts that you are about to run, they have similar names but do very different things.  Take care to only run the correct ones, as they add configuration and will cost you time to back out if you run the wrong ones.  Check the name twice before running it!

1\. From the desktop of workstation 1, right click and run the file LTRCOL2006-EU-CL\_Add\_Trunk.ps1 with powershell  

![](assets/docx-image-241.png)

2\. Open control hub, and navigate to PSTN & Routing, Gateway Configurations, Trunk tab. Observe we have a new trunk added named EU\_PSTN  

![](assets/docx-image-242.png)

3\. On the desktop of Workstation 1, open the file **LTRCOL2006_EU_PSTN_LGW_Config-Ready.txt** and copy the contents  

![](assets/docx-image-243.png)

4\. Open Putty and connect to the CUBE GW on 198.18.133.227. The username is admin and the password is dCloud123!  
   Paste the configuration commands in

5\. After 2 minutes, confirm the trunk TLS session with the command  
```
show sip-ua connection tcp tls detail  
```
     
!!! info
      You should see three established TLS connection – One for the internal calls trunk, one for the US PSTN trunk, and one for this trunk. You may also see them registered with a different remote-agent; This is because Webex gives you a SIP registrar physically close to the site you create the trunk from. In this case, we have a European SIP registrar instead of a US One. Note at the bottom, we have this connection on port 5071 and the Internal trunk on port 5070 because of the listen port command assigned to the SIP Tenant.  

![](assets/docx-image-244.png)

6\. Enter the show run command, and hit space bar until you find the section for voice class tenant 400. Observe the command 
```
listen-port secure 5071  
```
     
![](assets/docx-image-245.png)

7\. Now issue the following command, and check the registration is shown as yes for both trunks  
```
show sip-ua register status  
```
     
![](assets/docx-image-246.png)

### Assign PSTN Trunk as site PSTN Connection

1\. Open your London location in control hub and go to the PSTN Tab  

![](assets/docx-image-247.png)

2\. Manage the PSTN connection and change the routing choice to EU\_PSTN. We would normally recommend a route group here, but we are low on time!

3\. Tick the confirmation box and hit next  

![](assets/docx-image-248.png)

4\. Choose done (Add numbers later)  

![](assets/docx-image-249.png)

### Configure Reception Virtual Line

!!! info
      The London site has its own physical reception that will be serviced by Stefan Mauk.

1\. Click the Calling menu and select the Virtual Lines tab. Click the manage button, and add a new one  

![](assets/docx-image-250.png)

2\. Create a new line with the first name of London, last name of Reception, Location of London and choose any available number. Give it a 4 digit extension that matches the last 4 digits of the +E.164 number. Click the add button once complete  
!!! important
      Make a note of the extension number, you will need it later!

![](assets/docx-image-251.png)

3\. Choose Assign on the next screen to associate the line with a user  

![](assets/docx-image-252.png)

4\. Click the Assign Device button and choose Stefan Mauk. Save the configuration by clicking the Assign button  

![](assets/docx-image-253.png)

5\. Observe the options on the next screen to configure the line layout and call decline policy. Finalize with the save button  

![](assets/docx-image-254.png)

### 0 For Local Reception

!!! challenge
      Users wish to be able to dial 0 for a local reception desk. Let's configure that now using a translation pattern.

1\. Go to the PSTN & Routing page, then select Gateway Configurations and Translation Pattern tab  

![](assets/docx-image-255.png)

2\. Click the button to create a new translation pattern  

![](assets/docx-image-256.png)

3\. Create the translation pattern using the following settings, ensuring you adjust the replacement pattern for your own use.  Click **Create** when you have filled the configuration out.  **We recommend you always configure patterns to match the dialled digits closely, but we wanted to have you configure a broad X pattern here to show how this pattern matching principle works in the opposite way to UCM.**
!!! curious
      This is a location specific translation pattern, which means that org level translation patterns will not be considered as long as there is a location level match; **even if the org level match is more specific**. We are using an X as the match pattern here to demonstrate this principle. **Any single digit will match and be routed to reception.**
      In the UCM days, we would likely hit the more specific “0” Match pattern at the global level.
      
      **This is not so in Webex Calling!**
      
      0 counts as more specific than X, only at a given level. So, at the location level, with a 0 & and X pattern, 0 would win. However, if 0 is at the org level, and X is at the location level (As it is in our configuration here) dialing 0 would select the X pattern at the location level.
      
      This is what this excercise is designed to teach you.

![](assets/docx-image-257.png)

### Re-Route calls for New York Reception

!!! challenge
      This customer notes that users at London are mistakenly calling the 6 digit extension number for the New York reception as it was published on some internal documentation. The best solution is to add a translation pattern to redirect the calls to another destination. In this case, we will redirect calls made by London users to the New York reception, back to the London reception. Note we could also redirect calls to another user, or a number that doesn't exist to effectively block the call. You could also use outgoing call permission by digit pattern to simply block the call.

1\. Go to PSTN & Routing, Gateway Configurations and then Translation Patterns. Click the button to add a new one.  

![](assets/docx-image-258.png)

2\. Add the following translation pattern, remember to substitute in your numbers for the New York and London reception virtual lines that you made a note of earlier!

![](assets/docx-image-259.png)

## Test Calls

### Outbound PSTN Calls

1\. Open workstation 4 from dCloud  

![](assets/docx-image-260.png)

2\. Sign in to Webex as Stefan Mauk smauk@cbXXX.dc-xx.com

3\. Open the local gateway via Putty and log in. The IP is 198.18.133.227 username admin password dCloud123!  
   Issue the show run command and scroll using space bar until you see the configuration that looks something like the below. The red part will change in your deployment. This command identifies the trunk we configured earlier.  

<pre><code>
voice class uri 401 sip  
pattern dtg=<text style="color:red;">eu.pstn1451286379.lgu</text>
</code></pre>

![](assets/docx-image-261.png)

4\. Now find the configuration that looks like this. This command associates the trunk identifier above with this dial peer – so it gets selected as the incoming dial peer when we receive a call from Webex destined for the PSTN.  
<pre><code>
dial-peer voice 401 voip
description Inbound/Outbound Webex Calling
max-conn 250
destination-pattern BAD.BAD
session protocol sipv2
session target sip-server
destination dpg 400
<text style="color:red;">incoming uri request 401</text>
voice-class codec 99
voice-class stun-usage 200
no voice-class sip localhost
voice-class sip tenant 400
dtmf-relay rtp-nte
srtp
no vad  
</code></pre>

![](assets/docx-image-262.png)

5\. Issue the command  
```
debug ccsip messages  
terminal monitor
```

6\. Make a call from Stefan's Webex Client to Cisco TAC +448004047778. **There is no EU PSTN in this lab so the call will fail.** You should still see debug messages on the gateway however. Take a look for the Received SIP Message – Note the dtg that matches the voice class we looked at above! This corresponds to the dial peer incoming URI statement. This is how CUBE identifies the dial peer to receive the call on. If you want to go deeper on this, check the bonus content we will share with you; but we recommend completing the lab fully before you do this due to time constraints.
!!! code
      <b>
      
      ```
      Received:
      INVITE sip:+448004047778@198.18.1.227:5071;transport=tls;dtg=eu_pstn1451286379_lgu SIP/2.0
      ```
      
      </b>
      
      ```
      Via:SIP/2.0/TLS 170.72.17.213:8934;branch=z9hG4bKBroadworksSSE.-64.100.12.5V18602-0-100-944089769-1779786686885-
      From:"Stefan Mauk"<sip:+442047243054@170.72.17.213;user=phone>;tag=944089769-1779786686885-
      To:<sip:+448004047778@40462196.cisco-bcld.com;user=phone>
      Call-ID:SSE091126885260526667233005@170.72.17.213
      ```

![](assets/docx-image-263.png)

### 0 For Local Reception

!!! challenge
      Here, we will observe users from EU And US both dialling 0 and routing to the correct reception desk for them.

1\. Ensure that Eric Steele is still logged into workstation 2

2\. Open workstation 3, and log Rebekah out by clicking the Avatar and choosing Sign Out  

![](assets/docx-image-264.png)

3\. Sign Ricardo Filice into Workstation 3 using [rfilice@cbXXX.dc-xx.com](mailto:rfilice@cbXXX.dc-xx.com) and password dCloudXXXX! Where XXXX is the last four digits of your session ID.

4\. Dial 0 from Ricardo's Webex Client and observe the call is delivered to London Reception  

![](assets/docx-image-265.png)

5\. Now go back to Workstation 1, Charles Holland. Dial 0 from here, and observe the call is delivered to the New York Reception.   

![](assets/docx-image-266.png)

### Redirection of New York Reception DN

1\. Open control hub and navigate to PSTN & Routing > Numbers. Make a note of your New York Reception extension number.  

![](assets/docx-image-267.png)

2\. Open Workstation 3 and ensure Ricardo Filice is logged in using [rfilice@cbXXX.dc-xx.com](mailto:rfilice@cbXXX.dc-xx.com) and password dCloudXXXX! Where XXXX is the last four digits of your session ID.

3\. Dial the New York Reception six digit extension number and see the call is routed to the London Reception  

![](assets/docx-image-268.png)

# Finish Line!
This concludes the lab activity! We know this was a tough lab with new concepts, so congratulations for reaching the end! This is a brand new session and we would like to improve and repeat it at future events – so please remember to rate the session positively if you enjoyed it; and feel free to give us feedback directly if you have suggestions.

<!-- PLACEHOLDER: replace SLIDO-PLACEHOLDER-REPLACE-ME with the Lisbon PVT Slido event ID (QR code image assets/image-1.png still points to the WebexOne survey) -->
Please fill out the [Slido Survey](https://app.sli.do/event/SLIDO-PLACEHOLDER-REPLACE-ME) to rate the session! It really helps us to plan events and improve our content.  You can also scan the QR code below with your mobile device to fill out the survey on the go!


![alt text](assets/image-1.png)

!!! challenge
      If you still have time, try out the bonus content for extra learning!