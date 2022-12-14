# id 867202651 (Abrup Basin : Sunglow Forest), field 867202651
sm.lockInGameUI(True, False)
sm.createQuestWithQRValue(64019, "chk1=1")
sm.spawnNpc(9400590, -300, 130)
sm.showNpcSpecialActionByTemplateId(9400590, "summon", 0)
sm.spawnNpc(9400589, 0, 130)
sm.showNpcSpecialActionByTemplateId(9400589, "summon", 0)
sm.spawnNpc(9400592, 150, 130)
sm.showNpcSpecialActionByTemplateId(9400592, "summon", 0)
sm.spawnNpc(9400596, 350, 130)
sm.showNpcSpecialActionByTemplateId(9400596, "summon", 0)
sm.spawnNpc(9400635, 400, 130)
sm.showNpcSpecialActionByTemplateId(9400635, "summon", 0)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendNext("#face1#Ugh...")
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face1#Gaaah...")
sm.setParam(57)
sm.sendSay("#bPhew... ")
sm.setParam(37)
sm.sendSay("#face1#Uhhhhhh...")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#You... You have the nerve to return here after stealing our food?! ")
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face0#What? What?! Gah, I'm tired, I'm beaten up, and this is how you treat me? ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#...I'm sorry, treated like what, exactly? ")
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face0#Treated! Like! This! I was halfway up the El Nath Mountains when I decided to turn back just for you people! I thought you might need my help! ")
sm.setParam(57)
sm.sendSay("#bThen why did you run off with the food in the first place? ")
sm.setParam(37)
sm.sendSay("#face0#Hey, hey, hey! We... don't need to worry about that right now! You should be nice, or I won't tell you what I saw. ")
sm.sendSay("#face0#I really did come back because I was worried about you guys, you know! ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#I know you too well to believe that, Slaka. Besides, you look as though you've been lost in the woods for days.")
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face0#Well yeah, I was climbing that dangerous mountain! Geez... ")
sm.setParam(57)
sm.sendSay("#bSo what is it that you saw out there? ")
sm.setParam(37)
sm.sendSay("#face0#Up on the mountain like that, I had a good view of the entire Abrup Basin! ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#I should hope so, assuming you really were up the mountain... ")
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face0#Which I was! But while I was there I saw... it was... ")
sm.setParam(57)
sm.sendSay("#bWhat was it? ")
sm.setParam(37)
sm.sendSay("#face0#It was a giant silhouette, and a red snowstorm surrounding it! ")
sm.setParam(57)
sm.sendSay("#b...! ")
sm.setParam(37)
sm.sendSay("#face0#I could see hundreds... no, thousands of monsters spilling out of the snowstorm, too! ")
sm.sendSay("#face0#And they all moved together, making the storm even bigger! ")
sm.sendSay("#face0#That's exactly what happened when Kaptafel was about to be attacked, you know. ")
sm.sendSay("#face0#So yeah... I could have gone straight to El Nath, but you know me. My soft heart told me you guys were in trouble, so I came all the way back down. ")
sm.sendSay("#face0#You need to understand, that red snowstorm is still raging around the forest! ")
sm.sendSay("#face0#They're on the way here... The red snow and that giant shadow! ")
sm.setParam(57)
sm.sendSay("#b(That sounds just like the shadow I saw...) ")
sm.setParam(37)
sm.sendSay("#face0#See? Now, don't you feel bad for treating me like trash? ")
sm.setParam(57)
sm.sendSay("#b(That's a bit much, but still...) ")
sm.sendSay("#bAlright. I trust you, Slaka. Thanks for this valuable information. ")
sm.setParam(37)
sm.sendSay("#face0#Yeah? Am I finally being recognized for my contributions? ")
sm.setParam(57)
sm.sendSay("#bWell, we also can't ignore you stealing our food and abandoning us. ")
sm.setParam(37)
sm.sendSay("#face0#...Really? Well, uh, what's done is done, right? ")
sm.sendSay("#face0#I mean, if you're going to treat me like a thief, then... I could be like Robin Hood! Yeah, that food totally went to some poor folks in need! ")
sm.sendSay("#face0#Yep, poor folks... like me! Then once I was full, I had the energy to come all the way back and help! ...Right? ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#...Let's just put this behind us and move on. If things are really as bad as you say, then we have no time to waste. ")
sm.sendSay("#face0#We should hurry back.")
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400589, False)
sm.sendDelay(250)
sm.flipNpcByTemplateId(9400596, False)
sm.flipNpcByTemplateId(9400635, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400635, False, 300, 100)
sm.moveNpcByTemplateId(9400596, False, 300, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400592, False, 300, 100)
sm.moveNpcByTemplateId(9400589, False, 300, 100)
sm.sendDelay(250)
sm.forcedMove(False, 300)
sm.moveNpcByTemplateId(9400590, False, 300, 100)
sm.sendDelay(3000)
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(64109)
sm.warp(867202304)
