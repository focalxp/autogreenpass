import numpy as np
from sklearn import utils

earlyfirstname = np.array([
"Solbe ",
"Jin",
"Yunseo ",
"Miley",
"William",
"Alex",
"Eric",
"Evan",
"Muhammad",
"Jeffrey ",
"ruthie",
])


earlylastname = np.array([
"Hwang",
"Lee",
"Jung",
"Chang",
"Kim",
"Park",
"Ko",
"Koh",
"Khalil",
"Sun ",
"kang",
])
earlygrade = np.array([
"12",
"11",
"11",
"12",
"12",
"12",
"12",
"10",
"12",
"11",
"11",
])

earlyidstring = np.array([
"shwang23",
"jylee24",
"yjung24",
"cchang23",
"wikim23",
"apark23",
"jko23",
"hskoh25",
"mkhalil23",
"jsun24",
"rkang24",
])

earlyemail = np.array([
"shwang23@student.kis.or.kr",
"jylee24@student.kis.or.kr",
"yjung24@student.kis.or.kr",
"cchang23@student.kis.or.kr",
"wikim23@student.kis.or.kr",
"apark23@student.kis.or.kr",
"jko23@student.kis.or.kr",
"hskoh25@student.kis.or.kr",
"mkhalil23@student.kis.or.kr",
"jsun24@student.kis.or.kr",
"rkang24@student.kis.or.kr",
])

earlyemail, earlyidstring, earlyfirstname, earlylastname, earlygrade = utils.shuffle(earlyemail, earlyidstring, earlyfirstname, earlylastname, earlygrade)

#for i in range(len(earlyfirstname)):
    #print("%s %s %s %s %s" %(earlyemail[i], earlyidstring[i], earlyfirstname[i], earlylastname[i], earlygrade[i]))