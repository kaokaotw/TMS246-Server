# id 910143000 (null), field 910143000
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.createQuestWithQRValue(37152, "plane=on")
sm.sendDelay(1000)
sm.zoomCamera(0, 1000, 0, -873, 100)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1000)
sm.forcedMove(False, 350)
sm.sendDelay(3000)
sm.setSpeakerType(3)
sm.setParam(5)
sm.setInnerOverrideSpeakerTemplateID(1012110) # Anne
sm.sendNext("It flew over this way, didn't it? Where did my paper airplane land?")
sm.forcedFlip(True)
sm.sendDelay(2000)
sm.sendNext("Oh, it's way over there.")
sm.forcedInput(8)
sm.sendDelay(1000)
sm.forcedMove(True, 600)
sm.sendDelay(6000)
sm.sendNext("I guess I threw it harder than I thought... Ugh, it's really creepy here. Probably full of monsters.")
sm.createQuestWithQRValue(37152, "plane=off")
sm.sendDelay(500)
sm.changeBGM("Bgm00/Silence", 0, 0)
sm.sendDelay(500)
sm.sendDelay(2000)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 0, 0, 0)
sm.sendDelay(2000)
sm.sendNext("Heeey! I know you monsters are listening, but you better not attack me! I'm just here to get my airplane, then I'll be out of your fur... or scales... or whatever...")
sm.sendDelay(500)
sm.forcedFlip(True)
sm.sendDelay(500)
sm.sendDelay(2000)
sm.showEffect("Effect/OnUserEff.img/emotionBalloon/exclamation3", 0, 0, 0, 0, 0, 0, 0)
sm.sendDelay(2000)
sm.sendNext("Ahh! What's that screeching?!")
sm.sendDelay(1000)
sm.zoomCamera(1000, 1000, 1000, -873, 415)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 2000, 0, -873, 530)
sm.sendDelay(1300)
sm.removeOverlapScreen(1000)
sm.sendDelay(3000)
sm.spawnNpc(1501012, -886, 533)
sm.showNpcSpecialActionByTemplateId(1501012, "summon", 0)
sm.sendDelay(2000)
sm.sendNext("Ahhhh! A witch!")
sm.sendDelay(500)
sm.forcedMove(False, 350)
sm.sendDelay(2000)
sm.showEffect("Effect/OnUserEff.img/emotionBalloon/noSpeak", 0, -886, 583, 0, 0, 1, 0)
sm.sendDelay(3000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(500)
sm.sendDelay(500)
sm.sendDelay(1000)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.startQuest(37152)
sm.warp(101000000)
