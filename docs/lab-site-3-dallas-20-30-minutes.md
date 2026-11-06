# Lab Site 3 – Dallas [20-30 Minutes]

## 3.1 Overview {: #overview }

!!! info
      This site is similar again to New York, aside from that PSTN here is accessed via the centralized SBC at New York. Because this site is in the same country as Site 2 – the PSTN dial plan is the same. Users at this site need to dial 0 for a reception desk but be connected to the reception at site 2. We already created an Org-wide Translation for this purpose, so no changes are necessary there. The customer also wishes that this site should have some restrictions around dialling 800 numbers. We can use outbound calling permissions for this purpose.

![Dallas call paths](assets/diagrams/04-dallas-call-paths.png)

## 3.2 Configuration Steps {: #configuration-steps }

### 3.2.1 Add PSTN Numbers {: #add-pstn-numbers }

1\. Continuing on Workstation 1, Webex Control Hub. From Control Hub, Navigate to MANAGEMENT > Locations. On the **Locations** page select **Dallas** location.

2\. On Dallas location page, go to **PSTN** tab and click **Configure PSTN Services**.

![](assets/docx-image-181.png)

Now it will give you PSTN configuration options. Click **Manage** for PSTN Configuration > PSTN connection.

![](assets/docx-image-182.png)

3\. It will take you to PSTN Connection Type configuration page, select **Premises-based PSTN** and click **Next**.

![](assets/docx-image-183.png)

4\. We didn’t create the PSTN trunk yet, so on the next page, drop down the option for **Routing Choice** and select **None**. Check mark the option to confirm routing choice changes and click **Next**. We will come back and configure this later!

![](assets/docx-image-184.png)

5\. Keep all default values for the **Emergency Services Address** and click **Save**. If prompted, click **Apply** for **Suggested Address** pop-up window and click **Save** again.

6\. On the next page, Click **Add Numbers now.** Make sure Location has been selected as **Dallas** and the Number type is selected as **PSTN number** and click **Next**.

7\. On the next page will need to enter the PSTN numbers for the location, minimize the browser (and other applications), and on the desktop find the TEXT file named **DID\_Numbers.txt.** 
!!! important
      Be careful not to open the file DID\_Numbers\_LON.txt!
 It will have some DID Numbers (Fake) pregenerated for you to use in this lab. Select all of them, copy and paste them into **Enter phone numbers** field on Control Hub as shown below. Some Numbers might be marked in Red; this is because that number is either already used or taken by someone else within Webex Calling. You can remove all those numbers marked in Red by clicking the cross button next to them, or by clicking the **Clear Errors** button. Click **Save**.

![](assets/docx-image-185.png)

8\. Click **Close** on the following page and you will be taken to the Numbers page where you can see all the numbers you have just added.

### 3.2.2 Assign Main Number {: #assign-main-number }

1\. Continuing on Workstation 1, Webex Control Hub. Navigate to **MANAGEMENT** > **Locations**. On the locations page, choose **Dallas** location.   

![](assets/docx-image-186.png)

2\. On **Dallas** location page go to **PSTN** tab. On **PSTN** page, drop down the option for **Main number** and choose any of the available numbers. Click **Save**. The number will still be available for assignment whatever you wish to use it for!

![](assets/docx-image-187.png)

3\. Observe that as soon as you **Save** the **Main number** assignment, the warning will disappear, indicating now your location can make and receive calls.

### 3.2.3 Configure Site Dial Plan Settings {: #configure-site-dial-plan-settings }

!!! info
      Now we must set our site routing prefix, the trunk for internal calls, and enforce outbound dial digit of 9 just like our previous sites to ensure things work as desired

1\. Go to Locations and choose Dallas location. Under calling tab, click Internal dialing  

![](assets/docx-image-188.png)

2\. Set a site routing prefix of 45; Turn on Calls to on premises extensions and choose the same internal calls trunk we set up earlier  

![](assets/docx-image-189.png)

3\. Go back to the calling tab and open the external dialing menu  

![](assets/docx-image-190.png)

4\. Set outbound dial digit of 9 and enforce it. Hit save  

![](assets/docx-image-191.png)

### 3.2.4 Assign numbers to users {: #assign-numbers-to-users }

!!! info
      For this site, our telephony users will be **Rebekah Barretta**. We must assign them the +E.164 numbers we just ordered.

1\. Continuing on Workstation 1, Webex Control Hub. Navigate to **MANAGEMENT > Users.** On Users page, choose user **Rebekah Barretta**.

2\. On the **Rebekah Barretta** user summary page, scroll down a little and click **Edit Licenses**

![](assets/docx-image-192.png)

3\. On Edit services for [rbarretta@cbXXX.dc-YY.com](mailto:rbarretta@cbXXX.dc-YY.com) page, observe that no “Webex calling professional” license is assigned. Click the **Edit Licenses** button

