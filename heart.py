# This is the function file

# Value is the amount of heart being given or taken

def changeHeart(giverID: str, receiverID: str, value: str, filename: str): # Changes the values of the hearts in the CSV, returns nothing
  has_IDs = False
  rowNum = 0
  fileR = open(filename, 'r')
  fileInfo = fileR.read()
  fileR.close()
  fileInfo = fileInfo.split("\n")
  newHeart = 0.0
  for line in fileInfo:
    items = line.split(',')
    if((items[0] == giverID and items[1] == receiverID) or (items[0] == receiverID and items[1] == giverID)):
      has_IDs = True
      newHeart = str(round(float(items[2]) + float(value),1))
      break
    rowNum += 1
    
  if has_IDs == False:
    newFile = open(filename, 'w')
    for y in fileInfo:
      newFile.write(y + "\n")
    newFile.write(giverID + "," + receiverID + "," + value)
    newFile.close()
  
  if has_IDs == True:
    newFile = open(filename, 'w')
    for x in range(0, len(fileInfo)):
      if x != rowNum:
        newFile.write(fileInfo[x] + "\n")
      else:
        newFile.write(giverID + "," + receiverID + "," + newHeart)
  
def checkValue(id1, id2, filename): # Returns value of heart between two individuals
  hasHeart = False
  filex = open(filename, 'r')
  fileInfo = filex.read()
  filex.close()
  fileInfo = fileInfo.split("\n")
  for line in fileInfo:
    items = line.split(',')
    if (items[0] == id1 and items[1] == id2) or (items[0] == id2 and items[1] == id1):
      hasHeart = True
      return float(items[2])
  if hasHeart == False:
    return -1

#Determining Gift Icon
def det_icon(gift):
  gift_icon = ""
  if gift == "精灵球":
    gift_icon = "<:timg7:679280027371831337>"
  elif gift == "卡比兽的棒棒糖": 
    gift_icon = ":lollipop:"
  elif gift == "胖丁的甜苹果": 
    gift_icon = ":apple:"
  elif gift == "飞云冰淇淋": 
    gift_icon = ":shaved_ice:"
  elif gift == "波克比幸运蛋": 
    gift_icon = ":crystal_ball:"
  elif gift == "贝壳之铃": 
    gift_icon = ":oyster:"
  elif gift == "宝可梦之笛": 
    gift_icon = "<a:708890470557941823:710561626658439209>"
  elif gift == "七夕青鸟的钻石" :
    gift_icon = "<:691351339409735760:703524939403100161>"
  elif gift == "超梦的许愿星": 
    gift_icon = ":Star:"
  elif gift == "凤王的七彩皇冠": 
    gift_icon = "<:691351337618899024:703524938832806000>"
  elif gift == "宝可梦之心":
    gift_icon = "<:682610054578569226:691351338059300934>"
  elif gift == "日冠名":
    gift_icon = ":yellow_heart:"
  elif gift == "三日冠":
    gift_icon = ":blue_heart:"
  elif gift == "五日冠":
    gift_icon = ":brown_heart:"
  elif gift == "周冠名":
    gift_icon = ":heart:"
  elif gift == "十日冠":
    gift_icon = ":purple_heart:"
  elif gift == "半月冠":
    gift_icon = ":heartpulse:"
  elif gift == "月冠名" :
    gift_icon = "<a:708890471493009468:710561624372805744>"
  elif gift == "年冠名" :
    gift_icon = "<:691351339409735760:703524939403100161>"
  return gift_icon

#Determining gift picture
def det_pic(gift):
  gift_pic = ""
  if gift == "精灵球":
    gift_pic = "精灵球.png"
  elif gift == "卡比兽的棒棒糖": 
    gift_pic = "棒棒糖.png"
  elif gift == "胖丁的甜苹果": 
    gift_pic = "甜苹果.png"
  elif gift == "飞云冰淇淋": 
    gift_pic = "冰淇淋.png"
  elif gift == "波克比幸运蛋": 
    gift_pic = "幸运蛋.png"
  elif gift == "贝壳之铃": 
    gift_pic = "贝壳铃.png"
  elif gift == "宝可梦之笛": 
    gift_pic = "梦之笛.png"
  elif gift == "七夕青鸟的钻石": 
    gift_pic = "青鸟钻石.png"
  elif gift == "超梦的许愿星": 
    gift_pic = "许愿星.png"
  elif gift == "凤王的七彩皇冠": 
    gift_pic = "七彩皇冠.png"
  elif gift == "宝可梦之心": 
    gift_pic = "宝可梦之心.png"
  elif gift == "蒂安希的粉色钻石":
    gift_pic = "粉色钻石.gif"
  elif gift == "日冠名": 
    gift_pic = "日冠名.png"
  elif gift == "三日冠": 
    gift_pic = "三日冠.png"
  elif gift == "五日冠" :
    gift_pic = "五日冠.png"
  elif gift == "周冠名" :
    gift_pic = "周冠名.png"
  elif gift == "十日冠" : 
    gift_pic = "十日冠.png"
  elif gift == "半月冠" :
    gift_pic = "半月冠.png"
  elif gift == "月冠名" :
    gift_pic = "月冠名.gif"
  elif gift == "年冠名" :
    gift_pic = "年冠名.png"
  return gift_pic

