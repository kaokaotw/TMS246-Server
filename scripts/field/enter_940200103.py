# id 940200103 (Hidden Street : Lucid's Dream), field 940200103
sm.lockInGameUI(True, False)
sm.hideUser(True)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003278) # Mercedes
sm.sendNext("Your skills are more than just impressive, they're worthy of commendation. I can't wait to see what you can do with Dual Bowguns.")
sm.sendSay("You've proven my faith in you was not a mistake. I can only imagine how much more amazing you'll be when we next meet...")
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendNext("#face0#I'm so happy, it's like a dream! I don't ever want to wake up... To... wake up...")
sm.blind(True, 255, 0, 0, 0, 250)
sm.sendDelay(250)
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(940200105)
