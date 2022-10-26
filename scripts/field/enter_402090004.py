# id 402090004 (null), field 402090004
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.zoomCamera(0, 1000, 0, -1500, -200)
sm.spawnNpc(3001509, -1838, 250)
sm.showNpcSpecialActionByTemplateId(3001509, "summon", 0)
sm.spawnNpc(3001512, -1960, 250)
sm.showNpcSpecialActionByTemplateId(3001512, "summon", 0)
sm.spawnNpc(3001513, -1900, 250)
sm.showNpcSpecialActionByTemplateId(3001513, "summon", 0)
sm.spawnNpc(3001510, -1260, 250)
sm.showNpcSpecialActionByTemplateId(3001510, "summon", 0)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.sendDelay(500)
sm.createFieldTextEffect("#fnﾳﾪﾴﾮﾰ￭ﾵ￱ ExtraBold##fs18#A While Later, Far from the Caravan Refuge", 100, 1000, 6, -50, -50, 1, 4, 0, 0, 0)
sm.zoomCamera(4000, 1000, 4000, -1500, 250)
sm.sendDelay(4000)
sm.zoomCamera(3000, 1000, 3000, -1150, 250)
sm.forcedFlip(True)
sm.moveNpcByTemplateId(3001509, False, 350, 200)
sm.moveNpcByTemplateId(3001512, False, 350, 200)
sm.moveNpcByTemplateId(3001513, False, 350, 200)
sm.moveNpcByTemplateId(3001510, False, 350, 200)
sm.sendDelay(500)
sm.forcedMove(False, 350)
sm.sendDelay(2500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3001512) # Digs
sm.sendNext("#face0#The wind is strange. Are you sure we're headed the right direction?")
sm.sendDelay(500)
sm.playSound("Sound/SoundEff.img/ark/wind", 100)
sm.spineScreen(False, False, True, 0, "Effect/Direction17.img/effect/ark/dust/0/ark_dust","01_dust A","01")
sm.sendDelay(2500)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 868071, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 868073, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 868072, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 868074, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 0, 0, 0)
sm.sendDelay(1000)
sm.playSound("Sound/SoundEff.img/ark/wind", 100)
sm.spineScreen(False, True, True, 0, "Effect/Direction17.img/effect/ark/dust/0/ark_dust","02_dust B","02")
sm.moveNpcByTemplateId(3001509, False, 150, 120)
sm.setInnerOverrideSpeakerTemplateID(3001509) # Salvo
sm.sendNext("#face2#How can we be stuck in a sandstorm?! Ferret, I'm really glad you're so good at this, but... are your signals still working?")
sm.setInnerOverrideSpeakerTemplateID(3001510) # Ferret
sm.sendSay("#face0#...")
sm.zoomCamera(2000, 1000, 2000, -850, 250)
sm.moveNpcByTemplateId(3001512, False, 150, 120)
sm.moveNpcByTemplateId(3001513, False, 150, 120)
sm.playSound("Sound/SoundEff.img/ark/wind", 100)
sm.blind(False, 0, 0, 0, 0, 2000)
sm.sendNext("#face0#This is bad.")
sm.zoomCamera(1000, 1500, 1000, -850, 300)
sm.playSound("Sound/SoundEff.img/ark/wind", 100)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendNext("#face2#The sandstorm is messing with my devices.")
sm.zoomCamera(1000, 2000, 1000, -850, 320)
sm.playSound("Sound/SoundEff.img/ark/wind", 100)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendNext("#face3#I can't get any kind of signal.")
sm.spawnNpc(3001524, -750, 233)
sm.showNpcSpecialActionByTemplateId(3001524, "summon", 0)
sm.spawnNpc(3001524, -700, 233)
sm.showNpcSpecialActionByTemplateId(3001524, "summon", 0)
sm.spawnNpc(3001524, -650, 233)
sm.showNpcSpecialActionByTemplateId(3001524, "summon", 0)
sm.spawnNpc(3001524, -600, 233)
sm.showNpcSpecialActionByTemplateId(3001524, "summon", 0)
sm.spawnNpc(3001524, -560, 233)
sm.showNpcSpecialActionByTemplateId(3001524, "summon", 0)
sm.spawnNpc(3001524, -500, 233)
sm.showNpcSpecialActionByTemplateId(3001524, "summon", 0)
sm.spawnNpc(3001524, -420, 233)
sm.showNpcSpecialActionByTemplateId(3001524, "summon", 0)
sm.spawnNpc(3001524, -300, 233)
sm.showNpcSpecialActionByTemplateId(3001524, "summon", 0)
sm.showNpcSpecialActionByTemplateId(3001524, "attack", -1)
sm.showNpcSpecialActionByTemplateId(3001524, "attack", -1)
sm.showNpcSpecialActionByTemplateId(3001524, "attack", -1)
sm.showNpcSpecialActionByTemplateId(3001524, "attack", -1)
sm.showNpcSpecialActionByTemplateId(3001524, "attack", -1)
sm.showNpcSpecialActionByTemplateId(3001524, "attack", -1)
sm.playSound("Sound/SoundEff.img/ark/wind", 100)
sm.sendDelay(500)
sm.playSound("Sound/SoundEff.img/ark/wind", 100)
sm.forcedMove(False, 150)
sm.zoomCamera(2000, 1000, 2000, -1000, 250)
sm.setInnerOverrideSpeakerTemplateID(3001500) # Ark
sm.sendNext("#face4#That's definitely not good for us.")
sm.sendDelay(2500)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.warp(402000621)