#Get level of heart
def get_level(before_val, after_val, gifterNickID, receiverNickID):
  changeLevelHeart = False
  levelAnnounce = ""
  if (before_val < 131.4 and after_val >= 131.4 and after_val < 288):
    changeLevelHeart = True
    levelAnnounce = "并达成双人tag【" + gifterNickID + "&" + receiverNickID + ":rose: 不期而遇】"
  elif (before_val < 288 and after_val >= 288 and after_val < 365):
    changeLevelHeart = True
    levelAnnounce = "并达成双人tag【" + gifterNickID + "&" + receiverNickID + ":cupid: 怦然心动】"
  elif (before_val < 365 and after_val >= 365 and after_val < 520):
    changeLevelHeart = True
    levelAnnounce = "并达成双人tag【" + gifterNickID + "&" + receiverNickID + ":revolving_hearts: 两心相仪】"
  elif (before_val < 520 and after_val >= 520 and after_val < 1314):
    changeLevelHeart = True
    levelAnnounce = "并达成双人tag【" + gifterNickID + "&" + receiverNickID + ":champagne_glass: 真情诺诺】"
  elif (before_val < 1314 and after_val >= 1314 and after_val < 3344):
    changeLevelHeart = True
    levelAnnounce = "并达成双人专属永久tag【" + gifterNickID + "&" + receiverNickID + ":tulip: 情有独钟】"
  elif (before_val < 3344 and after_val >= 3344 and after_val < 5200):
    changeLevelHeart = True
    levelAnnounce = "并达成双人专属永久tag【" + gifterNickID + "&" + receiverNickID + ":sunrise_over_mountains: 一眼万年】"
  elif (before_val < 5200 and after_val >= 9999):
    changeLevelHeart = True
    levelAnnounce = "并达成双人专属永久tag【" + gifterNickID + "&" + receiverNickID + ":wedding: 岁月与共】"
  elif (before_val < 9999 and after_val >= 9999 and after_val < 13140):
    changeLevelHeart = True
    levelAnnounce = "并达成双人专属永久tag【" + gifterNickID + "&" + receiverNickID + ":bridge_at_night: 死生契阔】"
  elif (before_val < 13140 and after_val >= 13140 and after_val < 15200):
    changeLevelHeart = True
    levelAnnounce = "并达成双人专属永久tag【" + gifterNickID + "&" + receiverNickID + ":rainbow: 白首不分离】"
  elif (before_val < 15200 and after_val >= 15200 and after_val < 19999):
    changeLevelHeart = True
    levelAnnounce = "并达成双人专属永久tag【" + gifterNickID + "&" + receiverNickID + ":couple_with_heart: 一生一代一双人】"
  elif (before_val < 19999 and after_val >= 19999 and after_val < 33440):
    changeLevelHeart = True
    levelAnnounce = "并达成双人专属永久tag【" + gifterNickID + "&" + receiverNickID + ":milky_way: 河汉无极不如你】"
  elif (before_val < 33440 and after_val >= 33440):
    changeLevelHeart = True
    levelAnnounce = "并达成双人专属永久tag【" + gifterNickID + "&" + receiverNickID + ":stars:老板自定义tag名称/陪玩接该老板订单将获得永久90%分成】"
  return levelAnnounce

#Check gift value <1000, 1000-3000, >3000
def checkGift(value):
  if float(value) < 1000:
    return 1
  elif float(value) >= 1000 and float(value) < 3000:
    return 2
  elif float(value) >= 3000:
    return 3

#Determine Gift Value
def checkGiftValue(gift):
  gift_value = 0.0
  if gift == "精灵球":
    gift_value = 9
  elif gift == "卡比兽的棒棒糖": 
    gift_value = 26
  elif gift == "胖丁的甜苹果": 
    gift_value = 52
  elif gift == "飞云冰淇淋": 
    gift_value = 99
  elif gift == "波克比幸运蛋": 
    gift_value = 188
  elif gift == "贝壳之铃": 
    gift_value = 365
  elif gift == "宝可梦之笛": 
    gift_value = 520
  elif gift == "七夕青鸟的钻石" :
    gift_value = 999
  elif gift == "超梦的许愿星": 
    gift_value = 1314
  elif gift == "凤王的七彩皇冠": 
    gift_value = 3344
  elif gift == "宝可梦之心":
    gift_value = 5200
  elif gift == "日冠名":
    gift_value = 131.4
  elif gift == "三日冠":
    gift_value = 365
  elif gift == "五日冠":
    gift_value = 666
  elif gift == "周冠名":
    gift_value = 888
  elif gift == "十日冠":
    gift_value = 1314
  elif gift == "半月冠":
    gift_value = 1888
  elif gift == "蒂安希的粉色钻石":
    gift_value = 2020
  elif gift == "月冠名" :
    gift_value = 3650
  elif gift == "年冠名" :
    gift_value = 15200
  return gift_value

def help():
  help_out = "Commands: \n **/give** gifter_id reciever_id gift number_gifts amount anonymous(t/f)- comment \n **/back** gifter_id reciever_id gift number_gifts amount"
  return help_out