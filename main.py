import requests

session = requests.session()
deck = 1
responses = []
all_cabins = set()
headers = {
    "Host": "www.princess.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "AMCV_21C91F2F575539D07F000101%40AdobeOrg=2121618341%7CMCIDTS%7C17219%7CMCMID%7C49671028090519812502303589936345137365%7CMCAAMLH-1488302309%7C9%7CMCAAMB-1488302309%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1487704709s%7CNONE%7CMCAID%7CNONE; mbox=check#true#1487697570|session#6f787331475941c980ad4b2cacaa1045#1487699370|PC#6f787331475941c980ad4b2cacaa1045.20_84#1488907111; _aeu=QCQ=; _aes=QSE=; __utma=169354720.57759081.1487697510.1487697510.1487697510.1; __utmb=169354720.2.10.1487697510; __utmz=169354720.1487697510.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); s_dfa=crbrprincessprodus%2Ccrbrcarnivalbrandsprodus; s_ppn=pcl%3Aplanning%3Alearn_about_cruising; s_nr=1487697511727-New; gds=1487697511728; gds_s=First%20Visit; s_vnum=1488319200772%26vn%3D1; s_invisit=true; _ga=GA1.2.57759081.1487697510; ak_bmsc=8E4CEB0092F896BFEAC2B51BD46925DED02509E7915F00006776AC5859CF7A20~plp1zaFdpXtYLf8weCUutyV+qM2pvbRJTHeUPl5W83UaBA9xbhjS8cFhECxnAQ4XXE26wFWMx7qr5/zgkXdKE3lMlllVqWkFRBzT5/kJZAYeVcIJonmJfxms0HEj0Hu7WgP541M7F6/rCRt2e9TsmfbB/sGSgSlN7UMgk7ZVfiQGk5AGMRpivEPnqcKL3j+X05BdeVNvCUD9DmMQfxQZp9jD8fJHDwupKbe+/nIEVRmas=; edge_check=anyone%3Dtrue%2Cvisitor%3Dcheck; at_carnivalbrands=segments%3D5554399; aam_uuid=49219101422032194302258392854001707249; getLocale=%7B%22specialOffers%22%3A%22true%22%2C%22status%22%3A%22US%22%2C%22primaryCurrency%22%3A%22USD%22%2C%22country%22%3A%22US%22%2C%22countryPhone%22%3A%221-800-774-6237%22%2C%22isEU%22%3A%22false%22%2C%22brochures%22%3A%22true%22%2C%22lastUpdated%22%3A1487697509607%7D; mf_record_user=1; __atuvc=1%7C8; __atuvs=58ac7666fc540784000",
    "Connection": "keep-alive",
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Upgrade-Insecure-Requests': '1'
}
while deck <= 19:
    url = 'http://www.princess.com/getDeckJSON.do?&shipCode=MJ&version=0&deck=' + str(deck) + ''
    response = session.get(url=url, headers=headers).json()
    deck += 1
    cabins_array = response['cabins']
    if len(cabins_array) > 0:
        for c in cabins_array:
            responses.append(c)
for d in responses:
    all_cabins.add(str(d['deckNumber']) + ',' + str(d['categoryCode']) + ',' + str(d['text']))

final_count = {
    "deck1": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck2": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck3": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck4": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck5": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck6": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck7": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck8": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck9": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck10": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck11": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck12": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck13": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck14": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck15": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck16": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck17": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck18": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck19": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    }
}
for d in all_cabins:
    d = d.split(',')
    if d[0] == '1':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck1']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck1']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck1']['suite'] += 1
    if d[0] == '2':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck2']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck2']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck2']['suite'] += 1
    if d[0] == '3':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck3']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck3']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck3']['suite'] += 1
    if d[0] == '4':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck4']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck4']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck4']['suite'] += 1
    if d[0] == '5':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck5']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck5']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck5']['suite'] += 1
    if d[0] == '6':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck6']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck6']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck6']['suite'] += 1
    if d[0] == '7':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck7']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck7']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck7']['suite'] += 1
    if d[0] == '8':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck8']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck8']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck8']['suite'] += 1
    if d[0] == '9':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck9']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck9']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck9']['suite'] += 1
    if d[0] == '10':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck10']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck10']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck10']['suite'] += 1
    if d[0] == '11':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck11']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck11']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck11']['suite'] += 1
    if d[0] == '12':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck12']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck12']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck12']['suite'] += 1
    if d[0] == '13':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck13']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck13']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck13']['suite'] += 1
    if d[0] == '14':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck14']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck14']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck14']['suite'] += 1
    if d[0] == '15':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck15']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck15']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck15']['suite'] += 1
    if d[0] == '16':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck16']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck16']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck16']['suite'] += 1
    if d[0] == '17':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck17']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck17']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck17']['suite'] += 1
    if d[0] == '18':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck18']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck18']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck18']['suite'] += 1
    if d[0] == '19':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck19']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck19']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck19']['suite'] += 1
print("Majestic v0")
for k, v in final_count.items():
    if v['inside'] == 0 and v['oceanview'] == 0 and v['balcony'] == 0 and v['suite'] == 0:
        pass
    else:
        print(k, v)
