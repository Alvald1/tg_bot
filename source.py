import requests
import json
import time


def getMoex():
    tickers = [["TQBR", "GAZP", 10], ["TQBR", "HHRU", 1], ["TQTF", "FXUS", 100], ["TQTF", "RUSE", 1], ["TQBR", "MOEX", 10]]  # TQBR - акции   TQTF - ETF
    summ = 0
    res = ''
    for i in tickers:
        url = f'https://iss.moex.com/iss/engines/stock/markets/shares/boards/{i[0]}/securities/{i[1]}.json'
        r = requests.get(url)
        t = json.loads(r.text)
        summ += t['marketdata']['data'][0][37]*i[2]
        res += i[1] + ': ' + str(t['marketdata']['data'][0][37]) + '₽ - ' + str(round(t['marketdata']['data'][0][37]*i[2], 2))+'₽\n'
    return res + str(round(summ, 2))+'₽'


def getSteam():
    skins = [['Rio 2022 Contenders Sticker Capsule', 28],
             ['Rio 2022 Challengers Sticker Capsule', 32],
             ['Rio 2022 Legends Sticker Capsule', 2],
             ['Rio 2022 Contenders Autograph Capsule', 2],
             ['Rio 2022 Challengers Autograph Capsule', 2],
             ['Rio 2022 Legends Autograph Capsule', 2],
             ['Antwerp 2022 Contenders Autograph Capsule', 5],
             ['Antwerp 2022 Challengers Autograph Capsule', 5],
             ['Antwerp 2022 Legends Autograph Capsule', 6],
             ['Antwerp 2022 Champions Autograph Capsule', 3],
             ['Antwerp 2022 Contenders Sticker Capsule', 3],
             ['Antwerp 2022 Challengers Sticker Capsule', 3],
             ['Antwerp 2022 Legends Sticker Capsule', 3],
             ['Operation Riptide Case', 36],
             ['Operation Broken Fang Case', 38]]
    summ = 0
    res = ''
    for i in skins:
        url = f'https://steamcommunity.com/market/priceoverview/?currency=5&country=us&appid=730&market_hash_name={i[0].replace(" ","%20")}&format=json'
        r = requests.get(url)
        t = json.loads(r.text)
        if (t):
            price = float(t['lowest_price'][:-5].replace(',', '.'))
            res += (i[0]+': ' + str(price)+'₽ - ' + str(round(price*i[1], 2))+'₽\n')
            summ += round(price*i[1], 2)
        time.sleep(0.1)
    return res + str(round(summ, 2))+'₽'
