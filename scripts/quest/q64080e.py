# id 64080 ([MONAD: The First Omen] Night in the Forest), field 867201600
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face1#Back already? ")
sm.setParam(57)
sm.sendSay("#bWow, that's quite a fire you built. ")
sm.setParam(37)
sm.sendSay("#face2#I have you to thank for it. You taught me, after all! ")
sm.setParam(57)
sm.sendSay("#bOh, when we were making soup? Yeah, good point... ")
sm.sendSay("#bWait, your hands are all scratched up! ")
sm.setParam(37)
sm.sendSay("#face1#Well, I never said I was good at it. Don't worry, #h0#. Let's get some rest. ")
sm.setParam(57)
sm.sendSay("#bThanks, Alika. ")
sm.lockInGameUI(True, False)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 25, 0, 0)
sm.sendDelay(1000)
sm.setParam(37)
sm.sendNext("#face3#Uh... is that...? ")
sm.sendSay("#face3#Pete, don't look... ")
sm.completeQuestNoCheck(parentID)
sm.startQuest(64081)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.warp(867201601)