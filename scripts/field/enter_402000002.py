# id 402000002 (Savage Terminal : Old Storage Room), field 402000002
if not sm.hasHadQuest(34603):
    sm.lockInGameUI(True, False)
    sm.removeAdditionalEffect()
    sm.blind(True, 255, 0, 0, 0, 0)
    sm.forcedMove(False, 100)
    sm.sendDelay(1000)
    sm.zoomCamera(0, 2000, 0, -294, 138)
    sm.blind(True, 255, 0, 0, 0, 0)
    sm.sendDelay(1200)
    sm.blind(False, 0, 0, 0, 0, 1000)
    sm.sendDelay(1400)
    sm.setSpeakerType(3)
    sm.setParam(37)
    sm.setColor(1)
    sm.setInnerOverrideSpeakerTemplateID(3001271)
    sm.sendNext("#face1#Hm... No one's back from the mission yet.")
    sm.forcedMove(False, 200)
    sm.zoomCamera(1000, 2000, 1000, -94, 138)
    sm.sendDelay(1800)
    sm.forcedInput(6)
    sm.zoomCamera(500, 2000, 500, 270, 0)
    sm.sendDelay(500)
    sm.setInnerOverrideSpeakerTemplateID(3001250)
    sm.sendNext("#face2#Hey, newbie. Don't fight if there's nothing to gain from it. It's one of our basic rules.")
    sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 0, 0, 0)
    sm.setInnerOverrideSpeakerTemplateID(3001271)
    sm.sendSay("#face0#How would you know if I've been fighting? And what do you care if I fight anyway?")
    sm.forcedInput(0)
    sm.forcedMove(False, 200)
    sm.sendDelay(1800)
    sm.setInnerOverrideSpeakerTemplateID(3001250)
    sm.sendNext("#face2#I care because it affects the whole crew. You're an official branch member now, so you need to start acting like it.")
    sm.setInnerOverrideSpeakerTemplateID(3001271)
    sm.sendSay("#face1#...Fine.")
    sm.showFadeTransition(0, 1000, 3000)
    sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
    sm.moveCamera(True, 0, 0, 0)
    sm.sendDelay(300)
    sm.removeOverlapScreen(1000)
    sm.moveCamera(True, 0, 0, 0)
    sm.lockInGameUI(False, True)
