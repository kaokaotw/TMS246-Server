# id 402090013 (null), field 402090013
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.hideUser(True)
sm.changeBGM("Bgm48.img/Memory", 0, 0)
sm.zoomCamera(0, 1000, 0, 652, 55)
sm.setMapTaggedObjectVisible("core1", True, 0, 0)
sm.setMapTaggedObjectVisible("core2", True, 0, 0)
sm.setMapTaggedObjectVisible("core3", True, 0, 0)
sm.setMapTaggedObjectVisible("coreEff", False, 0, 0)
sm.spawnNpc(3001510, 450, 90)
sm.showNpcSpecialActionByTemplateId(3001510, "summon", 0)
sm.spawnNpc(3001514, 350, 90)
sm.showNpcSpecialActionByTemplateId(3001514, "summon", 0)
sm.spawnNpc(3001515, 270, 90)
sm.showNpcSpecialActionByTemplateId(3001515, "summon", 0)
sm.spawnNpc(3001516, 210, 90)
sm.showNpcSpecialActionByTemplateId(3001516, "summon", 0)
sm.spawnNpc(3001508, 850, 90)
sm.showNpcSpecialActionByTemplateId(3001508, "summon", 0)
sm.spawnNpc(3001517, 950, 90)
sm.showNpcSpecialActionByTemplateId(3001517, "summon", 0)
sm.spawnNpc(3001518, 1150, 90)
sm.showNpcSpecialActionByTemplateId(3001518, "summon", 0)
sm.spawnNpc(3001519, 1000, 90)
sm.showNpcSpecialActionByTemplateId(3001519, "summon", 0)
sm.spawnNpc(3001520, 1050, 90)
sm.showNpcSpecialActionByTemplateId(3001520, "summon", 0)
sm.spawnNpc(3001521, 60, 90)
sm.showNpcSpecialActionByTemplateId(3001521, "summon", 0)
sm.spawnNpc(3001522, 1220, 90)
sm.showNpcSpecialActionByTemplateId(3001522, "summon", 0)
sm.spawnNpc(3001511, 740, 90)
sm.showNpcSpecialActionByTemplateId(3001511, "summon", 0)
sm.sendDelay(1000)
sm.sendDelay(4000)
sm.createFieldTextEffect("#fnﾳﾪﾴﾮﾰ￭ﾵ￱ ExtraBold##fs18#Meanwhile, Caravan Refuge", 100, 1000, 6, -50, -50, 1, 4, 0, 0, 0)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3001510) # Ferret
sm.sendNext("#face2#I've lost contact with the recovery team. They're in danger.")
sm.sendSay("#face2#And the signal from the monsters is getting stronger!")
sm.setInnerOverrideSpeakerTemplateID(3001508) # Zippy
sm.sendSay("#face3#If we're lucky, the monsters won't make it to this crystal before we can get out of here. But we have to hurry.")
sm.setInnerOverrideSpeakerTemplateID(3001510) # Ferret
sm.sendSay("#face0#Yes. You're right. I'll get it ready.")
sm.moveNpcByTemplateId(3001510, False, 150, 180)
sm.sendDelay(2500)
sm.setMapTaggedObjectVisible("coreEff", True, 0, 0)
sm.sendDelay(3500)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.zoomCamera(0, 1000, 0, 652, 55)
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(3001508) # Zippy
sm.sendNext("#face2#Ark hasn't told us how it works, though.")
sm.setInnerOverrideSpeakerTemplateID(3001509) # Salvo
sm.sendSay("#face0#Trust your heart and your instincts.")
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(3001508) # Zippy
sm.sendNext("#face2#Yeah... okay... We can do this.")
sm.sendSay("#face2#Take us to our friends!")
sm.sendDelay(500)
sm.zoomCamera(3000, 2000, 3000, 652, -700)
sm.sendDelay(1000)
sm.blind(True, 255, 0, 0, 0, 1300)
sm.sendDelay(2000)
sm.sayMonologue("#fnArial##fs22#I learned something.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/1", 100)
sm.sayMonologue("#fnﾳﾪﾴﾮﾰ￭ﾵ￱##fs22#When you feel powerless,", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/2", 100)
sm.sayMonologue("#fnArial##fs22#You lose sight of what really matters.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/3", 100)
sm.sayMonologue("#fnArial##fs22#\r\nThe night I decided to leave...", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/4", 100)
sm.sayMonologue("#fnArial##fs22#Maybe I should have talked to you first.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/5", 100)
sm.sayMonologue("#fnArial##fs22#But I didn't know how to explain.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/6", 100)
sm.sayMonologue("#fnArial##fs22#If I had convinced you to join me, maybe our lives would have turned out differently.", 1)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/7", 100)
sm.sayMonologue("#fnArial##fs22#I feel so much regret over that.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/8", 100)
sm.sayMonologue("#fnArial##fs22#And no matter how hard I try to forgive myself...", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/9", 100)
sm.sayMonologue("#fnArial##fs22#That pain is always there, haunting me.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/10", 100)
sm.sayMonologue("#fnArial##fs22#\r\n\r\n'I'll protect you too.'", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/11", 100)
sm.sayMonologue("#fnArial##fs22#As you disappear into the sandstorm...", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/12", 100)
sm.sayMonologue("#fnArial##fs22#\r\n\r\n\r\nI remember that one promise.", 1)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/E/Male/13", 100)
sm.sendDelay(2000)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.hideUser(False)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.warp(402000402)
