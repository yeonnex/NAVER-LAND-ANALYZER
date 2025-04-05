## 1. API 기본 구조

>`GET` https://news.land.naver.com/api/articles/complex/{complexNo}

- complexNo=45
    - 단지 번호
    - 예: 관악현대아파트 단지 ID = 45

```shell
curl 'https://new.land.naver.com/api/articles/complex/45?realEstateType=ABYG%3AJGC&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears=&recentlyBuildYears=&minHouseHoldCount=&maxHouseHoldCount=&showArticle=false&sameAddressGroup=false&minMaintenanceCost=&maxMaintenanceCost=&priceType=RETAIL&directions=&page=12&complexNo=45&buildingNos=&areaNos=&type=list&order=rank' \
  -H 'accept: */*' \
  -H 'accept-language: ko,ko-KR;q=0.9,en;q=0.8' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDM4MTgyOTgsImV4cCI6MTc0MzgyOTA5OH0.4aB67rRa2wLbNFv8qwc-5FWvhRI6IClclubJHNfKWa4' \
  -H 'cache-control: no-cache' \
  -H 'pragma: no-cache' \
  -H 'referer: https://new.land.naver.com/complexes/45?ms=37.4893705,126.9620899,15&a=ABYG:JGC&e=RETAIL' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
```
## 2. 주요 Query 파라미터 분석
![img.png](img.png)

| 파라미터                                       | 설명             | 예시                                                                                                                                           |
| ------------------------------------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `realEstateType`                           | 부동산 종류         | `APT` → `아파트`<br>`JGC` → `재건축`<br>`ABYG`→ `아파트 분양권`<br>`PRE`→ `분양중·예정`<br>빈 값이면 전체                                                           |
| `tradeType`                                | 매매 유형          | `A1`→`매매`<br>`B1` → `전세`<br>`B2`→`월세`<br>빈 값이면 전체(전세/월세/매매 포함)                                                                               |
| `priceMin`, `priceMax`                     | 매매 가격 범위       | 예: `0 ~ 900000000` (0 ~ 9억)                                                                                                                  |
| `areaMin`, `areaMax`                       | 공급 면적 범위 (㎡)   | `areaMin: 0 areaMax: 33` → `~10평`<br><br>`areaMin: 66, areaMax: 132` → `20~40평`                                                              |
| `minHouseHoldCount`, `maxHouseHoldCount`   | 세대 수 필터        | `minHouseHoldCount: 1000, maxHouseHoldCount: 2000` → `1000 ~2000세대`                                                                          |
| `minMaintenanceCost`, `maxMaintenanceCost` | 관리비 필터         |                                                                                                                                              |
| `priceType`                                | 가격 종류          | `REAL`→ `국토교통부 실거래가 기준`<br>`RETAIL`→`매물가격 기준`                                                                                                |
| `directions`                               | 방향 필터(남향/서향 등) | `SS:EE:WN:ES:WW`→`남,동,북서,남동,서`                                                                                                               |
| `page`                                     | 페이지 번호         | `3` → `3페이지`                                                                                                                                 |
| `complexNo`                                | 단지 번호          | `45` → `서울시 관악구 봉천동 관악현대아파트`                                                                                                                 |
| `buildingNos`, `areaNos`                   | 특정 동이나 평형 번호   |                                                                                                                                              |
| `order`                                    | 정렬 조건          | `rank` → `인기순`                                                                                                                               |
| `showArticle`                              | 매물 보여줄지        | `false`                                                                                                                                      |
| `tag`                                      | 층수             | `::::ONEFLOOR::::` → `1층`<br>`::::LOWFLOOR::::` → `저층`<br>`::::MIDFLOOR::::` → `중간층`<br>`::::HIGHFLOOR::::`→`고층`<br>`::::TOPFLOOR::::` →`탑층` |
|                                            | 융자금            | `:::::LOWLOAN:::`→`융자금 30%미만`<br>`:::::NOLOAN:::`→ `융자금 없음`                                                                                  |
|                                            | 방 개수           | `:THREEROOM:::::::`→ `방 3개`<br>`:FOURROOM:::::::`→ `방 4개 이상`                                                                                 |
|                                            | 욕실수            | `::TOWBATH::::::`→`욕실 2개`<br>`::FOURBATH::::::`→`욕실 4개 이상`                                                                                   |
|                                            | 기타             | `:::::::::DUPLEX`→`복층`<br>`:::::::::ALLREPAIR`→`올수리`<br>`:::::::::FASTSELL`→`급매`<br>`:::::::::RENTHUG`→`세안고`                                 |
