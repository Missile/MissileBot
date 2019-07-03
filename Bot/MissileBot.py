import time
import praw
import config
import requests

def bot_login():
  print("Logging in")
  time.sleep(1)
  r = praw.Reddit(username = config.username,
      password = config.password,
      client_id = config.client_id,
      client_secret = config.client_secret,
      user_agent = "Autoresponder by /u/Missile1337")
  print("Logged in!")
  time.sleep(1)
  return r

#############################################################################################

#Get Parent
def get_parent(unread_message):
  #Get root submission ID:
  #parentid = unread_message.context.split("/")
  #parentid = parentid[4]

  #Get message parent:
  parentid = unread_message.parent_id
  if(parentid.startswith("t1_")):
    submission = r.comment(id=parentid[3:])
  elif(parentid.startswith("t3_")):
    submission = r.submission(id=parentid[3:])
  else:
    submission = False

  #print("parentid: " + parentid)
  return submission

#############################################################################################

#Messages
def get_message(message, m_body):
  #Check for text in mention
  if("won but demote" in m_body or "wbd" in m_body or "wbd" in m_body):
    message.report("Won but demoted -MissileBot")
    return "Did you win and demote?\n\nThis happens when your client is out of sync with the server. Typically, a desync happens when you leave a game before the scoreboard screen. Do not fear! Everything is synced and correct on the server side. The client will not update the amount of points you lost [or won] until you restart the game or complete another game in the same playlist.\n\nIf you lost the previous game, your next match is usually with players with equal or lower skill ratings resulting in winning less points. You did not gain enough points from the win to even out the points you lost from the previous game. You were on the edge of the division, causing a demotion for winning."
  elif(("phish" in m_body) or ("phished" in m_body) or ("scam" in m_body) or ("scammed" in m_body)):
    return "Please submit a support ticket at https://support.rocketleague.com if you got phishing scammed. \n\n---\n\n###To submit a ticket: \n\n1. Click the **Sign In** link in the top right corner and sign in with your platform. \n2. Click on **Submit a Ticket** in the top right corner. \n3. In the **Issue** dropdown, select **Feedback, bugs and play reports**, and then **Someone took my items**. \n4. Fill out the rest of the form. \n\nIf you get an auto response, make sure to continue to reply. Try to include as much info as you can. \n\n---\n\nBest case scenario, Psyonix will give return your items but trade locked. \n\n**Remember to change your passwords!**"
  elif(("gif" in m_body) or ("highlight" in m_body)):
    return "**The method for recording and posting gameplay highlights depends on your platform.**\n\n&nbsp;\n\n**PC**: \n\nMethod 1: Use https://www.gifyourgame.com/ to automatically create a clip by pressing a single button after the play. \n\nMethod 2: If you want to make a gif from a replay use screen recording software (OBS is a good, free program) to record a clip of the replay. You can then upload the video to https://gfycat.com/upload, then post the gfycat link to the subreddit.\n\n&nbsp;\n\n**PS4**: \n\nMethod 1: Record some videos of the replays with the share function. Use the share factory app to trim/edit replays, then upload the video to youtube from the app. Paste the youtube link to https://gfycat.com/upload, then post the gfycat link to the subreddit. \n\nMethod 2: Record some videos of the replays with the share function. Plug a usb drive into the PS4. Go to your capture gallery and navigate to the videos you wish to send. Press the options button and select something to the effect of “Copy media to mass storage device”. Select the desired videos and wait. The PS4 will make a PS4 folder under which you will have videos and screenshots, then it will be sorted by game. Remove the usb drive after it is done and stick it in your computer. Upload the video from the usb drive to https://gfycat.com/upload, then post the gfycat link to the subreddit. \n\n&nbsp;\n\n**Xbox One**: \n\nMethod 1: https://xbox.streamable.com and http://xboxdvr.com/ Both allow you to browse videos you've uploaded to Xbox Live, use either one of them to create a shareable link you can post in the subreddit. \n\nMethod 2: Upload recordings to your OneDrive from the xbox, then upload the mp4 file to https://gfycat.com/upload and post the gfycat link to the subreddit.\n\n&nbsp;\n\n**Switch**: \n\nOpen the the replay of the play you want to post. Watch the part of the replay you want to record, and after it's done, press and hold the Switch’s capture button — it’s the square button with the indented circle, located under the directional pad on the left Joy-Con, or opposite the home button on the Switch Pro controller. Holding the button automatically records the previous 30 seconds of gameplay. You can then upload the clip to facebook or twitter from the album menu. Paste the facebook/twitter link to http://gfycat.com/upload and post the gfycat link to the subreddit."
  elif(("hour" in m_body) or ("skill" in m_body)):
    return "The number of hours played to reach a rank shouldn't be used as measure of skill. Everyone learns at their own rate. Please watch this explanation by Pro player CJCJ: https://clips.twitch.tv/WonderfulBillowingTomatoBrokeBack"
  elif(("lag" in m_body) or ("network" in m_body)):
    return "#If you experience server issues:\n\nWhen you talk about servers, remember to mention which Region you're playing. For instance it's possible that US-West is down, while everything else works fine.\n\n#Rocket League connection requirements:\n\nRocket League requires precise and consistent information because of fast inter-acting physics. There is nowhere for a bad connection to hide. You need a quality connection without [packetloss](https://en.wikipedia.org/wiki/Packet_loss) or [jitter](https://en.wikipedia.org/wiki/Jitter#Packet_jitter_in_computer_networks). WiFi is the most common reason for bad connections.\n\n[WiFi is bad for gaming](https://www.pcgamer.com/heres-how-playing-on-wi-fi-hurts-your-game/). For all games. Some games types can reduce the effects of a bad connection. But make no mistake, your WiFi is a handicap in those games as well.\n\nUse a [$5 ethernet cable](https://www.google.com/search?q=ethernet+cable+amazon) and you have perfected your home network. For all games.\n\nOn rare occasions it is not possible to get a [cable](https://www.google.com/search?q=ethernet+cable+amazon) from the router to the console/pc. Then [power line adapters](https://www.google.com/search?q=powerline+adapter) are a reasonable alternative. They are much more expensive than a $5 cable, and perform worse. But still much better than WiFi.\n\n#How to test your connection:\n\n- First you need to find a Rocket League server IPs to test. [Wireshark](https://www.wireshark.org/download.html) can do that. Have it running while you play a Casual match to find the server IP.\n\n- If you don't want to install Wireshark, you can open Launch.log located in \Documents\My Games\Rocket League\TAGame\Logs and search for StartJoin and copy the IP that looks something like 212.142.22.23.\n\n- Then you test your connection for that Rocket League server IP using a program like [winmtr](https://sourceforge.net/projects/winmtr). Leave it running for some time and paste the results.\n\n- Rocket League requires less than 1mbit bandwidth. It doesn't matter whether you have 10mbit or 1000mbit. This means bandwidth tests like speedtest.net are near irrelevant when testing a connection quality for gaming. You are also not testing your connection towards a Rocket League server."
  elif(("reward" in m_body) or ("drop" in m_body) or ("fan" in m_body) or ("gg" in m_body)):
    message.report("RLCS Fan Rewards -MissileBot")
    return "**How do I sign up for Fan Rewards?**\n\nVisit [http://rewards.rocketleague.com](http://rewards.rocketleague.com), click the big \"Log in with Twitch\" button to authorize your Twitch account, select the platform of your choice. You can connect all your platform accounts, but only your preferred account will receive the Fan Rewards.\n\n&nbsp;\n\n**How will I get rewards?**\n\nFan Rewards drop at random from watching the live broadcast. **You are NOT GUARANTEED a drop from watching.** Fan Rewards drop at random from watching the live broadcast. You will receive a Twitch notification displaying the item you received. Psyonix will NEVER ask for your login info, email, or password. Having Rocket League open has no affect on the drop rates. Just restart your game when you receive a whisper. Drops may be delayed or there might not be an item notification you when you launch the game (item is already owned).\n\n&nbsp;\n\n**Where do I watch?**\n\nTune in to the official live broadcasts. The device you watch on does not matter as long as you are logged in and considered in the 'Viewer Count'. This includes audio only on the mobile Twitch app. You DO NOT need to be active in chat to be considered a viewer."
  elif(("season reward win" in m_body) or ("srw" in m_body)):
    message.report("Season reward wins -MissileBot")
    return "[Image: Season Reward Level Bar](https://rocketleague.media.zestyio.com/Season-Reward-Level-Bar-2.jpg)\n\nIn the image above, the \"Unranked Season Reward Level\" on the left indicates your current reward level. For instance, if it is on the Gold Season Reward Level, you have unlocked the Bronze, Silver, and Gold rewards for this season.\n\nThe right side indicates the rank you require to progress to the next tier's reward. Wins only count towards your Season Reward by playing at Bronze tier or higher. But a Gold player who has unlocked Gold Season Rewards cannot yet unlock Platinum Season Rewards.\n\nYour Reward Level starts at Unranked, and each win earns you progress towards the next level. Each Reward Level requires 10 wins to unlock, and they are sequential - you unlock Silver rewards after Bronze, Gold after Silver, and so on.\n\n&nbsp;\n\n^(**Can I lose Season Reward Levels if I lose matches or drop a skill tier?**)\n\n^(You will not lose progress towards your season rewards. Losses do not subtract from your win total, and your progress will be stored even if you get demoted.)\n\n^(**How do different playlists interact with the Season Reward Level?**)\n\n^(You can earn wins towards leveling up from any Competitive Playlist. However, you still only earn wins for matches of sufficient rank. If you 2v2 rank is Platinum and your 3v3 rank is Silver, 3v3 wins will only count towards Silver Reward Level and below.)\n\nSource: [Blog](https://www.rocketleague.com/news/changes-competitive-season-5)"
  elif("flair" in m_body):
    message.report("Subreddit flair -MissileBot")
    return "**Official Reddit Mobile App**\n\n* On the subreddit page, select the ellipsis (...) on the top right and tap \"Change user flair\". Select the flair you want. To select an editable text flair, click the edit button on the top right. Team flairs cannot be edited.\n\nor\n\n* Tap your username on a post to open up a hover card. Tap the \"Change flair\" to change your flair on the current subreddit you're browsing. Select the flair you want. To select an editable text flair, click the edit button on the top right. Team flairs cannot be edited.\n\n&nbsp;\n\n**Desktop Site**\n\n* On the right sidebar, there is an \"Edit Flair\" button. This will bring up a menu where you can select your flair. You can only edit the text of competitive rank flairs.\n\nHere is a GIF example: https://gfycat.com/JoyfulQuarterlyGoose\n\n---\n\n**Grand Champ Flair**\n\nYou can request the Grand Champion flair only if you have made GC. Under the subreddit rules, on the sidebar or \"Community Info\" in the official Reddit mobile app, there is a link to the Request GC Flair thread. Read the thread and follow the format."
  elif("bug" in m_body):
    message.report("Known bug post -MissileBot")
    return "This is a known bug and Psyonix is aware of it. It should be fixed in the next patch."

