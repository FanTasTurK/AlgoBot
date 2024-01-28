import bot, config

BOT_TOKEN = config.BOT_TOKEN
BOT_ID = config.BOT_ID

def strategy(Price,Coin,side,CoinList,TP,stpLoss):

    bot.tbot(BOT_TOKEN,BOT_ID,Price,Coin,side,CoinList,TP,stpLoss)