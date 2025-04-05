# 1. 가격 변동이 있는 매물 찾기 (priceChangeState != "SAME", isPriceModification = true) TODO 실제 이런 데이터가 정말 있나 알아보기. 왜냐하면 매물은 하루 지나면 내려가고 다시 올리면 새로운 데이터처럼 보이기 떄문...!
# 2. 오늘자 올라온 매물 찾기
# 3. 관심 매물로 설정해 놓은 매물 찾기
from datetime import datetime

import requests

from real_estate_models import RealEstateResponseResult, RealEstateArticle

url = "https://new.land.naver.com/api/articles/complex/45"

params = {
    "realEstateType": "APT:ABYG:JGC:PRE",
    "tradeType": "",
    "tag": ":::::::",
    "rentPriceMin": "0",
    "rentPriceMax": "900000000",
    "priceMin": "0",
    "priceMax": "900000000",
    "areaMin": "0",
    "areaMax": "900000000",
    "priceType": "RETAIL",
    "showArticle": "false",
    "sameAddressGroup": "false",
    "type": "list",
    "page": "1",
    "complexNo": "45",
    "order": "rank"
}

headers = {
    "Accept": "*/*",
    "Accept-Language": "ko,ko-KR;q=0.9,en;q=0.8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDM4NTMxNjYsImV4cCI6MTc0Mzg2Mzk2Nn0.cy2U1u14z33saXnRSU4Q_HqBlMHwczw43Xyp7pxwT0k",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": "https://new.land.naver.com/complexes/45?ms=37.492882,126.95597450000001,17&a=APT:ABYG:JGC:PRE&e=RETAIL&articleNo=2517668440",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Ch-Ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"'
}

cookies = {
    "NNB": "VP3XGWS36FMWE",
    "NAC": "K89yBMgTabXL",
    "_fbp": "fb.1.1742191207561.914887589491497572",
    "_fwb": "123HbBdYL8KCi0VjRCL6aHR.1743160962628",
    "landHomeFlashUseYn": "Y",
    "NACT": "1",
    "_ga": "GA1.1.1958796966.1743818267",
    "nhn.realestate.article.rlet_type_cd": "A01",
    "nhn.realestate.article.trade_type_cd": '""',
    "_ga_451MFZ9CFM": "GS1.1.1743822113.2.0.1743822117.0.0.0",
    "nid_inf": "2143718966",
    "NID_JKL": "737dMh0Za20ebcX8gaEC7n0qBNDJQSkuysSSVsJG/Dk=",
    "REALESTATE": "Sat Apr 05 2025 20:39:26 GMT+0900 (Korean Standard Time)",
    "BUC": "_GdTPCptnzy5nxNJ7aJRMe7yzDemFSVX_RkcnBBH8Dk="
}

response = requests.get(url, headers=headers, params=params, cookies=cookies)
print(response)
if response.status_code == 200:
    data = response.json()
    print(data)
    try:
        articles = [
            RealEstateArticle(**article)
            for article in data["articleList"]
        ]

        result = RealEstateResponseResult(
            isMoreData=data["isMoreData"],
            articleList=data["articleList"],
        )

        for article in result.articleList:
            print(
                f"[{datetime.strptime(article.articleConfirmYmd, '%Y%m%d').strftime('%Y-%m-%d')}] "
                f"🏠 {article.articleName} {article.buildingName} "
                f"{article.floorInfo.split('/')[1]}층 {article.floorInfo.split('/')[0]}호 "
                f"💵 {article.dealOrWarrantPrc}"
            )
    except Exception as e:
        print("매핑 실패: ", e)

else:
    print("요청 실패: ", response.status_code)
