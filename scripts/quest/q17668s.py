# id 17668 ([Commerci Republic] Twice Cooked), field 865030111
sm.setSpeakerID(9390238) # Zion
sm.sendNext("So s-should we go? I don't feel safe here.")
sm.setParam(2)
sm.sendSay("Yeah, let's leave..")
sm.setParam(4)
sm.setInnerOverrideSpeakerTemplateID(9390202) # Leon Daniella
sm.sendSay("Wait, where's Claire?")
sm.setParam(0)
sm.sendSay("She is safe. One of my men escorted her away before the battle.")
sm.sendSay("She's likely in #b#m865030300##k.")
sm.setParam(2)
res = sm.sendAskYesNo("I see, then let's go.")
sm.setParam(57)
sm.setColor(1)
sm.sendNext("Let's go see Gilberto.")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9390218) # Il Capo
sm.sendSay("I don't think so.")
sm.setParam(32)
sm.sendSay("Gah!")
sm.startQuest(parentID)
sm.setParam(57)
sm.sendSay("Zion! Wake up Zion!")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9390202) # Leon Daniella
sm.sendSay("...He's gone. Maaaaan, how are we going to clear our names?!")
sm.setParam(57)
sm.sendSay("We let our guard down, and now... what are we going to do?")
sm.setParam(37)
sm.sendSay(" We at least have to find Claire.")
sm.setParam(57)
sm.sendSay("Where did Zion say she was?")
sm.setParam(37)
sm.sendSay("#b#m865030300##k. Let's move.")