#############################################################################################

#Bot function
def reply_mention(r, comments_replied_to):

  #Get message
  for unread_message in r.inbox.unread(limit=5):
    print(unread_message.subject)
    
    #Mark read
    unread_message.mark_read()

    #If username mention...
    if(unread_message.subject == "username mention"):
      submission = get_parent(unread_message)

      #Bot already posted in submission thread
      if(not submission):
        continue;

      #set author
      ment_author = unread_message.author.name

      #If original post deleted... fixes error when deleted
      if(not submission.author):
        subm_author = '[deleted]'
      else:
        subm_author = submission.author.name

      #Get message
      message = ""
      message = get_message(submission, unread_message.body.lower())

      #Making response
      messageAuth = "\n\n" + invm + "Mentioned " + invm + "by " + invm + "/u/" + ment_author + " " + invm + "for " + invm + "OP, " + invm + "/u/" + subm_author + invm +"."
      message += messageAuth + messageEnd

      if(message != messageAuth+messageEnd):
        submission.reply(message)
        #add to posted
        #comments_replied_to.append(submission.id)
        print("Replied to a post from a mention.")


    #If comment reply...
    elif(unread_message.subject == "comment reply" and (unread_message.author.name == "Missile1337" or unread_message.author.name == "Koponewt")):
      if("delete" in unread_message.body.lower()):
        comment = r.comment(id=unread_message.parent_id[3:])
        comment.delete()

#############################################################################################

#Start of bot
time.sleep(1)
r = bot_login()
comments_replied_to = []
time.sleep(1)
invm = "^^^^^^^^^^^^^^^^"
messageEnd = "\n\n*****\n^[FAQ](/r/MissileBot/wiki/index) &nbsp; ^| &nbsp; ^[Contact](https://www.reddit.com/message/compose?to=Missile1337) &nbsp; ^| &nbsp; ^(Beep. Boop.)"

sleepError = 40
sleepTime = 12

while True:
    try:
        #print("Looking at inbox...")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
        reply_mention(r, comments_replied_to)
        print("Sleeping for " + str(sleepTime) + " seconds...")
        time.sleep(sleepTime)
    except requests.exceptions.ConnectionError:
        print("Connection exception, will retry in " + str(sleepError) + " seconds")
        time.sleep(sleepError)
    except requests.exceptions.ReadTimeout:
        print("Read Timeout exception, will retry in " + str(sleepError) + " seconds")
        time.sleep(sleepError)
    except Exception as e:
        print(e)
        print("Error! Sleeping for " + str(sleepError) + " seconds.")
        time.sleep(sleepError)
