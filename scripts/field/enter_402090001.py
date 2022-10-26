# id 402090001 (null), field 402090001
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.zoomCamera(0, 1000, 0, -303, -545)
sm.sendDelay(1000)
sm.forcedFlip(True)
sm.sendDelay(2000)
sm.createFieldTextEffect("#fnﾳﾪﾴﾮﾰ￭ﾵ￱ ExtraBold##fs18#Several Days Later, Caravan Refuge Entrance", 100, 2200, 6, -50, -50, 1, 4, 0, 0, 0)
sm.zoomCamera(3000, 1000, 3000, -303, 70)
sm.sendDelay(4000)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3001500) # Ark
sm.sendNext("#face1#Ugh... How long have I been out?")
sm.sendSay("#face1#Why am I in the desert? And... what's wrong with my arm?")
sm.forcedAction(0, 300)
sm.sendDelay(300)
sm.forcedFlip(True)
sm.forcedAction(0, 300)
sm.sendDelay(300)
sm.forcedFlip(True)
sm.forcedAction(0, 300)
sm.sendDelay(300)
sm.forcedFlip(False)
sm.sendNext("#face2#Who tied me up? What do they want?")
sm.sendSay("#face3#Maybe they're not dangerous. Then again, the wounds on my arms look pretty fresh.")
sm.sendSay("#face0#Urgh... At least I'm alive.")
sm.sendSay("#face5#Maybe I can reason with whoever it is.")
sm.forcedFlip(True)
sm.forcedAction(0, 300)
sm.sendDelay(300)
sm.sendNext("#face0#I might be able to cut these ropes, but who knows how much time I've got.")
sm.sendSay("#face3#Looks like about 20 people over there. Too many to fight. I might have to make a run for it.")
sm.sendSay("#face0#...But I suppose I should at least try to talk to them first.")
sm.sendSay("#face2#Ah! Here comes one now.")
sm.spawnNpc(3001509, -1250, 90)
sm.showNpcSpecialActionByTemplateId(3001509, "summon", 0)
sm.sendDelay(1000)
sm.showFadeTransition(0, 300, 300)
sm.sendDelay(300)
sm.removeOverlapScreen(300)
sm.zoomCamera(0, 2000, 0, -1200, 150)
sm.sendDelay(300)
sm.moveNpcByTemplateId(3001509, False, 150, 70)
sm.zoomCamera(3500, 2000, 3500, -950, 150)
sm.setInnerOverrideSpeakerTemplateID(3001509) # Salvo
sm.sendNext("#face2#Boy, I feel like singing at the top of my lungs today!")
sm.sendDelay(3000)
sm.flipNpcByTemplateId(3001509, True)
sm.zoomCamera(5000, 2000, 5000, -730, 150)
sm.moveNpcByTemplateId(3001509, False, 150, 70)
sm.sendNext("#face2#I might just dance too! Fancy feet! Shuffle, shuffle, shuffle! I'm doing it!")
sm.sendDelay(2000)
sm.flipNpcByTemplateId(3001509, True)
sm.moveNpcByTemplateId(3001509, False, 430, 100)
sm.sendNext("#face3#Salvo on duty and doing fine! \r\nMy dance demolition skill's top of the line!")
sm.sendDelay(1500)
sm.sendNext("#face4#Woo! Yeah! Woo, woo! Yea- OH!")
sm.sendDelay(2000)
sm.playSound("Sound/SoundEff.img/Falldown", 100)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284521, 0, 0)
sm.sendDelay(300)
sm.sendDelay(300)
sm.zoomCamera(0, 2000, 0, -430, 150)
sm.flipNpcByTemplateId(3001509, False)
sm.moveNpcByTemplateId(3001509, True, 60, 220)
sm.sendDelay(2000)
sm.sendNext("#face1#The monster's awaaaaake!")
sm.spawnNpc(3001509, -490, 90)
sm.showNpcSpecialActionByTemplateId(3001509, "summon", 0)
sm.sendDelay(1000)
sm.sendDelay(300)
sm.zoomCamera(0, 2000, 0, -450, 150)
sm.spawnNpc(3001508, -185, 76)
sm.showNpcSpecialActionByTemplateId(3001508, "summon", 0)
sm.spawnNpc(3001510, -122, 76)
sm.showNpcSpecialActionByTemplateId(3001510, "summon", 0)
sm.spawnNpc(3001514, -30, 76)
sm.showNpcSpecialActionByTemplateId(3001514, "summon", 0)
sm.spawnNpc(3001515, 10, 127)
sm.showNpcSpecialActionByTemplateId(3001515, "summon", 0)
sm.spawnNpc(3001516, 70, 127)
sm.showNpcSpecialActionByTemplateId(3001516, "summon", 0)
sm.spawnNpc(3001512, -570, 76)
sm.showNpcSpecialActionByTemplateId(3001512, "summon", 0)
sm.spawnNpc(3001513, -620, 76)
sm.showNpcSpecialActionByTemplateId(3001513, "summon", 0)
sm.spawnNpc(3001520, -570, 127)
sm.showNpcSpecialActionByTemplateId(3001520, "summon", 0)
sm.spawnNpc(3001519, -640, 127)
sm.showNpcSpecialActionByTemplateId(3001519, "summon", 0)
sm.spawnNpc(3001517, -670, 76)
sm.showNpcSpecialActionByTemplateId(3001517, "summon", 0)
sm.spawnNpc(3001518, -720, 76)
sm.showNpcSpecialActionByTemplateId(3001518, "summon", 0)
sm.sendDelay(2000)
sm.setInnerOverrideSpeakerTemplateID(3001500) # Ark
sm.sendNext("#face4#You think I'm a monster?")
sm.zoomCamera(1000, 1000, 1000, -300, 70)
sm.sendDelay(1000)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284857, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284858, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284859, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284860, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284861, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284862, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284863, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284864, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284865, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284866, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284867, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 284835, 0, 0)
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(3001510) # Ferret
sm.sendNext("#face2#It can talk? Maybe it's different from the others? But... no... something's not right... Its arm...")
sm.setInnerOverrideSpeakerTemplateID(3001500) # Ark
sm.sendSay("#face4#Please listen. I'm not a monster. I don't want to hurt you. Would you untie me?")
sm.setInnerOverrideSpeakerTemplateID(3001509) # Salvo
sm.sendSay("#face0#That's just what a monster #ewould#n say! Identify yourself if you want to be released! Or... promise to listen to my music. That's okay too.")
sm.sendDelay(1100)
sm.speechBalloon(False, 0, 0, "The face...", 1000, 0, 0, 0, 0, 4, 3001512, 102647)
sm.sendDelay(1100)
sm.speechBalloon(False, 0, 0, "Where are you from?", 1000, 0, 0, 0, 0, 4, 3001514, 102647)
sm.sendDelay(1100)
sm.speechBalloon(False, 0, 0, "What's wrong with your arm?", 1000, 0, 0, 0, 0, 4, 3001513, 102647)
sm.setInnerOverrideSpeakerTemplateID(3001500) # Ark
sm.sendNext("#face3#I... I don't actually know. I don't know who I am either. I wish I could tell you.")
sm.sendSay("#face3#All I can remember is one big nightmare and someone calling me... Ark. I think that's my name.")
sm.setInnerOverrideSpeakerTemplateID(3001510) # Ferret
sm.sendSay("#face4#Hm, doesn't seem like they're lying.")
sm.setInnerOverrideSpeakerTemplateID(3001508) # Zippy
sm.sendSay("#face2#Well, they smile too much to be evil, right? Maybe we should let 'em go. What does everybody think?")
sm.blind(True, 200, 0, 0, 0, 3000)
sm.sendDelay(500)
sm.setInnerOverrideSpeakerTemplateID(3001509) # Salvo
sm.sendNext("#face1#No! We don't know who that is! And they haven't even listened to my music! What if they turn around and attack us the moment we untie them?!")
sm.setInnerOverrideSpeakerTemplateID(3001512) # Digs
sm.sendSay("#face0#Salvo's got a point. Well, about them attacking us, not the music.")
sm.setInnerOverrideSpeakerTemplateID(3001513) # Grit
sm.sendSay("#face0#Morale at the refuge is already bad. If we have another problem, it'll be devastating.")
sm.sendDelay(1100)
sm.setInnerOverrideSpeakerTemplateID(3001500) # Ark
sm.sendNext("#face3#(This debate is clearly not leaning in my favor. Maybe I should just go with my original plan to work the rope loose and make a break for it.)")
sm.sendDelay(300)
sm.blind(False, 0, 0, 0, 0, 300)
sm.sendDelay(500)
sm.zoomCamera(0, 1000, 0, -300, 70)
sm.sendDelay(500)
sm.zoomCamera(0, 1000, 0, -300, 70)
sm.setInnerOverrideSpeakerTemplateID(3001508) # Zippy
sm.sendNext("#face2#The alarm?! Monsters again... Get ready, everyone! Now! We must defend the refuge!")
sm.sendSay("#face2#Anyone who can't fight needs to find a safe place to hide. Anyone who can, follow me!")
sm.sendDelay(500)
sm.zoomCamera(0, 1000, 0, -300, 70)
sm.sendDelay(500)
sm.playSound("Sound/SoundEff.img/blackHeaven/secretmission3", 100)
sm.changeBGM("Bgm28.img/helisiumWarcry", 0, 0)
sm.setInnerOverrideSpeakerTemplateID(3001510) # Ferret
sm.sendNext("#face2#It's too late! Look!")
sm.sendDelay(500)
sm.zoomCamera(1000, 2000, 1000, -1000, 70)
sm.sendDelay(1000)
sm.spawnNpc(3001527, -1450, -273)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1430, -273)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1420, -273)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1400, -273)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1380, -273)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1370, -273)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1350, -273)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1300, -273)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1450, -78)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1430, -78)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1420, -78)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1410, -78)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1350, -78)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1320, -78)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1300, -78)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1280, -78)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1350, 150)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1120, 150)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.spawnNpc(3001527, -1200, 150)
sm.showNpcSpecialActionByTemplateId(3001527, "summon", 0)
sm.spawnNpc(3001528, -1480, 150)
sm.showNpcSpecialActionByTemplateId(3001528, "summon", 0)
sm.moveNpcByTemplateId(3001527, False, 600, 300)
sm.moveNpcByTemplateId(3001528, False, 400, 300)
sm.moveNpcByTemplateId(3001527, False, 500, 300)
sm.moveNpcByTemplateId(3001528, False, 400, 300)
sm.moveNpcByTemplateId(3001527, False, 600, 300)
sm.moveNpcByTemplateId(3001528, False, 400, 300)
sm.moveNpcByTemplateId(3001527, False, 700, 300)
sm.moveNpcByTemplateId(3001528, False, 400, 300)
sm.moveNpcByTemplateId(3001527, False, 500, 300)
sm.moveNpcByTemplateId(3001528, False, 400, 300)
sm.moveNpcByTemplateId(3001527, False, 400, 300)
sm.moveNpcByTemplateId(3001528, False, 500, 300)
sm.moveNpcByTemplateId(3001527, False, 400, 300)
sm.moveNpcByTemplateId(3001528, False, 600, 300)
sm.moveNpcByTemplateId(3001527, False, 400, 300)
sm.moveNpcByTemplateId(3001528, False, 700, 300)
sm.moveNpcByTemplateId(3001527, False, 300, 300)
sm.moveNpcByTemplateId(3001528, False, 200, 300)
sm.moveNpcByTemplateId(3001527, False, 400, 300)
sm.moveNpcByTemplateId(3001528, False, 400, 300)
sm.showNpcSpecialActionByTemplateId(3001527, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001528, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001527, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001528, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001527, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001528, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001527, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001528, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001527, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001528, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001527, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001528, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001527, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001528, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001527, "move", -1)
sm.showNpcSpecialActionByTemplateId(3001528, "move", -1)
sm.sendDelay(1000)
sm.zoomCamera(1000, 2000, 1000, -750, 150)
sm.sendDelay(1000)
sm.sendDelay(500)
sm.setInnerOverrideSpeakerTemplateID(3001508) # Zippy
sm.sendNext("#face1#Everyone, RUN!!")
sm.sendDelay(1000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(1000)
sm.sendNext("#face2#I'm sorry about the misunderstanding! I'll let you go. Hurry!")
sm.sendDelay(1000)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.warp(402000615)
