# id 940200270 (Arcana : Grove of the Spirit Tree), field 940200270
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.spawnNpc(3003369, 292, 123)
sm.showNpcSpecialActionByTemplateId(3003369, "summon", 0)
sm.showNpcSpecialActionByTemplateId(3003369, "stand2", -1)
sm.resetNpcSpecialActionByTemplateId(3003369)
sm.showNpcSpecialActionByTemplateId(3003369, "appear", 0)
sm.sendDelay(4500)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("This aura... it's so much darker than the other tainted spirits...")
sm.sendDelay(900)
sm.sendNext("I won't allow you to corrupt this forest!")
sm.lockInGameUI(False, True)
sm.warp(940200280)
