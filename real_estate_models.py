from dataclasses import dataclass
from typing import List, Optional

@dataclass
class RealEstateArticle:
    articleNo: str # 매물 번호
    articleName: str # 매물 제목
    articleStatus: str # 매물 상태 (예: 활성, 비활성)
    realEstateTypeCode: str # 부동산 유형 코드 (예: "APT")
    realEstateTypeName: str # 부동산 유형 이름 (예: "아파트", "오피스텔")
    articleRealEstateTypeCode: str # 매물의 부동산 유형 코드 (예: "A01")
    articleRealEstateTypeName: str # 매물의 부동산 유형 이름 (예: "아파트")
    tradeTypeCode: str # 거래 유형 코드 (예: "A1"(매매))
    tradeTypeName: str # 거래 유형 이름 (예: "매매")
    verificationTypeCode: str # 검증 유형 코드(예: "OWNER", "NDOC1", "DOC", "DOCV2")
    floorInfo: str # 층 정보 (예: "2/15")
    priceChangeState: str # 가격 변동 상태 (예: "SAME")
    isPriceModification: bool # 가격 수정 여부 (예: true, false)
    dealOrWarrantPrc: str # 거래가 또는 보증금
    areaName: str # 지역 이름 (예: "76", "94")
    area1: float # 전용 면적 (㎡)
    area2: float # 공급 면적 (㎡)
    direction: str # 방향 (예: "남향")
    articleConfirmYmd: str # 매물 등록일 (예: "20250404")
    siteImageCount: int # 현장 사진 수
    articleFeatureDesc: str # 매물 특징 설명 (예: "갭투자가능 올수리됨 전세43000만원 숲세권동 조용하고 주차용이함")
    tagList: List[str] # 태그 리스트 (예: ["25년이상","대단지","방세개","화장실한개"])
    buildingName: str # 건물명 (예: "125동")
    sameAddrCnt: int # 동일 주소 매물 수
    sameAddrDirectCnt: int # 동일 주소 직거래 수
    sameAddrMaxPrc: str # 동일 주소 최고가 (예: "7억 2,000")
    sameAddrMinPrc: str # 동일 주소 최저가 (예: "4억")
    cpid: str # 외부 부동산 정보 제공업체 ID (예: "bizmk", "NEONET")
    cpName: str # 외부 부동산 정보 제공업체 이름 (예: "부동산뱅크")
    cpPcArticleUrl: str # 외부 정보 제공 업체 매물 상세 URL (예: "http://land.mk.co.kr/rd/rd.php?UID=2517721034")
    latitude: str # 위도 (예: "37.492747")
    longitude: str # 경도 (예: "126.961048")
    isLocationShow: bool # 위치 노출 여부
    realtorName: str # 중개사명 (예: "현대공인중개사사무소")
    realtorId: str # 중개사 ID (예: "hd8761010")
    tradeCheckedByOwner: bool # 집주인 확인 여부
    isDirectTrade: bool # 직거래 여부
    isInterest: bool # 관심 매물 여부
    isComplex: bool # 단지형 여부

@dataclass
class RealEstateResponseResult:
    articles: List[RealEstateArticle]
    hasMore: bool
    page: int
    totalCount: int

@dataclass
class RealEstateApiResponse:
    result: RealEstateResponseResult