![](assets/docx-image-193.png)

4\. On the next page, go to **Calling** tab, check mark options for **Webex Calling** and **Professional** and click **Save.**

![](assets/docx-image-194.png)

5\. On the next page, drop down the option for **Location** and choose **Dallas**. Now drop down the option for **Phone Number** and choose any +E.164 phone number other than the one assigned to location Main number. For **Extension** enter last 4 digits of the assigned DID number. Click **Save**. Click **Close**.

![](assets/docx-image-195.png)

6\. Now, go to **SERVICES** > **PSTN & Routing** page. On the **Numbers** page observe that the Dallas extension numbers show with the site routing code of 45.   

![](assets/docx-image-196.png)

### 3.2.5 Create PSTN Trunk {: #create-pstn-trunk }

!!! info
      This site will access PSTN Via the gateway physically located at New York. For this, we should create an extra trunk for our US Dial plan PSTN Calls. See the diagram below for the desired end state. We already configured our trunk for internal calls; Now we will configure a different trunk to use for PSTN calls. We will keep them separate in this deployment to allow for configuration granularity. We want to retain the ability to change settings on the PSTN Trunk for Dallas without potentially affecting internal calls for all users!

![](assets/docx-image-197.png)

!!! important
      There are some scripts that you are about to run, they have similar names but do very different things.  Take care to only run the correct ones, as they add configuration and will cost you time to back out if you run the wrong ones.  Check the name twice before running it!

1\. From the desktop of workstation 1, right click and run the file **LTRCOL2006-CL\_Add\_Trunk.ps1** with powershell. This will create a trunk in control hub for you, and place a configuration file on the desktop  

![](assets/docx-image-198.png)

2\. Open control hub, and navigate to PSTN & Routing, Gateway Configurations, Trunk tab. Observe we have a new trunk added named US\_PSTN  

![](assets/docx-image-199.png)

3\. On the desktop of Workstation 1, open the file LTRCOL2006\_PSTN\_LGW\_Config-Ready.txt and copy the contents  

![](assets/docx-image-200.png)

4\. Open Putty and connect to the CUBE GW on 198.18.133.227. The username is admin and the password is dCloud123!  
   Paste the configuration commands in  

![](assets/docx-image-201.png)

5\. After 2 minutes, confirm the trunk TLS session with the command  
```
show sip-ua connection tcp tls detail  
```
     
   You should see two established TLS connection – one for the previous trunk, and one for the new one.
!!! note
      Note at the bottom, we have this connection on port 5061 and the Internal trunk on port 5070 because of the listen port command assigned to the SIP Tenant. It is important to configure this when we have multiple trunks!  

![](assets/docx-image-202.png)

6\. Enter the show run command, and hit space bar until you find the section for voice class tenant 300. Observe the command

```
listen-port secure 5070  
```

![](assets/docx-image-203.png)

7\. Now issue the following command, and check the registration is shown as yes for both trunks  
```
show sip-ua register status
```

![](assets/docx-image-204.png)

### 3.2.6 Assign PSTN Trunk as site PSTN Connection {: #assign-pstn-trunk-as-site-pstn-connection }

1\. Open your Dallas location in control hub and go to the PSTN Tab. Click Manage next to the PSTN Connection  

![](assets/docx-image-205.png)

2\. Change the routing choice to US\_PSTN. We would normally recommend a route group here, but we are low on time!

3\. Tick the confirmation box and hit save  

![](assets/docx-image-206.png)

4\. Choose done (Add numbers later)

### 3.2.7 Outbound Calling Permissions by Digit Pattern {: #outbound-calling-permissions-by-digit-pattern }

!!! challenge
      The customer wants to block all calls from this site to 1-800 numbers, except for Cisco TAC. We can do this using the **outbound calling permissions by digit pattern** functionality.

1\. From Control Hub, go to locations, and select your Dallas location.  
     
![](assets/docx-image-207.png)

2\. Choose calling, then outgoing calling permissions and finally permissions by digit pattern.  

![](assets/docx-image-208.png)

3\. Click to add a digit pattern.  

![](assets/docx-image-209.png)

4\. Add two patterns as follows, one to block +1800! And one to allow +18005532447 for TAC. Ensure you mouse over the pattern information tooltip to see the valid methods of digit classification (!, X and [] notation) and understand the Allow transfers/forwards option  
     
![](assets/docx-image-210.png) 
![](assets/docx-image-211.png)

5\. Next, go to PSTN & Routing, Gateway Configurations, Verify Call Routing to test. Use Rebekah as the source user, and input a call destination of +18005532447. Observe that the call shows as routing to an external number, and you get details of the US\_PSTN Trunk and the outgoing call permissions affecting it.   

![](assets/docx-image-212.png)

6\. Now change the number to +18005532446 (The last digit changes to 6) and test again. Observe the call rejection and the relevant details are displayed.  

