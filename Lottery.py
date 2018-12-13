import random


def randomRedNum():
    '''
    随机取得一组红球号码
    :return: 一个6元素list
    '''
    redNum = []
    while len(redNum) < 6:
        i = random.randint(1, 33)
        if i not in redNum:
            redNum.append(i)
    redNum.sort()
    return redNum


class Lottery():
    def __init__(self, redNum, blueNum):
        self.__redNum = redNum
        self.__blueNum = blueNum

    def setRedNum(self, redNum):
        self.__redNum = redNum

    def setBlueNum(self, blueNum):
        self.__blueNum = blueNum

    def getRedNum(self):
        return self.__redNum

    def getBlueNum(self):
        return self.__blueNum

class Mechine():
    '''
    开奖机，产生开奖号码
    '''

    def shakeResult(self):
        result = Lottery(randomRedNum(), random.randint(1, 16))
        return result


class Customer():
    '''
    购彩人，可购买彩票
    '''
    def __init__(self, ticket=None):
        if ticket == None:
            ticket = []
        self.__ticket = ticket

    def buyLotteryRandom(self, num):
        '''
        增加随机号
        :param num: 增加注数
        :return: 无
        '''
        for i in range(num):
            lottery = Lottery(randomRedNum(), random.randint(1, 16))
            self.__ticket.append(lottery)

    def buyLottery(self, redNum, blueNum):
        '''
        增加一注手选号码
        :param redNum:红球号，一个6元列表
        :param blueNum: 蓝球号，一个整数
        :return: 无
        '''
        redNum.sort()
        lottery = Lottery(redNum, blueNum)
        self.__ticket.append(lottery)

    def getTicket(self):
        return self.__ticket

    def speak(self):
        if len(self.__ticket) == 0:
            print("还没要购彩!")
            return None
        else:
            print("目前共购了{}注彩票，号码如下：".format(len(self.__ticket)))
            for i in self.__ticket:
                print("彩票红球号码：{0},蓝球号码：{1}".format(i.getRedNum(), i.getBlueNum()))

def compare(result, customerNum):
    '''
    对奖函数
    :param result: 开奖号码,一个Lottery对象
    :param customerNum: 彩票号码，一个Lottery对象
    :return: 中奖级数
    '''
    red = 0
    blue = 0
    for i in customerNum.getRedNum():
        if i in result.getRedNum():
            red += 1
    if customerNum.getBlueNum() == result.getBlueNum():
        blue += 1
    if red == 6 and blue == 1:
        return 1
    elif red == 6 and blue == 0:
        return 2
    elif red == 5 and blue == 1:
        return 3
    elif (red == 5 and blue == 0) or (red == 4 and blue == 1):
        return 4
    elif (red == 4 and blue == 0) or (red == 3 and blue == 1):
        return 5
    elif (red == 2 and blue == 1) or (red == 1 and blue == 1) or (red == 0 and blue == 1):
        return 6
    else:
        return 0