deck = 1
responses = []
all_cabins = set()
headers = {
    "Host": "www.princess.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "AMCV_21C91F2F575539D07F000101%40AdobeOrg=2121618341%7CMCIDTS%7C17219%7CMCMID%7C49671028090519812502303589936345137365%7CMCAAMLH-1488302309%7C9%7CMCAAMB-1488302309%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1487704709s%7CNONE%7CMCAID%7CNONE; mbox=check#true#1487697570|session#6f787331475941c980ad4b2cacaa1045#1487699370|PC#6f787331475941c980ad4b2cacaa1045.20_84#1488907111; _aeu=QCQ=; _aes=QSE=; __utma=169354720.57759081.1487697510.1487697510.1487697510.1; __utmb=169354720.2.10.1487697510; __utmz=169354720.1487697510.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); s_dfa=crbrprincessprodus%2Ccrbrcarnivalbrandsprodus; s_ppn=pcl%3Aplanning%3Alearn_about_cruising; s_nr=1487697511727-New; gds=1487697511728; gds_s=First%20Visit; s_vnum=1488319200772%26vn%3D1; s_invisit=true; _ga=GA1.2.57759081.1487697510; ak_bmsc=8E4CEB0092F896BFEAC2B51BD46925DED02509E7915F00006776AC5859CF7A20~plp1zaFdpXtYLf8weCUutyV+qM2pvbRJTHeUPl5W83UaBA9xbhjS8cFhECxnAQ4XXE26wFWMx7qr5/zgkXdKE3lMlllVqWkFRBzT5/kJZAYeVcIJonmJfxms0HEj0Hu7WgP541M7F6/rCRt2e9TsmfbB/sGSgSlN7UMgk7ZVfiQGk5AGMRpivEPnqcKL3j+X05BdeVNvCUD9DmMQfxQZp9jD8fJHDwupKbe+/nIEVRmas=; edge_check=anyone%3Dtrue%2Cvisitor%3Dcheck; at_carnivalbrands=segments%3D5554399; aam_uuid=49219101422032194302258392854001707249; getLocale=%7B%22specialOffers%22%3A%22true%22%2C%22status%22%3A%22US%22%2C%22primaryCurrency%22%3A%22USD%22%2C%22country%22%3A%22US%22%2C%22countryPhone%22%3A%221-800-774-6237%22%2C%22isEU%22%3A%22false%22%2C%22brochures%22%3A%22true%22%2C%22lastUpdated%22%3A1487697509607%7D; mf_record_user=1; __atuvc=1%7C8; __atuvs=58ac7666fc540784000",
    "Connection": "keep-alive",
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Upgrade-Insecure-Requests': '1'
}
while deck <= 19:
    url = 'http://www.princess.com/getDeckJSON.do?&shipCode=MJ&version=1&deck=' + str(deck) + ''
    response = session.get(url=url, headers=headers).json()
    deck += 1
    cabins_array = response['cabins']
    if len(cabins_array) > 0:
        for c in cabins_array:
            responses.append(c)
for d in responses:
    all_cabins.add(str(d['deckNumber']) + ',' + str(d['categoryCode']) + ',' + str(d['text']))

final_count = {
    "deck1": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck2": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck3": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck4": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck5": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck6": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck7": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck8": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck9": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck10": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck11": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck12": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck13": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck14": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck15": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck16": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck17": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck18": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck19": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    }
}
for d in all_cabins:
    d = d.split(',')
    if d[0] == '1':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck1']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck1']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck1']['suite'] += 1
    if d[0] == '2':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck2']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck2']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck2']['suite'] += 1
    if d[0] == '3':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck3']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck3']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck3']['suite'] += 1
    if d[0] == '4':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck4']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck4']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck4']['suite'] += 1
    if d[0] == '5':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck5']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck5']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck5']['suite'] += 1
    if d[0] == '6':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck6']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck6']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck6']['suite'] += 1
    if d[0] == '7':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck7']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck7']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck7']['suite'] += 1
    if d[0] == '8':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck8']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck8']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck8']['suite'] += 1
    if d[0] == '9':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck9']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck9']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck9']['suite'] += 1
    if d[0] == '10':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck10']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck10']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck10']['suite'] += 1
    if d[0] == '11':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck11']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck11']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck11']['suite'] += 1
    if d[0] == '12':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck12']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck12']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck12']['suite'] += 1
    if d[0] == '13':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck13']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck13']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck13']['suite'] += 1
    if d[0] == '14':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck14']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck14']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck14']['suite'] += 1
    if d[0] == '15':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck15']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck15']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck15']['suite'] += 1
    if d[0] == '16':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck16']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck16']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck16']['suite'] += 1
    if d[0] == '17':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck17']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck17']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck17']['suite'] += 1
    if d[0] == '18':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck18']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck18']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck18']['suite'] += 1
    if d[0] == '19':
        if d[1] == 'D4' or d[1] == 'DF' or d[1] == 'DW' or d[1] == 'BV' or d[1] == 'BF' or d[1] == 'BW' or d[1] == 'DZ' or d[1] == 'BY' or d[1] == 'BB' or d[1] == 'DE' or d[1] == 'BD' or d[1] == 'BE' or d[1] == 'DA' or d[1] == 'BA' or d[1] == 'DB' or d[1] == 'DD' or d[1] == 'BC' or d[1] == 'DC':
            final_count['deck19']['balcony'] += 1
        elif d[1] == 'IB' or d[1] == 'IC' or d[1] == 'IF' or d[1] == 'IA' or d[1] == 'IE' or d[1] == 'ID':
            final_count['deck19']['inside'] += 1
        elif d[1] == 'MC' or d[1] == 'MF' or d[1] == 'S2' or d[1] == 'S3' or d[1] == 'S5' or d[1] == 'MA' or d[1] == 'MB' or d[1] == 'M1' or d[1] == 'ME' or d[1] == 'S4' or d[1] == 'M6' or d[1] == 'MC':
            final_count['deck19']['suite'] += 1
print("Majestic v1")
for k, v in final_count.items():
    if v['inside'] == 0 and v['oceanview'] == 0 and v['balcony'] == 0 and v['suite'] == 0:
        pass
    else:
        print(k, v)