![](assets/docx-image-213.png)

7\. Now change the source user to a user at another site. Observe the call is permitted no matter what, because the block patterns we added are to the Dallas site only.  

![](assets/docx-image-214.png)

8\. Now navigate to Users, open Rebekah and navigate to Calling tab. Click Outgoing call permissionas, and permissions by digit pattern  

![](assets/docx-image-215.png)

9\. Rebekah is a site manager at this site, and needs to be able to dial a certain subset of 1-800-999 numbers. Read and understand the note about which settings are used, and then click Add digit pattern  

![](assets/docx-image-216.png)

10\. Add a pattern to allow +1800999 numbers as follows  

![](assets/docx-image-217.png)

11\. Open PSTN & Routing, Gateway Configurations and choose Verify call routing. Enter Rebekah as the source, and the destination of +18009992354 or any other 1800999 number. Observe this call is now allowed, because of user level outgoing call permissions we just applied  

![](assets/docx-image-218.png)

## 3.3 Test Calls {: #test-calls }

### 3.3.1 Outbound PSTN Calls {: #outbound-pstn-calls }

1\. Go to workstation 3, and sign out Kellie Melby from Webex

2\. Sign in as Rebekah Barretta [rbarretta@cbXXX.dc-xx.com](mailto:rbarretta@cbXXX.dc-xx.com) with the relevant password from the session info file

3\. Open the local gateway via Putty and log in. The IP is 198.18.133.227 username admin password dCloud123!  
   Issue the show run command and scroll using space bar until you see the configuration that looks something like the below. The red part will change in your deployment. This command identifies the trunk we configured earlier.  
```  
voice class uri 201 sip
pattern dtg=us.pstn0710039444.lgu
```
  
![](assets/docx-image-219.png)

4\. Now find the configuration that looks like this. This command associates the trunk identifier above with this dial peer – so it gets selected as the incoming dial peer when we receive a call from Webex destined for the PSTN.  

<pre><code>
dial-peer voice 201 voip
description Inbound/Outbound Webex Calling
translation-profile outgoing Inbound\_Call
max-conn 250
destination-pattern BAD.BAD
session protocol sipv2
session target sip-server
destination dpg 100
<text style="color:red;">incoming uri request 201</text>
voice-class codec 99
voice-class stun-usage 200
no voice-class sip localhost
voice-class sip tenant 200
dtmf-relay rtp-nte
srtp
no vad  
</code></pre>
![](assets/docx-image-220.png)

5\. Press q to exit the config display mode, and Issue the commands below. Press enter after each one.  
```
debug ccsip messages  
terminal monitor
```

6\. Make a call from Rebekah’s Webex Client to Cisco TAC +18005532447. Take a look on your local gateway for the Received SIP Message – Note the dtg that matches the voice class we looked at above! This corresponds to the dial peer incoming URI statement. This is how CUBE identifies the dial peer to receive the call on. If you want to go deeper on this, check the bonus content we will share with you; but we recommend completing the lab fully before you do this due to time constraints.  

!!! code
      <b>
      
      ```
      Received:
      INVITE sip:+18005532447@198.18.1.227:5061;transport=tls;dtg=us_pstn1772527955_lgu SIP/2.0
      ```
      
      </b>
      
      ```
      Via:SIP/2.0/TLS 144.196.250.30:8934;branch=z9hG4bKBroadworksSSE.-64.100.12.6V1314-0-100-482438161-1777719090043-
      From:"Rebekah Barretta"<sip:+15269457852@144.196.250.30;user=phone>;tag=482438161-1777719090043-
      To:<sip:+18005532447@40462196.cisco-bcld.com;user=phone>  
      ```


![](assets/docx-image-221.png)

7\. Now make a call to +18005532445. Note that you hear a system message stating “You are not able to make this call” and nothing appears on the local gateway; This is because Webex calling blocks the calls due to policy before forwarding to the PSTN. Be aware of this when troubleshooting call failures with Webex Calling, sometimes the cause can be at the Webex Calling level, and sometimes at the Local Gateway – Use verify call routing to know where to troubleshoot!

### 3.3.2 Dial 0 for Webex Calling Reception {: #dial-0-for-webex-calling-reception }

!!! challenge
      Now let’s test our 0 for reception pattern. Dial 0 from Rebekah’s Webex client and note the call gets delivered to Eric Steeles Webex client. I lied earlier! There are two sections in this lab with only a single step. Next time you test 0 for reception, we won’t be so lucky!

![](assets/docx-image-222.png)

### 3.3.3 Webex Calling To UCM Calls {: #webex-calling-to-ucm-calls }

You can feel free to test dialing from Rebekah to Taylor Bard on UCM. DN 6026 or +E1.64 +12943216026. All the configuration is already in place to support these dialing habits!