﻿# a.Перетворення значення HEX в Little Endian значення
def hexToLittle (hexVal, numOfBytes):
   numOfBits = numOfBytes * 8
   binVal = bin(int(hexVal, 16))[2:]

   if len(binVal) < numOfBits:
      binVal = "0" * (numOfBits - len(binVal)) + binVal 

   #divide into bytes
   bytesArr = []
   for i in range(numOfBytes):
      currByte = binVal[i*8:(i+1)*8]
      bytesArr.append(currByte)
   
   #swap
   for j in range(int(numOfBytes/2)): 
      bytesArr[j], bytesArr[numOfBytes-j-1] = bytesArr[numOfBytes-j-1], bytesArr[j]

   #collect bytes into a bit string
   bitStr = ""
   for i in bytesArr:
      bitStr += i

   return int(bitStr, 2)

# b.Перетворення значення HEX в Little Endian значення
def hexToBig (hexVal):
   binVal = bin(int(hexVal, 16))[2:]
   return int(binVal, 2)

#c.Перетворення значення Little Endian на HEX значення
def littleToHex (littleVal, numOfBytes):
   numOfBits = numOfBytes * 8
   binVal = bin(littleVal)[2:]

   if len(binVal) < numOfBits:
      binVal = "0" * (numOfBits - len(binVal)) + binVal 

   #divide into bytes
   bytesArr = []
   for i in range(numOfBytes):
      currByte = binVal[i*8:(i+1)*8]
      bytesArr.append(currByte)
   
   #swap
   for j in range(int(numOfBytes/2)): 
      bytesArr[j], bytesArr[numOfBytes-j-1] = bytesArr[numOfBytes-j-1], bytesArr[j]

   #collect bytes into a bit string
   bitStr = ""
   for i in bytesArr:
      bitStr += i

   return hex(int(bitStr,2))

#d.Перетворення BIG Endian значення в HEX значення
def bigToHex (bigVal):
   return hex(bigVal)

#Test vectors:
def catchError(number, hexVal, numOfBytes, littleVal, bigVal):
   print("\n")
   hexVal = hexVal.lower()
   try:
      hexTolittleVal = hexToLittle(hexVal, numOfBytes)
      if littleVal != hexTolittleVal:
         print(f"Error vallue hexToLittle {number}")
         print(f"correct vallue {littleVal}")
         print(f"incorrect vallue {hexTolittleVal}\n")
      else: print(f"Correct hexToLittle {number}\n")

      hexToBigVal = hexToBig(hexVal)
      if bigVal != hexToBigVal:
         print(f"Error vallue hexToBig {number}")
         print(f"correct vallue {bigVal}")
         print(f"incorrect vallue {hexToBigVal}\n")
      else: print(f"Correct hexToBig {number}\n")

      littleToHexVal = littleToHex(littleVal, numOfBytes)
      if littleToHexVal != hexVal:
         print(f"Error vallue littleToHex {number}")
         print(f"correct vallue {hexVal}")
         print(f"incorrect vallue {littleToHexVal}\n")
      else: print(f"Correct littleToHex {number}\n")

      bigToHexVal = bigToHex(bigVal)
      if hexVal != bigToHexVal:
         print(f"Error vallue bigToHex {number}")
         print(f"correct vallue {hexVal}")
         print(f"incorrect vallue {bigToHexVal}\n")
      else: print(f"Correct bigToHex {number}\n")
   except:
         print('Error!!!')

#a.Vector 1:
catchError(1,"0xff00000000000000000000000000000000000000000000000000000000000000", 32, 255, 115339776388732929035197660848497720713218148788040405586178452820382218977280)
#b.Vector 2:
catchError(2,"0xaaaa000000000000000000000000000000000000000000000000000000000000", 32, 43690, 77193548260167611359494267807458109956502771454495792280332974934474558013440)
#c.Vector 3:
catchError(3,"0xFFFFFFFF", 4, 4294967295, 4294967295)
#d.Vector 4:
catchError(4,"0xF000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", 512, 240, 979114576324830475023518166296835358668716483481922294110218890578706788723335115795775136189060210944584475044786808910613350098299181506809283832360654948074334665509728123444088990750984735919776315636114949587227798911935355699067813766573049953903257414411690972566828795693861196044813729172123152193769005290826676049325224028303369631812105737593272002471587527915367835952474124875982077070337970837392460768423348044782340688207323630599527945406427226264695390995320400314062984891593411332752703846859640346323687201762934524222363836094053204269986087043470117703336873406636573235808683444836432453459818599293667760149123595668832133083221407128310342064668595954073131257995767262426534143159642539179485013975461689493733866106312135829807129162654188209922755829012304582671671519678313609748646814745057724363462189490278183457296449014163077506949636570237334109910914728582640301294341605533983878368789071427913184794906223657920124153256147359625549743656058746335124502376663710766611046750739680547042183503568549468592703882095207981161012224965829605768300297615939788368703353944514111011011184191740295491255291545096680705534063721012625490368756140460791685877738232879406346334603566914069127957053440)

