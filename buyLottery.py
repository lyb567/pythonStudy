import Lottery

qishu = 1
c = Lottery.Customer()
m = Lottery.Mechine()
c.buyLottery([1, 6, 11, 16, 21, 30], 7)
c.buyLottery([5, 7, 9, 12, 20, 21], 15)
c.buyLotteryRandom(22222222)
for i in range(qishu):
    resNum = m.shakeResult()
    for j in c.getTicket():
        cusNum = j
        res = Lottery.compare(resNum, cusNum)
        if res < 3 and res != 0:
            print("中了{0}等奖，共开了{1}期，第{2}注彩中奖".format(res, i, len(c.getTicket())*i), resNum.getRedNum(), "蓝球号码：", resNum.getBlueNum())


