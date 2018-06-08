import numpy as np
import datetime
import requests
import time
import random

# PSBB to Vadapalani route MAP.

x=np.array([ [80.1992218,13.039887],
 [80.1992218,13.039887],
 [80.1990958,13.0389899],
 [80.1988851,13.0376059],
 [80.19885220000001,13.03743],
 [80.1987535,13.0368438],
 [80.1987402,13.0367638],
 [80.198562,13.036792],
 [80.1984391,13.0368078],
 [80.198429,13.036733],
 [80.19843779999999,13.0367924],
 [80.19837,13.036802],
 [80.198279,13.036815],
 [80.198188,13.036828],
 [80.198097,13.03684],
 [80.198005,13.036853],
 [80.197914,13.036866],
 [80.19781999999999,13.03688],
 [80.197732,13.036895],
 [80.197641,13.036911],
 [80.19755000000001,13.036927],
 [80.197459,13.036942],
 [80.19736,13.03696],
 [80.197278,13.036973],
 [80.197187,13.036988],
 [80.19705999999999,13.03701],
 [80.19705999999999,13.036995],
 [80.196974,13.03702],
 [80.196883,13.037032],
 [80.19682,13.03704],
 [80.196701,13.037062],
 [80.19661000000001,13.037079],
 [80.19652000000001,13.037096],
 [80.196429,13.037113],
 [80.19634000000001,13.03713],
 [80.196247,13.037144],
 [80.196156,13.037158],
 [80.196065,13.037172],
 [80.1960378,13.0371759],
 [80.19597400000001,13.037185],
 [80.195883,13.037199],
 [80.195792,13.037213],
 [80.1957,13.037227],
 [80.19560900000001,13.037241],
 [80.19551800000001,13.037255],
 [80.195427,13.037269],
 [80.195336,13.037282],
 [80.195245,13.037296],
 [80.195154,13.03731],
 [80.19506199999999,13.037324],
 [80.194971,13.037338],
 [80.19488,13.037352],
 [80.19476,13.03737],
 [80.194698,13.037377],
 [80.19460599999999,13.037387],
 [80.194515,13.037398],
 [80.194423,13.037408],
 [80.19433100000001,13.037418],
 [80.19423999999999,13.037429],
 [80.194148,13.037439],
 [80.194056,13.037449],
 [80.19396500000001,13.03746],
 [80.193873,13.03747],
 [80.193782,13.03748],
 [80.19369,13.037491],
 [80.19359799999999,13.037501],
 [80.19352000000001,13.03751],
 [80.193415,13.037524],
 [80.193324,13.037537],
 [80.19323300000001,13.03755],
 [80.1931,13.03757],
 [80.193054,13.037587],
 [80.19296799999999,13.03762],
 [80.19289000000001,13.03765],
 [80.19280000000001,13.03774],
 [80.192778,13.0378],
 [80.19275,13.03788],
 [80.192739,13.037976],
 [80.19273,13.03806],
 [80.192745,13.038154],
 [80.192759,13.038244],
 [80.19277,13.03831],
 [80.19278300000001,13.038423],
 [80.192793,13.038513],
 [80.19279400000001,13.0385221],
 [80.192803,13.038603],
 [80.192814,13.038693],
 [80.192824,13.038783],
 [80.19283400000001,13.038873],
 [80.19284500000001,13.038962],
 [80.19285499999999,13.039052],
 [80.192865,13.039142],
 [80.19288,13.03927],
 [80.192886,13.039322],
 [80.19289600000001,13.039412],
 [80.19290700000001,13.039501],
 [80.19291800000001,13.039591],
 [80.192928,13.039681],
 [80.192939,13.039771],
 [80.19295,13.03986],
 [80.19306,13.03985],
 [80.19295,13.03986],
 [80.192958,13.039914],
 [80.192972,13.040004],
 [80.19298600000001,13.040093],
 [80.193,13.040182],
 [80.19301400000001,13.040272],
 [80.193028,13.040361],
 [80.19304,13.04044],
 [80.193056,13.04054],
 [80.19307000000001,13.040629],
 [80.193085,13.040718],
 [80.193099,13.040808],
 [80.19311399999999,13.040897],
 [80.193128,13.040986],
 [80.19314300000001,13.041076],
 [80.193157,13.041165],
 [80.193172,13.041254],
 [80.193186,13.041343],
 [80.1932,13.041433],
 [80.193215,13.041522],
 [80.193229,13.041611],
 [80.19324400000001,13.041701],
 [80.193258,13.04179],
 [80.19327,13.04186],
 [80.193288,13.041968],
 [80.193304,13.042057],
 [80.193319,13.042147],
 [80.19333399999999,13.042236],
 [80.19335,13.042325],
 [80.193365,13.042414],
 [80.193381,13.042503],
 [80.19339600000001,13.042592],
 [80.193411,13.042681],
 [80.19342,13.04273],
 [80.19343600000001,13.042861],
 [80.19344700000001,13.042951],
 [80.19345800000001,13.04304],
 [80.19346899999999,13.04313],
 [80.19347999999999,13.04322],
 [80.193491,13.04331],
 [80.193502,13.0434],
 [80.19351399999999,13.043489],
 [80.19353,13.04362],
 [80.193535,13.043669],
 [80.193545,13.043759],
 [80.193555,13.043849],
 [80.193564,13.043939],
 [80.193574,13.044029],
 [80.193584,13.044119],
 [80.19358680000001,13.0441469],
 [80.19359300000001,13.044209],
 [80.193603,13.044298],
 [80.193609,13.044353],
 [80.19368400000001,13.044402],
 [80.19384599999999,13.044406],
 [80.193905,13.044399],
 [80.193996,13.044387],
 [80.194087,13.044375],
 [80.19417900000001,13.044363],
 [80.19427,13.044351],
 [80.194362,13.044339],
 [80.194453,13.044327],
 [80.19454399999999,13.044315],
 [80.194636,13.044303],
 [80.194727,13.044291],
 [80.194819,13.044279],
 [80.19490999999999,13.044268],
 [80.19500100000001,13.044256],
 [80.195093,13.044244],
 [80.195184,13.044232],
 [80.19527600000001,13.04422],
 [80.19536700000001,13.044208],
 [80.195459,13.044196],
 [80.19558000000001,13.04418],
 [80.195641,13.044168],
 [80.195731,13.044151],
 [80.19582200000001,13.044135],
 [80.195913,13.044118],
 [80.19600300000001,13.044101],
 [80.196094,13.044084],
 [80.196185,13.044068],
 [80.196275,13.044051],
 [80.196366,13.044034],
 [80.196456,13.044018],
 [80.196547,13.044001],
 [80.19663799999999,13.043984],
 [80.19672799999999,13.043967],
 [80.19681900000001,13.04395],
 [80.19691,13.043934],
 [80.197,13.043917],
 [80.197091,13.0439],
 [80.197181,13.043883],
 [80.197272,13.043867],
 [80.197363,13.04385],
 [80.197453,13.043833],
 [80.19754399999999,13.043816],
 [80.19763500000001,13.0438],
 [80.19772500000001,13.043783],
 [80.197816,13.043766],
 [80.197906,13.043749],
 [80.19796,13.04374],
 [80.198089,13.043723],
 [80.19817999999999,13.043712],
 [80.198272,13.0437],
 [80.198363,13.043689],
 [80.198418,13.043682],
 [80.198499,13.043765],
 [80.198517,13.043866],
 [80.198533,13.043955],
 [80.198548,13.044044],
 [80.19856400000001,13.044133],
 [80.19858000000001,13.044222],
 [80.198596,13.044311],
 [80.198611,13.0444],
 [80.198627,13.044489],
 [80.198643,13.044578],
 [80.19865900000001,13.044667],
 [80.19867499999999,13.044757],
 [80.19869,13.044846],
 [80.1987,13.0449],
 [80.198729,13.045023],
 [80.19875,13.045111],
 [80.19877,13.045199],
 [80.198791,13.045287],
 [80.198812,13.045375],
 [80.19883299999999,13.045463],
 [80.198853,13.045551],
 [80.198874,13.045639],
 [80.19889499999999,13.045728],
 [80.19891,13.04579],
 [80.198939,13.045903],
 [80.198962,13.04599],
 [80.19898499999999,13.046078],
 [80.19900800000001,13.046166],
 [80.199032,13.046253],
 [80.199055,13.046341],
 [80.199078,13.046428],
 [80.19911000000001,13.04655],
 [80.199124,13.046603],
 [80.199147,13.046691],
 [80.19917,13.046778],
 [80.19919299999999,13.046866],
 [80.19921600000001,13.046954],
 [80.19923900000001,13.047041],
 [80.199262,13.047129],
 [80.199285,13.047216],
 [80.199308,13.047304],
 [80.19932799999999,13.047378],
 [80.199401,13.047436],
 [80.19949699999999,13.047434],
 [80.199589,13.047433],
 [80.199682,13.047431],
 [80.19977400000001,13.04743],
 [80.199866,13.047428],
 [80.199958,13.047427],
 [80.20005000000001,13.047425],
 [80.200143,13.047424],
 [80.20023500000001,13.047422],
 [80.200327,13.04742],
 [80.200419,13.047419],
 [80.200512,13.047417],
 [80.200604,13.047416],
 [80.20069599999999,13.047414],
 [80.200788,13.047413],
 [80.20088,13.047411],
 [80.20097,13.04741],
 [80.201065,13.047407],
 [80.201157,13.047404],
 [80.20129,13.0474],
 [80.201341,13.047405],
 [80.20143299999999,13.047414],
 [80.201525,13.047423],
 [80.201616,13.047432],
 [80.20169,13.04744],
 [80.201798,13.04746],
 [80.20188899999999,13.047476],
 [80.20202000000001,13.0475],
 [80.202069,13.047513],
 [80.202158,13.047537],
 [80.20228,13.04757],
 [80.202336,13.047587],
 [80.202423,13.047615],
 [80.202511,13.047643],
 [80.20263,13.04768],
 [80.202687,13.047695],
 [80.202777,13.047718],
 [80.202866,13.047741],
 [80.202955,13.047764],
 [80.20304400000001,13.047787],
 [80.20313,13.04781],
 [80.20322400000001,13.047829],
 [80.20331400000001,13.047848],
 [80.20340400000001,13.047866],
 [80.20352,13.04789],
 [80.20358400000001,13.047905],
 [80.20367400000001,13.047927],
 [80.203763,13.047949],
 [80.203853,13.04797],
 [80.203942,13.047992],
 [80.204032,13.048013],
 [80.2041,13.04803],
 [80.20421,13.048061],
 [80.20429799999999,13.048087],
 [80.204387,13.048112],
 [80.204475,13.048138],
 [80.20456400000001,13.048163],
 [80.204652,13.048189],
 [80.20475999999999,13.04822],
 [80.204829,13.048241],
 [80.204917,13.048268],
 [80.205005,13.048295],
 [80.20509300000001,13.048322],
 [80.205181,13.048349],
 [80.205269,13.048376],
 [80.20535700000001,13.048403],
 [80.205445,13.04843],
 [80.205533,13.048457],
 [80.20562099999999,13.048484],
 [80.205709,13.048511],
 [80.205797,13.048538],
 [80.205885,13.048565],
 [80.205973,13.048592],
 [80.20606100000001,13.048619],
 [80.206149,13.048646],
 [80.206237,13.048673],
 [80.20632500000001,13.048701],
 [80.206413,13.048728],
 [80.206501,13.048755],
 [80.20658899999999,13.048782],
 [80.206677,13.048809],
 [80.206765,13.048836],
 [80.20681,13.04885],
 [80.20693900000001,13.048895],
 [80.207026,13.048925],
 [80.20704809999999,13.0489326],
 [80.207032,13.048977],
 [80.2070437,13.0489428],
 [80.2074106,13.049089],
 [80.2074978,13.0515255],
 [80.2075158,13.0520692],
 [80.2075486,13.0525323],
 [80.2075588,13.0530414],
 [80.2075644,13.0532632],
 [80.2082327,13.0532314],
 ] )

print x.shape[0]

for len in range (x.shape[0],0,-1):
     longx = str(x[len-1,0])
     latx  = str(x[len-1,1])
     timex =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     print timex
     r = requests.put("http://track.intracworks.com:5055/?id="+(str(382059))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(random.randint(10,40)))
     time.sleep(0.01)

r = requests.put("http://track.intracworks.com:5055/?id="+(str(382059))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(0))
time.sleep(0.01)
r = requests.put("http://track.intracworks.com:5055/?id="+(str(382059))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(0))

     

time.sleep(600)

for len in range (0 , x.shape[0]):
     longx = str(x[len,0])
     latx  = str(x[len,1])
     timex =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     r = requests.put("http://track.intracworks.com:5055/?id="+(str(382059))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(random.randint(10,40)))
     delay_time = random.randint(1,5) 
     time.sleep(0.01)
time.sleep(320)

r = requests.put("http://track.intracworks.com:5055/?id="+(str(382059))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(0))
time.sleep(0.01)
r = requests.put("http://track.intracworks.com:5055/?id="+(str(382059))+"&lat="+(latx)+"&lon="+(longx)+"&timestamp="+(timex)+"&speed="+ str(0))





