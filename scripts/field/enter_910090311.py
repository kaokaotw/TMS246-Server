# id 910090311 (Partem : Ruins Guardian Way Entrance), field 910090311
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.spawnNpc(1013350, -631, 60)
sm.showNpcSpecialActionByTemplateId(1013350, "summon", 0)
sm.zoomCamera(0, 2000, 0, -540, -400)
sm.sendDelay(500)
sm.createFieldTextEffect("#fnArial##fs18#Partem Ruins", 100, 1000, 6, -50, -50, 1, 4, 0, 0, 0)
sm.zoomCamera(4000, 2000, 4000, -540, 100)
sm.sendDelay(4500)
sm.setSpeakerType(3)
sm.setParam(549)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendNext("#face0#Huh. So it really was a secret entrance into the ruins after all.")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendSay("#face0#Ack... Who designed this place, anyway? This path branches off in a bunch of different directions. Do you have any clue which way we should go? Because I sure don't...")
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendSay("#face3#(Well, this place gives us nothing if not options for taking a wrong turn. Guess I didn't notice the first time I was in here because I just followed the light from the altar key.)")
sm.sendSay("#face0#(Hmm... Would there be a clue to undoing the curse in the chamber where I first found the relic? Or should I look somewhere else?)")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendSay("#face0#Uhm... I think I'm hearing a faint vibration-y sort of sound. Is it just me? It's sort of like what I hear when the ruins shake, so that's not very encouraging.")
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendSay("#face6##b(You stand still, trying to focus on the sound. Though faint, you do hear a deep thrum from further below.)#k")
sm.sendSay("#face0#(If I can zero in on where that sound is coming from, it might lead to something. The question is, how do I do that when it's so faint? Hmm... Y'know, even if I can't, maybe SHE can...)")
sm.sendSay("#face0#Hey, kiddo, got a favor to ask. Do you think you can root out the source of this sound?")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendSay("#face0#I think so. I've been frightened by those loud noises from the ruins for so long that I've become almost hypersensitive to sounds like that.")
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendSay("#face0#All right. Lead the way, then, and I'll follow.")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendSay("#face0#So you want to actually go TOWARD the sound? Eeep... That seems more than a little dicey to me, but I'll summon up all my courage and do it. Just promise me you'll be right behind me.")
sm.sendDelay(500)
sm.zoomCamera(2000, 1000, 2000, -120, -48)
sm.moveNpcByTemplateId(1013350, False, 550, 180)
sm.sendDelay(2000)
sm.forcedMove(False, 300)
sm.sendDelay(2000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(500)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(35923)
sm.createQuestWithQRValue(35948, "00=h0;10=h0;11=h1;02=h1;21=h0;12=h0;22=h1;13=h0;23=h1;14=h0;24=h0;15=h0;06=h0;25=h0;07=h0;16=h0;26=h1;08=h0;17=h0;09=h0;19=h0")
sm.createQuestWithQRValue(35948, "00=h0;10=h0;11=h1;02=h1;21=h0;12=h0;22=h1;13=h0;23=h1;14=h0;24=h0;15=h1;06=h0;25=h0;07=h0;16=h0;26=h1;08=h0;17=h0;09=h0;19=h0")
sm.warp(100051041)