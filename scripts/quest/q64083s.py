# id 64083 ([MONAD: The First Omen] Treacherous Forest Road), field 867201603
sm.lockInGameUI(True, False)
sm.flipNpcByTemplateId(9400580, False)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face0#Shall we head out, then? ")
sm.setParam(57)
sm.sendSay("#bYeah. Let's get going. ")
sm.setParam(37)
sm.sendSay("#face0#Oh, I was thinking... it might be better to leave Pete here. The roads are getting more dangerous, and I'd hate to lose him with monsters around. ")
sm.sendDelay(250)
sm.flipNpcByTemplateId(9400580, True)
sm.sendDelay(250)
sm.flipNpcByTemplateId(9400580, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400580, False, 500, 150)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400595, False, 500, 150)
sm.sendDelay(6000)
sm.flipNpcByTemplateId(9400580, True)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400580, True, 500, 120)
sm.sendDelay(2000)
sm.sendNext("#face1#Let's go! ")
sm.lockInGameUI(False, True)
sm.startQuest(parentID)
sm.createQuestWithQRValue(parentID, "mapIdx=0")
sm.warp(867201700)
