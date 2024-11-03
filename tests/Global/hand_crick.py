import random

print()

oddList = ["odd","od","dd","do","o","d"] 
eveList = ["even","eve","ven","eve",'ev','ve','e'] 
batList = ['batting','bat','at','att','atting','ting','tting']
bowlList= ['bowl','ball','bal','owl','all','al']
biasList= [0,0,0,0,1] 
batScore=0
comScore=0
usrScore=0
score = {'usrScore':0, 'comScore':0}



def inp(inpMsg,dataType='',warning=""): #return integer if required else return input as it is
    inp=input(inpMsg) 
    if dataType!='int':
        return inp
    elif dataType=='int' and not inp.isnumeric():
        print()
        print(warning)
        inp = input(inpMsg)
    elif dataType=='int' and inp.isnumeric():
        return int(inp)


def outOrNot(p,c): #invalid for -1 invalid2 for any other invalid, True for out, False for not out
    if -1 in [p,c]:
        return 'invalid'
    elif p!=c:
        return False
    elif p==c:
        return True
    else:
        return 'invalid2'

def decide(l1,l2,r1,r2,dataType,inpMsg,warning=""): #return input, r1 
    while True:
        takeInp=inp(inpMsg,dataType,warning)
        if takeInp in l1:
            return takeInp, r1
        elif takeInp in l2:
            return takeInp, r2
        else:
            print()
            print(warning)



def throw(roleMsg):
    print(roleMsg)
    usrNum=decide(range(1,11),range(1,11),'','','int',"Throw a number: ")[0]
    return usrNum,random.randint(1,10) #return usr value, and a random from 1 to 10



def switchRole(batting):
    if batting=='usr':
        batting='com'
    else:
        batting='usr'


oddOrEve = decide(eveList,oddList,'eve','odd','',"Enter Odd or Eve: ","Only enter Odd or Eve!")[1]  #stores odd or eve 
print (oddOrEve) #debug statement


oddEveVal=decide(range(1,10,2),range(2,10,2),'odd','eve','int',"Enter a number for Odd or Eve(max: 10): ","Only enter odd or eve(max: 10)")
oddEveVal=oddEveVal[0] 
print (oddEveVal) #debug statement 

#check if odd or eve 
comOddEveVal = random.randint(1,10)
checkOddEveVal=oddEveVal+comOddEveVal #sum to check for oddeve 
if (checkOddEveVal%2==0 and oddOrEve=='eve') or (checkOddEveVal%2==1 and oddOrEve=='odd'):
    usrWillChoose = True
else:
    usrWillChoose=False


#if usr won oddEve ask for bat or ball
if usrWillChoose:
    print(oddEveVal,'+',comOddEveVal,'=',oddEveVal+comOddEveVal,"\nYou can choose")
    batting=decide(batList,bowlList,'usr','com','notInt',"Batting or Bowling: ","Enter a valid choice!\n")[1] #batting takes usr or com
else:
    batting=random.choice(['com' for x in biasList if x==0]+['usr'])
    if batting == 'com':
        comRole='bat'
    else:
        comRole='bowl'
    print("Coumputer chose to",comRole)



isNotOut=True
teamsBowled = 0



def declareOut(batting):
    return "You took a wicket!" if batting == 'com' else "You lost a  wicket!"


def easyMatch():
    global teamsBowled
    if teamsBowled==2:
        return score['usrScore'],score['comScore']
    if batting == 'usr':
        roleMsg = "You are batting"
    else:
        roleMsg="You are bowling"
    global batScore
    global isNotOut
    while isNotOut and batScore<=50 and teamsBowled!=2: 
        [batThrow,bowlThrow] = throw(roleMsg) 
        isNotOut=outOrNot(batThrow,bowlThrow) 
        batScore+=batThrow 
    print(declareOut(batting))
    score[batting+'Score'] = batScore 
    print('Runs: ',batScore)
    teamsBowled = teamsBowled+1
    switchRole(batting)
    easyMatch()

easyMatch()

def declareResult():
    if score['usrScore'] > score['comScore']:
        print("You won!\n",score['usrScore'],":",score['comScore'])
    elif score['usrScore'] < score['comScore']:
        print("You lost!\n",score['usrScore'],":",score['comScore'])

    else:
        print("Close Game! It was a tie!",score['comScore'])