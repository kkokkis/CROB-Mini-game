from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import random
import json
import os
import asyncio
from typing import Optional

app = Flask('')

@app.route('/')
def home():
    return "체크"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

유저리스트 = ["신지", "플레", "꼬끼스", "리보", "gwb", "한정민", "데스틴", "식덕", "김노트", "소진", "지렌"]
#쿠키, 펫, 보물 리스트
쿠키리스트 = [
    "용감한 쿠키", "명랑한 쿠키", "딸기맛 쿠키", "보더맛 쿠키", "체리맛 쿠키", "천사맛 쿠키", "피스타치오맛 쿠키",
    "버블껌맛 쿠키", "근육맛 쿠키", "락스타맛 쿠키", "좀비맛 쿠키", "소다맛 쿠키", "파일럿맛 쿠키",
    "악마맛 쿠키", "닌자맛 쿠키", "연금술사맛 쿠키", "뱀파이어맛 쿠키", "치즈케이크맛 쿠키", "용사맛 쿠키",
    "공주맛 쿠키", "치어리더맛 쿠키", "에일리언 도넛", "히어로맛 쿠키", "요가맛 쿠키", "팝콘맛 쿠키",
    "정글전사 쿠키", "해적맛 쿠키", "피겨여왕맛 쿠키", "웨어울프맛 쿠키", "구미호맛 쿠키", "마법사맛 쿠키",
    "눈설탕맛 쿠키", "다크초코 쿠키", "민트초코 쿠키", "코코아맛 쿠키", "팬케이크맛 쿠키", "키위맛 쿠키",
    "허브맛 쿠키", "요정맛 쿠키", "슈크림맛 쿠키", "박하사탕맛 쿠키", "닥터 와사비 쿠키", "머스터드맛 쿠키",
    "오렌지맛 쿠키", "달토끼맛 쿠키", "말차맛 쿠키", "마카롱맛 쿠키", "음유시인맛 쿠키", "스파클링맛 쿠키",
    "단팥맛 쿠키", "아이스캔디맛 쿠키", "핑크초코 쿠키", "아보카도맛 쿠키", "벚꽃맛 쿠키", "휘핑크림맛 쿠키",
    "화이트초코 쿠키", "탐험가맛 쿠키", "블랙베리맛 쿠키", "칠리맛 쿠키", "홍고추맛 쿠키", "자몽맛 쿠키",
    "레몬맛 쿠키", "소금맛 쿠키", "라임맛 쿠키", "오징어먹물맛 쿠키", "석류맛 쿠키", "디제이맛 쿠키",
    "롤케이크맛 쿠키", "마시멜로맛 쿠키", "시나몬맛 쿠키", "무화과맛 쿠키", "솜사탕맛 쿠키", "당근맛 쿠키",
    "비트맛 쿠키", "자색고구마맛 쿠키", "우유맛 쿠키", "이온맛 쿠키로봇", "사이보그맛 쿠키", "다이노사워 쿠키",
    "자두맛 쿠키", "복숭아맛 쿠키", "요거트크림맛 쿠키", "호두맛 쿠키", "괴도맛 쿠키", "마라맛 쿠키",
    "생일케이크맛 쿠키", "폭죽맛 쿠키", "밤톨맛 쿠키", "푸딩맛 쿠키", "예언자맛 쿠키", "블루파이맛 쿠키",
    "라즈베리 무스맛 쿠키", "장미맛 쿠키", "시금치맛 쿠키", "샌드위치맛 쿠키", "망고맛 쿠키", "풋사과맛 쿠키",
    "크림 유니콘 쿠키", "대추맛 쿠키", "대파맛 쿠키", "캡틴 아이스 쿠키", "샤벳상어맛 쿠키", "랍스터맛 쿠키",
    "모카가오리맛 쿠키", "트러플맛 쿠키", "양파맛 쿠키", "메론빵맛 쿠키", "고블린맛 쿠키", "크루아상맛 쿠키",
    "팝핑 캔디맛 쿠키", "샤이닝글리터맛 쿠키", "체스초코 쿠키", "얼그레이맛 쿠키", "쿠키멀즈", "츄러스맛 쿠키",
    "구슬아이스맛 쿠키", "바나나맛 쿠키", "스타후르츠맛 쿠키", "감초맛 쿠키", "파프리카맛 쿠키", "알로에맛 쿠키",
    "버터프레첼맛 쿠키", "아몬드맛 쿠키", "라일락맛 쿠키", "전갈맛 쿠키", "더덕꽃맛 쿠키", "인삼맛 쿠키",
    "수국맛 쿠키", "사워벨트맛 쿠키", "쇼콜라봉봉맛 쿠키", "앰버슈가맛 쿠키", "슈가글라스맛 쿠키", "에그노그맛 쿠키",
    "티라미수맛 쿠키", "스트링젤리맛 쿠키", "밀랍맛 쿠키", "크로우베리맛 쿠키", "닥터 뼈다귀 쿠키", "피자맛 쿠키",
    "람부탄맛 쿠키", "앵두맛 쿠키", "초코볼맛 쿠키", "페페론치노맛 쿠키", "콜리플라워맛 쿠키", "스네이크후르츠맛 쿠키",
    "흑마늘맛 쿠키", "화이트고스트맛 쿠키", "매작과맛 쿠키", "의적맛 쿠키", "지초맛 쿠키", "독버섯맛 쿠키",
    "난초맛 쿠키", "롤리팝맛 쿠키", "버터베어맛 쿠키", "커피캔디맛 쿠키", "바게트맛 쿠키", "하바네로맛 쿠키",
    "파스텔머랭맛 쿠키", "커런트크림맛 쿠키", "센티피드맛 쿠키", "블랙페퍼맛 쿠키", "물망초 다이노 쿠키",
    "감자맛 쿠키", "샤인머스캣맛 쿠키", "전기장어맛 쿠키", "랑그드샤맛 쿠키", "카푸치노맛 쿠키", "옥춘맛 쿠키",
    "김맛 쿠키", "블루슬러시맛 쿠키", "카놀리맛 쿠키", "스모어맛 쿠키", "슈톨렌맛 쿠키", "딸기생크림맛 쿠키",
    "우주비행사맛 쿠키", "감귤탕후루맛 쿠키", "구운달걀맛 쿠키", "초코바맛 쿠키", "버터오징어맛 쿠키",
    "슈니발렌맛 쿠키", "마블식빵맛 쿠키", "분모자맛 쿠키", "포두부맛 쿠키", "딸기초코스틱맛 쿠키",
    "민트웨이퍼맛 쿠키", "크림소다맛 쿠키", "체리콜라맛 쿠키", "레드판나코타맛 쿠키", "블랙누들맛 쿠키",
    "블랙올리브맛 쿠키", "캔디콘맛 쿠키", "키친싱크파이맛 쿠키", "페퍼누스맛 쿠키", "엘더베리맛 쿠키",
    "황소자리맛 쿠키", "유과맛 쿠키", "방울엿맛 쿠키", "에스트로넛", "생토노레맛 쿠키", "생크림담비 쿠키", "바크초코 쿠키", "달빛술사 쿠키", "바람궁수 쿠키", "바다요정 쿠키", "불꽃정령 쿠키",
    "어둠마녀 쿠키", "천년나무 쿠키", "용과 드래곤 쿠키", "파인 드래곤 쿠키", "시간지기 쿠키",
    "백련 드래곤 쿠키", "리치 드래곤 쿠키", "용안 드래곤 쿠키", "심해군주 쿠키", "설탕백조 쿠키",
    "자일리톨 노바 쿠키", "설탕흑조 쿠키", "꿈길잡이 쿠키", "스테비아 노바 쿠키", "헬로키티", "미미",
    "쿠키로이드", "커피맛 쿠키", "버터크림초코 쿠키", "특전사맛 쿠키", "하츄핑", "빤짝핑", "레전더리 픽업 스킨을 뽑는 것보다 낮은 확률로 나온 꽝"
] # < cookie
펫리스트 = [
    "초코방울", "치즈방울", "럭키다이스", "포켓딸기", "스포트라이트", "브레인껌", "미니 잭슨 2호", "로켓폭죽",
    "반딧불이", "천상의별", "쌍둥이덤벨", "조각레몬", "구름펠리칸", "불꽃박쥐", "꼬마유령", "생명저울", "참나무 주스통",
    "치즈뭉치 고양이", "용의꼬리", "공주의 장신구", "반짝이볼", "치즈펄 핸드백", "스페이스 미니볼", "젤리코 큐브",
    "샌드형 스피커", "까칠한 토마토", "야생 고기왕", "낄낄 폭탄", "눈꽃송이", "털뭉치 멍뭉이", "여우구슬", "마법사전",
    "스노우 글로브", "영혼 투구", "미스터 파솔라시", "마시멜로 햄찌", "팬케이크 원반", "키위새", "허브티팟",
    "꽃봉오리", "도토리 부엉이", "종이배 선원", "와사비 문어", "핫도그도그", "어린쥐", "달절구", "녹차티백",
    "캐스터네츠", "통나무케이크", "보타이보틀", "찹쌀 하프물범", "톡톡캔디통", "핑크캔디", "아포카포", "홍차 찻잔",
    "크림로즈", "회중시계 심판", "배낭이", "집사 유령", "배드페퍼", "파프리카 샌드백", "자몽텀블러", "레몬 전지",
    "고무튜브", "미스터 삑", "방울문어", "루비 석류", "젤리패드", "라이트 형제", "꼬꼬마 아코디언", "시나몬롤 토끼",
    "열매사슴", "솜사탕 비둘기", "당근케이크 토끼", "새싹 비트", "화나구마", "우유보틀 엔젤", "곰돌이온",
    "BB 건전지", "팝핑 용알", "사부 건자두", "판다만두", "요술램프", "조수 테디", "치즈크럼블 고양이", "막지마라",
    "용과리", "파티풍선", "뿅뿅게임기", "왕밤도치", "루돌프벨", "보라보라 향초", "앤틱북마크", "푸들베리",
    "블러디로즈", "완두벌레", "오이샌드", "망고부리새", "파인 여우원숭이", "토끼사과", "머랭뿔", "식지 않는 찻잔",
    "죽순대감", "세일러닻", "해적 휠리엄", "집게초롱", "등불해파리", "반짇고치", "양파 물고기", "멜롱두더지",
    "우걱우걱 상자", "꽃니바퀴", "엔젤팝봉", "프로듀서 마이크", "누가캔디 나이트", "찻잔받침", "퓨어크림", "꿈츄리",
    "구슬마술컵", "사바나나 사자", "꿀잠양", "뱃냥이", "프리프리봇", "알로드론", "버터레용", "초코고양이 네로",
    "팔랑일락", "눈물독독병", "꾸러기약", "인삼이라지", "꽃개구리", "연근이", "파우치사우루스", "봉봉버드",
    "벌꿀벌", "슈가딜라이트", "산타모자", "랜턴컵 티라미수", "스마일 탐지기", "실링베어", "새알브로치",
    "두근두근 모니터", "피자 핫소스", "복슬이람", "파닥눈이", "오동통통볼", "슈퍼파워 드링크", "용암전갈",
    "콜리콜리", "비늘부채", "용란조개", "소원인형", "쨍강거울", "약과 찹사리", "바람이", "풀무늬다람쥐",
    "개굴버섯구리", "꽃잎사마귀", "신사쥐", "산타양말", "왈칵잉크", "펜이로소이다", "맵새", "크림티즈",
    "블랙핀도치", "미스 도레미", "보물병", "후추통갈이", "별꽃피쉬", "씨앗이", "디렉터 큐", "번개장어",
    "가시고기", "사건파일", "카프림치노", "색동주머니", "깨비불", "얼음과자새", "각설탕엔젤", "생수통",
    "캠퍼 스텐", "호랑가시사탕", "산타장갑", "샌드위성", "닥터리톨", "꼭지귤", "달걀머리새", "누가 데일리 밴드",
    "골든옥토퍼스상", "암모나이트롤", "식빵아지", "탱글둥지", "메롱 포두부탈", "쿵짝스틱", "웨이퍼 메트로놈",
    "뽀글방울", "팡팡버블", "앵앵베리버드", "흑설탕거울", "단무지사장", "올리브 레이저", "폭죽콘", "매직파이오븐",
    "쿨쿨달", "별사탕 방울", "별조각병", "삐리리 피리뿔", "철썩 방망이", "멍멍 보부상", "네이처셀", "통역찌",
    "콩알 뻐꾸기 시장", "쑥쑥 크림우유병", "어둠 망령", "마그마불새", "에메랄드 수호골렘", "푸른 회오리용", "눈폭풍 예티",
    "별빛 드림캐쳐", "파도방울", "풀잎개비", "영원한 어둠의 눈", "무한바퀴", "천년옥사슴", "호불호랑이",
    "연꽃비늘룡", "용과화룡검", "황금방패룡", "금패용안석", "드래곤하트뱃", "키티의 빨간사과", "미미의 노란꽃",
    "플레이블록", "생크림 모카커피", "뭉치유니콘", "건빵 보급병", "핑핑스타", "빤짝구름"
] # <- pet
보물리스트 = [
    "방어막 버블건", "젤리 토핑 컵케이크", "곰젤리 아이스크림", "롤리팝 스케이트", "코인 장식 은왕관", "미니 자석 로봇",
    "아몬드 초코칩 망치", "캔디 다이너마이트", "젤리 씨앗 크리스탈 항아리", "얼음 진주 산호초", "부활의 붉은 알",
    "어둠의 캔디케인 마법 지팡이", "은화꽃 코인 브로치", "부활의 날개 젤리", "완벽한 착지 교본", "다이너마이트 보물상자",
    "무지개곰젤리 롤케이크", "신성한 오로라 영액", "이글이글 별똥별 캔디", "테이프껌 스프링 슈즈", "황금코인 폭죽상자",
    "곰젤리 부메랑", "당근푸딩 트램폴린", "왕곰젤리 보석반지", "얼음 꽁꽁 초코케이크", "성스러운 수호방패",
    "저주받은 영웅의 성배", "핫핫 스파이시 터보엔진", "배부른 젤리퐁퐁 점핑 젤리말", "꿈꾸는 곰젤리 메달", "파도방울 소라껍데기",
    "황금치즈 곡괭이", "불끈 파워 에너지드링크", "볼통통 곰젤리 저금통", "별사탕 우주시계", "행운의 클로버 귀걸이",
    "럭셔리 레드카펫", "완벽한 보물지도", "원혼이 잠든 마법거울", "기적의 초록나무 영양제", "알록달록 무지개 헤드셋",
    "태고의 천둥북", "색색 종이비행기", "판타스틱 매직 트럼프 카드", "금지된 마법서 조각", "퐁당 무화과 에이드",
    "평화의 비둘기 만쥬", "토네이도 당근로켓", "슈퍼 자이언트 강낭콩", "불타는 불고구마", "우유속에 초코샌드",
    "마이크로 이온 칩", "일렉트릭쇼크 큐브", "잠자는 숲속의 아기공룡", "불꽃 고리 반지", "수련의 두루마리",
    "신선 복숭아씨앗", "신비의 마법 양탄자", "호두까기 망치", "마그마 펜듈럼", "젤리크림 거품기", "만능 찰칵 카메라",
    "보라광선 수정구슬", "명예로운 기사의 검", "동글연두 완두콩총", "생생 생과일주스", "사과사탕 풍선", "영웅의 작은 나무말",
    "눈꽃소복 얼음곰", "영롱한 진주조개", "상냥한 유령 곰인형", "잘 익은 멜론 다이너마이트", "시간 수습 가위", "팝팝 포토카드",
    "우아한 마법빗자루", "검은바람 화살통", "알사탕 피에로 슈즈", "작은 별 무드등", "최신형 파프북", "무지개젤리 물감",
    "전설의 거울눈", "만병통치약 절구", "쑥쑥 꽃뿌리개", "패셔니스타 스포트라이트", "낙원 나침반", "딸랑딸랑 루돌프 리스",
    "시간 혼돈 가위", "곰젤리 칭찬 도장", "튼튼 종합영양젤리", "람독수리 사냥장갑", "짝짝짝 응원수술", "어린 용의 발톱",
    "유령퇴치 부적 스티커", "삼색 말랑몰랑떡", "단짝나비 브로치", "별나라 비행기", "자동출력 타자기", "타오르는 흑요석",
    "보들보들 털실공", "보글보글 해마물총", "풍년 허수아비", "버블버블 노란 잠수함", "대왕 대법전", "밤나들이 청사초롱",
    "오로라 설탕 깃털", "골드베리방울", "젤리팝 물로켓", "곰젤리 탕후루", "냠냠믹스팝콘", "훌쩍 코코야자나무", "붉은뿔가면",
    "퍼펙트 스위트 기타", "거룩한 태양의 검", "호숫가의 설탕장미", "해피해피 잭오랜턴", "꿈나라 여행용 베개",
    "별 나와라 지팡이", "찹쌀과자 꾸러미", "온실 속 희망의 꽃", "유리사탕 플라네타륨", "푸르른 미래의 씨앗", "불꽃의 정수",
    "생명의 정수", "영원한 꿈의 램프", "끝없는 소원의 유성우", "빛과 어둠의 모래시계", "초대형 미확인 비행도넛",
    "엄마의 애플파이", "정성으로 만든 키티 도시락", "키티의 달콤한 캔디상자", "견고한 우정 반지", "마음을 나눈 단짝 펜던트", "위대한 결전의 창"
] #treasure

cookie_list_en = [
    "Lollipop Cookie", "Butterbear Cookie", "Coffee Candy Cookie", "Baguette Cookie", "Habanero Cookie",
    "Pastel Meringue Cookie", "Currant Cream Cookie", "Centipede Cookie", "Peppercorn Cookie",
    "Pond Dino Cookie", "Potato Cookie", "Shine Muscat Cookie", "Electric Eel Cookie",
    "Langue de Chat Cookie", "Cappuccino Cookie", "Okchun Cookie", "Gim Cookie", "Blue Slushy Cookie",
    "Cannoli Cookie", "S'more Cookie", "Stollen Cookie", "Strawberry Cream Cookie", "Astronaut Cookie",
    "Tangerine Tanghulu Cookie", "Sauna Egg Cookie", "Choco Bar Cookie", "Butter Squid Cookie",
    "Schneeball Cookie", "Marble Bread Cookie", "Starch Noodle Cookie", "Flat Tofu Cookie",
    "Strawberry Stick Cookie", "Mint Wafer Cookie", "Cream Soda Cookie", "Cherry Cola Cookie",
    "Red Panna Cotta Cookie", "Agent Jjajang Cookie", "Agent Olive Cookie", "Candy Corn Cookie",
    "Everything Pie Cookie", "Peppernut Cookie", "Elderberry Cookie", "Taurus Cookie", "Yugwa Cookie",
    "Yeot Cookie", "Astronuts", "Caramel Choux Cookie", "Cream Ferret Cookie", "Moonlight Cookie",
    "Wind Archer Cookie", "Sea Fairy Cookie", "Fire Spirit Cookie", "Dark Enchantress Cookie",
    "Millennial Tree Cookie", "Pitaya Dragon Cookie", "Ananas Dragon Cookie", "Timekeeper Cookie",
    "Lotus Dragon Cookie", "Lychee Dragon Cookie", "Longan Dragon Cookie", "Abyss Monarch Cookie",
    "Sugar Swan Cookie", "Xylitol Nova Cookie", "Black Sugar Swan Cookie", "Dreamweaver Cookie",
    "Stevia Nova Cookie", "GingerBrave", "GingerBright", "Strawberry Cookie", "Skater Cookie",
    "Zombie Cookie", "Angel Cookie", "Muscle Cookie", "Pilot Cookie", "Ninja Cookie", "Soda Cookie",
    "Rockstar Cookie", "Devil Cookie", "Cherry Cookie", "Alchemist Cookie", "Gumball Cookie",
    "Pistachio Cookie", "Vampire Cookie", "Cheesecake Cookie", "Knight Cookie", "Princess Cookie",
    "Cheerleader Cookie", "Heartsping", "Twinkleping", "Hello Kitty", "Mimmy", "Cookiedroid",
    "Coffee Cookie", "Buttercream Choco Cookie", "Special Force Cookie", "Space Doughnut",
    "Hero Cookie", "Skating Queen Cookie", "Yoga Cookie", "Kumiho Cookie", "Pirate Cookie",
    "Popcorn Cookie", "Werewolf Cookie", "Snow Sugar Cookie", "Wizard Cookie", "Tiger Lily Cookie",
    "Dark Choco Cookie", "Mint Choco Cookie", "Fairy Cookie", "Cocoa Cookie", "Pancake Cookie",
    "Kiwi Cookie", "Herb Cookie", "Cream Puff Cookie", "Peppermint Cookie", "Dr. Wasabi Cookie",
    "Mustard Cookie", "Orange Cookie", "Moon Rabbit Cookie", "Matcha Cookie", "Macaron Cookie",
    "Carol Cookie", "Sparkling Cookie", "Red Bean Cookie", "Ice Candy Cookie", "Pink Choco Cookie",
    "Avocado Cookie", "Cherry Blossom Cookie", "Whipped Cream Cookie", "White Choco Cookie",
    "Adventurer Cookie", "Blackberry Cookie", "Chili Pepper Cookie", "Red Pepper Cookie",
    "Grapefruit Cookie", "Lemon Cookie", "Salt Cookie", "Lime Cookie", "Squid Ink Cookie",
    "Pomegranate Cookie", "DJ Cookie", "Roll Cake Cookie", "Marshmallow Cookie", "Cinnamon Cookie",
    "Fig Cookie", "Cotton Candy Cookie", "Carrot Cookie", "Beet Cookie", "Purple Yam Cookie",
    "Milk Cookie", "Ion Cookie Robot", "Cyborg Cookie", "Dino-Sour Cookie", "Plum Cookie",
    "Peach Cookie", "Yogurt Cream Cookie", "Walnut Cookie", "Roguefort Cookie", "Mala Sauce Cookie",
    "Birthday Cake Cookie", "Firecracker Cookie", "Chestnut Cookie", "Pudding Cookie",
    "Prophet Cookie", "Blueberry Pie Cookie", "Raspberry Mousse Cookie", "Rose Cookie",
    "Spinach Cookie", "Sandwich Cookie", "Mango Cookie", "Apple Cookie", "Cream Unicorn Cookie",
    "General Jujube Cookie", "Leek Cookie", "Captain Ice Cookie", "Sorbet Shark Cookie",
    "Lobster Cookie", "Mocha Ray Cookie", "Truffle Cookie", "Onion Cookie", "Melon Bun Cookie",
    "Goblin Cookie", "Croissant Cookie", "Popping Candy Cookie", "Shining Glitter Cookie",
    "Chess Choco Cookie", "Earl Grey Cookie", "Cookiemals", "Churro Cookie", "Ice Juggler Cookie",
    "Banana Cookie", "Starfruit Cookie", "Licorice Cookie", "Bell Pepper Cookie", "Aloe Cookie",
    "Butter Pretzel Cookie", "Almond Cookie", "Lilac Cookie", "Scorpion Cookie", "Bellflower Cookie",
    "Ginseng Cookie", "Hydrangea Cookie", "Sour Belt Cookie", "Chocolate Bonbon Cookie",
    "Amber Sugar Cookie", "Sugar Glass Cookie", "Eggnog Cookie", "Tiramisu Cookie",
    "String Gummy Cookie", "Candlelight Cookie", "Crowberry Cookie", "Dr. Bones Cookie",
    "Pizza Cookie", "Rambutan Cookie", "Cherry Ball Cookie", "Choco Ball Cookie", "Peperoncino Cookie",
    "Cauliflower Cookie", "Snake Fruit Cookie", "Black Garlic Cookie", "White Ghost Cookie",
    "Vagabond Cookie", "Rebel Cookie", "Lilybell Cookie", "Poison Mushroom Cookie", "Blue Lily Cookie", "A dud with a lower chance of getting a legendary pickup skin"
]

pet_list_en = [
    "Lollipop pet", "Butterbear pet", "Coffee Candy pet", "Baguette pet", "Habanero pet",
    "Pastel Meringue pet", "Currant Cream pet", "Centipede pet", "Peppercorn pet",
    "Pond Dino pet", "Potato pet", "Shine Muscat pet", "Electric Eel pet", "Langue de Chat pet",
    "Cappuccino pet", "Okchun pet", "Gim pet", "Blue Slushy pet", "Cannoli pet", "S'more pet",
    "Stollen pet", "Strawberry Cream pet", "Astronaut pet", "Tangerine Tanghulu pet",
    "Sauna Egg pet", "Choco Bar pet", "Butter Squid pet", "Schneeball pet", "Marble Bread pet",
    "Starch Noodle pet", "Flat Tofu pet", "Strawberry Stick pet", "Mint Wafer pet",
    "Cream Soda pet", "Cherry Cola pet", "Red Panna Cotta pet", "Agent Jjajang pet",
    "Agent Olive pet", "Candy Corn pet", "Everything Pie pet", "Peppernut pet",
    "Elderberry pet", "Taurus pet", "Yugwa pet", "Yeot pet", "Astronuts pet",
    "Caramel Choux pet", "Cream Ferret pet", "Moonlight pet", "Wind Archer pet",
    "Sea Fairy pet", "Fire Spirit pet", "Dark Enchantress pet", "Millennial Tree pet",
    "Pitaya Dragon pet(Epic)", 'Pitaya Dragon pet(Legen)', "Ananas Dragon pet(Epic)",'Ananas Dragon pet(Legen)', "Timekeeper pet", "Lotus Dragon pet(Legen)",'Lotus Dragon pet(Epic)',
    "Lychee Dragon pet(Legen)", 'Lychee Dragon pet(Epic)', "Longan Dragon pet", "Abyss Monarch pet", "Sugar Swan pet",
    "Xylitol Nova pet", "Black Sugar Swan pet", "Dreamweaver pet", "Stevia Nova pet",
    "GingerBrave pet", "GingerBright pet", "Strawberry pet", "Skater pet", "Zombie pet",
    "Angel pet", "Muscle pet", "Pilot pet", "Ninja pet", "Soda pet", "Rockstar pet",
    "Devil pet", "Cherry pet", "Alchemist pet", "Gumball pet", "Pistachio pet",
    "Vampire pet", "Cheesecake pet(Coin)", 'Cheesecake pet(Score)', "Knight pet", "Princess pet", "Cheerleader pet",
    "Heartsping pet", "Twinkleping pet", "Hello Kitty pet", "Mimmy pet", "Cookiedroid pet",
    "Coffee pet", "Buttercream Choco pet", "Special Force pet", "Space Doughnut pet",
    "Hero pet", "Skating Queen pet", "Yoga pet", "Kumiho pet", "Pirate pet", "Popcorn pet",
    "Werewolf pet", "Snow Sugar pet", "Wizard pet", "Tiger Lily pet", "Dark Choco pet",
    "Mint Choco pet(Coin)", "Mint Choco pet(Score)", "Fairy pet", "Cocoa pet", "Pancake pet", "Kiwi pet", "Herb pet",
    "Cream Puff pet", "Peppermint pet", "Dr. Wasabi pet", "Mustard pet", "Orange pet",
    "Moon Rabbit pet", "Matcha pet", "Macaron pet", "Carol pet", "Sparkling pet",
    "Red Bean pet", "Ice Candy pet", "Pink Choco pet", "Avocado pet", "Cherry Blossom pet",
    "Whipped Cream pet", "White Choco pet", "Adventurer pet", "Blackberry pet",
    "Chili Pepper pet", "Red Pepper pet", "Grapefruit pet", "Lemon pet", "Salt pet",
    "Lime pet", "Squid Ink pet", "Pomegranate pet", "DJ pet", "Roll Cake pet",
    "Marshmallow pet", "Cinnamon pet", "Fig pet", "Cotton Candy pet", "Carrot pet",
    "Beet pet", "Purple Yam pet", "Milk pet", "Ion Robot pet", "Cyborg pet", "Dino-Sour pet",
    "Plum pet", "Peach pet", "Yogurt Cream pet", "Walnut pet", "Roguefort pet",
    "Mala Sauce pet", "Birthday Cake pet", "Firecracker pet", "Chestnut pet", "Pudding pet",
    "Prophet pet", "Blueberry Pie pet", "Raspberry Mousse pet", "Rose pet", "Spinach pet",
    "Sandwich pet", "Mango pet", "Apple pet", "Cream Unicorn pet", "General Jujube pet",
    "Leek pet", "Captain Ice pet", "Sorbet Shark pet", "Lobster pet", "Mocha Ray pet",
    "Truffle pet", "Onion pet", "Melon Bun pet", "Goblin pet", "Croissant pet",
    "Popping Candy pet", "Shining Glitter pet", "Chess Choco pet", "Earl Grey pet",
    "Cookiemals pet", "Churro pet", "Ice Juggler pet", "Banana pet", "Starfruit pet",
    "Licorice pet", "Bell Pepper pet", "Aloe pet", "Butter Pretzel pet", "Almond pet",
    "Lilac pet", "Scorpion pet", "Bellflower pet", "Ginseng pet", "Hydrangea pet",
    "Sour Belt pet", "Chocolate Bonbon pet", "Amber Sugar pet", "Sugar Glass pet",
    "Eggnog pet", "Tiramisu pet", "String Gummy pet", "Candlelight pet", "Crowberry pet",
    "Dr. Bones pet", "Pizza pet", "Rambutan pet", "Cherry Ball pet", "Choco Ball pet",
    "Peperoncino pet", "Cauliflower pet", "Snake Fruit pet", "Black Garlic pet",
    "White Ghost pet", "Vagabond pet", "Rebel pet", "Lilybell pet", "Poison Mushroom pet",
    "Blue Lily pet", 'Guardian pet(Magma)', 'Guardian pet(Blue dragon)', 'Guardian pet(Snow)', 'Guardian pet(Golem)'
]

treasure_list_en = [
    "Shield Bubble Gun", "Jelly Topped Cupcake", "Bear Jelly Ice Cream", "Lollipop Skate",
    "Coin Silver Crown", "Mini Magnet Robot", "Almond Chocolate Chip Hammer", "Candy Dynamite",
    "Jelly Seed Crystal Jar", "Red Egg of Resurrection", "Candy Cane Staff of Darkness",
    "Silver Flower Brooch", "Winged Jelly of Resurrection", "Perfect Landing Book",
    "Divine Aurora Extract Flask", "Coin Fireworks Box", "Rainbow Bear Roll Cake",
    "Fiery Candy Comet", "Ticking Treasure Chest", "Bubble Gum Spring Jumpers",
    "Bear Jelly Boomerang", "Carrot Pudding Trampoline", "Bearstone Ring",
    "Frozen Piece of Cake", "Divine Guardian Shield", "Cursed Goblet",
    "X-tra Hot Turbo Engine", "Stuffed Jumping Jelly Horsey", "Dreaming Bear Medal",
    "Bubble Wave Shell", "Golden Cheese Pickaxe", "Power Energy Drink", "Star Candy Globe",
    "Lucky Clover Earrings", "Luxury Red Carpet", "Perfect Treasure Map", "Mirror of Malice",
    "Miraculous Nutrient Ampoule", "Rainbow Headphones", "Thunderdrum",
    "Colorful Paper Plane", "Magic Card Deck", "Forbidden Manuscript", "Figgy Punch",
    "Peaceful Dove Bun", "Carrot Missile", "Giant Superbean", "Flaming Sweet Potato",
    "Milk Snack", "Ion Microchip", "Gigawatt Cube", "Tinysaur Hatchling",
    "Ring of Eternal Flame", "Scroll of Guidance", "Ageless Peach Pit",
    "Fabled Magic Carpet", "Nutcracker Mallet", "Magma Pendulum", "Jelly Cream Whisk",
    "E-Z Camera", "Plasma Crystal Ball", "Saber of Virtue", "Green Pea Slingshot",
    "1000% Juice", "Apple Candy Balloon", "Horse Figurine", "Double Scoop Frozen Bear",
    "Iridescent Pearl", "Haunted Snuggly Bear", "Melon Dynamite", "Timeweaver Scissors",
    "Pop Pop Photocard", "Enchanted Broom", "Darkwind Quiver", "Candy Clown Shoe",
    "Starlight Nightlight", "New PepBook", "Rainbow Paint Tube", "Enchanted Mirror",
    "Panacea Pestle", "Flowering Can", "Fashionista Spotlight", "Paradise Compass",
    "Jingle Jingle Wreath", "Time Rend Scissors", "Good-Job Bear Stamp",
    "Bone-afide Multivitamin Jelly", "Rambirdtan Handler Glove", "Cheery Pom Poms",
    "Drakeling Claw", "Ghost-Repellent Sticker", "Tricolor Chewy Rice Cake",
    "Butterfly Brooch", "Starry Aeroplane", "Automatic Typewriter", "Igneous Obsidian",
    "Fluffy Yarn Ball", "Seahorse Watergun", "Bountiful Scarecrow", "Bubbly Submarine",
    "Giant Lawbook", "Moonlight Lantern", "Aurora Sugar Feather", "Goldberry Bell",
    "Jelly Pop Bottle Rocket", "Bear Jelly Tanghulu", "Munch-Munch Popcorn",
    "Sniffly Cocoa Palm", "Crimson Dragon Mask", "Sweet Jams Guitar", "Supreme Sunblade",
    "Lakeside Sugar Rose", "Jolly Jack O'Lantern", "Dreamland Travel Pillow",
    "The Starmaker", "Chapssal Bundle", "Flower of Hope", "Glass Candy Planetarium",
    "Budding Future", "Precise Rambutan Bow", "Essence of Conflagration",
    "Essence of Rejuvenation", "Lamp of Endless Dreams", "Eternal Wish Meteor",
    "Hourglass of Aeternus Tempora", "Unidentified Flying Donut", "Trident legend treasure",
    "Mama's Apple Pie", "Kitty's Lovely Lunchbox", "Kitty's Candy Box", "Firm Friendship Ring", "True Friendship Pendant"
]

데이터파일 = "userdata.json"

def load_data():
    if not os.path.exists(데이터파일):
        with open(데이터파일, 'w') as f:
            json.dump({"users": {}, "대결": {}}, f)
    with open(데이터파일, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(데이터파일, 'w') as f:
        json.dump(data, f, indent=2)

#!대표쿠키설정 @멘션 [쿠키, 펫]
@bot.command()
async def 대표쿠키6496(ctx, *, 이름):
    data = load_data()
    user_id = str(ctx.author.id)
    if user_id not in data['users']:
        data['users'][user_id] = {"대표쿠키": 이름, "전적": {"승": 0, "패": 0}}
    else:
        data['users'][user_id]['대표쿠키'] = 이름
    save_data(data)
    await ctx.send(f"{ctx.author.mention}의 대표 쿠키가 `{이름}`으로 설정되었습니다!")

@bot.command()
async def 김노트(ctx):
    await ctx.send("아잌ㅋㅋㅋㅋㅋㅋ 러븤ㅋㅋㅋㅋㅋㅋㅋㅋ 복시젠ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

@bot.command()
async def sickduck(ctx):
    await ctx.send("Marry me please Go4 ㅠㅠ")
    
@bot.command()
async def 식덕(ctx):
    await ctx.send("안녕 나는 골드스타게이 식덕이라고 해.\n주로 바텀 포지션에서 하는걸 좋아해.")

@bot.command()
async def bottom(ctx):
    await ctx.send("is sickduck")

@bot.command()
async def 대표쿠키설정(ctx, 상대: discord.Member, *, 이름):
    data = load_data()
    user_id = str(상대.id)
    if user_id not in data['users']:
        data['users'][user_id] = {"대표쿠키": 이름, "전적": {"승": 0, "패": 0}}
    else:
        data['users'][user_id]['대표쿠키'] = 이름
    save_data(data)
    await ctx.send(f"{상대.mention}의 대표 쿠키가 `{이름}`으로 설정되었습니다! (관리자 설정)")

def get_special_rule():
    market = ["롤리팝 스케이트", "부활의 붉은 알", "핫핫 스파이시 터보엔진", "부활의 날개 젤리", "완벽한 보물지도"]
    market2 = ["1회 리롤권", f"{random.sample(유저리스트, 1)}의 대표쿠키와 펫", "브레인껌", "쌍둥이덤벨", "치즈크럼블 고양이", "프로듀서 마이크", "머스터드맛 쿠키", "키위맛 쿠키", "오렌지맛 쿠키"]
    market3 = ["마그마 불새", "눈폭풍 예티", "푸른 회오리용", "에메랄드 수호골렘"]
    rules = [
        "🍀 **우리 친구할래?**\n두 플레이어가 `체스초코 쿠키`를 횟수 제한없이 사용할 수 있습니다.\nBoth players will be able to use `Chess Choco` without restrictions.",
        "🏍 **이 차는 이제 제껍니다.**\n`#속도` 태그를 가진 쿠키가 등장한다면 `고블린맛 쿠키 또는 괴도맛 쿠키`로 대체하여 사용합니다.(대표 쿠키는 여전히 사용 가능합니다.)\nIf `#Speed Tag Cookie` appears, it should be replaced with `Goblin Cookie or Roguefort Cookie`.(Symbol cookies are still available.)",
        "🐒 **남의 떡이 커보인다.**\n플레이어가 대표 쿠키를 서로 바꿔서 사용합니다.\nBoth players swap Symbol Cookie's.",
        f"🎲 **주사위 결정전**: 1:1 상황이라면 주사위를 굴려 높은 쪽이 `{random.randint(20, 100)}M점`를 가져갑니다.(!dice)\nIn a 1:1 situation, the dice are rolled and the higher roll gets an `Extra score`(!dice).",
        f"🗳 **우리의 공공재**\n모든 참가자는 `{random.sample(유저리스트, 1)}`의 대표쿠키를 사용할 수 있습니다.",
"🌀 **뒤바뀐 운명**\n서로가 뽑은 세팅은 상대의 것이 됩니다.\nEach other's setup becomes the other's.", "⁉️ **바꿔 다 바꿔!**\n대결 중 딱 1번씩 모두의 세팅을 리롤할 기회를 가집니다.\nHave the right to reroll both player's setup only once per match.", "♻️ **쓰레기도 안고가는**\n세트 마다 상대의 세팅 중 꼭 사용해야할 쿠키(or 펫) 하나를 지정합니다.\nFor each set, choose a cookie (or pet) that must be used in your opponent's setup.", "🧭 **이 길이 아닌가?**\n맵 순서가 역순으로 진행됩니다.\nMap order will be reversed.",f"🥷 **그런데 그 때 닌자가 나타났다.**\n`닌자맛 쿠키`를 선달로 사용시 `{random.randint(100,300)}M`점을 추가로 얻습니다. 모두의 대표쿠키가 닌자맛 쿠키로 변경됩니다.\nWhen use `Ninja Cookie` as your primary cookie, you will receive an additional extra points. Everyone's symbol cookie will change into a Ninja Cookie.", f"🪽 **더 가볍게**\n미장착한 보물 하나당 `{random.randint(60,100)}M점`을 추가로 얻습니다.\nYou will receive an additional score for each unequipped treasure.", f"🐿 **돌아온 다람쥐 상점**\n각 플레이어는 다음 아이템을 항목별로 1개씩 구입할 수 있습니다.\n\n`{random.sample(market,1)}`을 `{random.randint(100,500)}만점`에 구입할 수 있다.\n`{random.sample(market2,1)}`을 `{random.randint(500,1200)}만점`에 구입할 수 있다.\n`{random.sample(market3,1)}`을 `{random.randint(1300,2100)}만점`에 구입할 수 있다.", "👀 **가운데는 무시ㅠㅠ**\n두번째 맵 대신 첫번째 맵을 2번 플레이합니다.\nPlay the first map twice instead of the second map.","🎫 **아직 안끝났어!**\n2:0으로 게임이 끝났을 경우 패자의 의사로 2점을 걸고 3번째 게임을 시작할 수 있습니다. 4:0이 된다면 결과 정산을 2번합니다.\nIf the game ends 2:0, the loser can challenge a third game with a 2-point stake. If 4:0, the result is settled twice.", "🏆 **주니어컵**\n1성맵에서 경기합니다.\nPlay on 1-star maps.", "👴 **고령화 시대**\n체력 관련 능력이 없는 모든 펫이 `공주의 장신구`로 대체됩니다.(대표 펫은 여전히 사용 가능합니다.)\nAll pets without stamina related abilities will be changed to `Princess pet`. (Symbol pets are still available.)", f"🏅 **원맨쇼**\n이어달리기를 하지 않는다면 총점의 `{random.randint(35,60)}%`를 추가합니다.\nIf you do not relay, you will receive an additional persentage of total score.", "⚔️ **상남자식 단판**\n`지축을 뒤흔드는 용의 포효`에서 단판에 결과를 짓습니다.\n`Third map` produces results in one play.", "☄️ **너도 멸종되지 않게 조심해**\n모든 `드래곤 쿠키`가 `물망초 다이노 쿠키`로 대체됩니다. `보물 유성우, 별똥별`을 제한없이 사용할 수 있습니다.\nAll `Dragon Cookie` will be replaced with `Pond Dino Cookie`. You can use Treasure `Eternal Wish Meteor` and `Fiery Candy Comet` without restrictions.", "🦅**고산병**\n`#비행` 태그를 가진 쿠키가 등장한다면 `에일리언 도넛` 또는 `쿠키멀즈`로 대체하여 사용합니다. (대표 쿠키는 여전히 사용 가능합니다.)\nIf `#Flight Tag Cookie` appears, it should be replaced with `Alien Doughnut or Cookiemals`. (Symbol cookies are still available.)"
    ]
    return random.choice(rules)

#!전적 @멘션
@bot.command()
async def 전적(ctx, 대상: Optional[discord.Member] = None):
    대상 = 대상 or ctx.author
    user_id = str(대상.id)
    data = load_data()

    if user_id not in data['users']:
        await ctx.send(f"📊 {대상.display_name}의 전적 정보가 없습니다.")
        return

    user_data = data['users'][user_id]
    승 = user_data['전적'].get('승', 0)
    패 = user_data['전적'].get('패', 0)
    레이팅 = user_data.get('레이팅', 100)

    await ctx.send(
        f"📈 {대상.mention}의 전적:\n"
        f"✅ 승: `{승}`회\n"
        f"❌ 패: `{패}`회\n"
        f"🏅 레이팅: `{레이팅}`점"
    )


#!전적초기화 @멘션
@bot.command()
@commands.has_permissions(administrator=True)
async def 전적초기화(ctx, 대상: discord.Member):
    data = load_data()
    user_id = str(대상.id)

    if user_id in data['users']:
        data['users'][user_id]['전적'] = {"승": 0, "패": 0}
        await ctx.send(f"🧹 {대상.display_name}님의 전적이 초기화되었습니다.")
    else:
        await ctx.send("❌ 해당 유저의 전적 정보가 없습니다.")

    save_data(data)

@전적초기화.error
async def 전적초기화_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🔒 관리자만 이 명령어를 사용할 수 있습니다.")

@bot.command()
async def 대결(ctx, 상대: discord.Member):
    try:
        await asyncio.wait_for(대결_처리(ctx, 상대), timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.send("⏰ 대결 시작이 너무 오래 걸려 실패했어요.")

async def 대결_처리(ctx, 상대):
    user1 = str(ctx.author.id)
    user2 = str(상대.id)
    data = load_data()

    data['대결'][user1] = {"상대": user2}
    data['대결'][user2] = {"상대": user1}

    # 대결 시작 시 매칭대기 목록에서 제거
    if "매칭대기" in data:
        data["매칭대기"] = [uid for uid in data["매칭대기"] if uid not in [user1, user2]]

    # 30% 확률로 특수 규칙 적용
    special_rule = None
    if random.random() < 0.99:
        special_rule = get_special_rule()
        data['대결'][user1]["특수규칙"] = special_rule
        data['대결'][user2]["특수규칙"] = special_rule

    save_data(data)

    user1_cookie = data['users'].get(user1, {}).get("대표쿠키", "(미설정)")
    user2_cookie = data['users'].get(user2, {}).get("대표쿠키", "(미설정)")

    msg = (
        f"🎯 {ctx.author.mention} vs {상대.mention} 대결이 시작되었습니다!\n"
        f"- {ctx.author.display_name}의 대표 쿠키: `{user1_cookie}`\n"
        f"- {상대.display_name}의 대표 쿠키: `{user2_cookie}`\n"
        f"각자 `!세팅`, `!setup` 명령어를 입력하여 조합을 받으세요."
    )

    if special_rule:
        msg += f"\n\n**특수 규칙 발동!**: {special_rule}"

    await ctx.send(msg)
    

    
@bot.command()
async def 세팅(ctx):
    try:
        await asyncio.wait_for(세팅_처리(ctx), timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.send("⏰ 세팅이 너무 오래 걸려 실패했어요.")

async def 세팅_처리(ctx):
    user = str(ctx.author.id)
    data = load_data()
    if user not in data['대결']:
        await ctx.send("대결 상대가 없습니다. 먼저 `!대결 @상대` 를 입력하세요.")
        return

    쿠키 = random.sample(쿠키리스트, 4)
    펫 = random.sample(펫리스트, 2)
    보물 = random.sample(보물리스트, 6)
    data['대결'][user].update({"쿠키": 쿠키, "펫": 펫, "보물": 보물})
    save_data(data)
    await ctx.send(
        f"🍪 {ctx.author.mention}의 조합:\n"
        f"쿠키: {', '.join(쿠키)}\n"
        f"펫: {', '.join(펫)}\n"
        f"보물: {', '.join(보물)}"
    )

@bot.command()
async def dice(ctx):
    결과 = random.randint(1, 6)
    await ctx.send(f"🎲 {ctx.author.mention}의 주사위 결과는 `{결과}`입니다!")

@bot.command()
async def setup(ctx):
    try:
        await asyncio.wait_for(handle_setup(ctx), timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.send("⏰ Setup took too long and failed.")

async def handle_setup(ctx):
    user = str(ctx.author.id)
    data = load_data()
    if user not in data['대결']:
        await ctx.send("You are not in a battle. Use `!battle @opponent` first.")
        return

    cookies = random.sample(cookie_list_en, 4)
    pets = random.sample(pet_list_en, 2)
    treasures = random.sample(treasure_list_en, 6)
    data['대결'][user].update({"cookies": cookies, "pets": pets, "treasures": treasures})
    save_data(data)
    await ctx.send(
        f"🍪 {ctx.author.mention}'s setup:\n"
        f"Cookies: {', '.join(cookies)}\n"
        f"Pets: {', '.join(pets)}\n"
        f"Treasures: {', '.join(treasures)}"
    )

@bot.command()
async def 결과(ctx, 상대: Optional[discord.Member], 점수: str):
    if 상대 is None:
        await ctx.send("❗ 상대를 멘션(@)해주세요. 예: `!결과 @사용자 123456:123123`")
        return

    try:
        score1, score2 = map(int, 점수.split(":"))
    except:
        await ctx.send("❗ 점수 형식이 잘못됐습니다. 예: `!결과 @상대 123456:123123`")
        return

    user1 = str(ctx.author.id)
    user2 = str(상대.id)
    data = load_data()

    # 초기화
    for uid in [user1, user2]:
        if uid not in data['users']:
            data['users'][uid] = {
                "대표쿠키": "없음",
                "전적": {"승": 0, "패": 0},
                "레이팅": 1000
            }
        if "레이팅" not in data['users'][uid]:
            data['users'][uid]["레이팅"] = 1000

    if score1 == score2:
        await ctx.send("⚖️ 무승부는 기록되지 않습니다.")
        return

    winner, loser = (user1, user2) if score1 > score2 else (user2, user1)
    winner_obj = ctx.author if winner == user1 else 상대

    # 전적 갱신
    data['users'][winner]['전적']['승'] += 1
    data['users'][loser]['전적']['패'] += 1

    # 레이팅 계산
    r_win = data['users'][winner]['레이팅']
    r_lose = data['users'][loser]['레이팅']
    gain = 60 + (r_lose - r_win) // 10
    gain = max(40, min(gain, 80))

    data['users'][winner]['레이팅'] += gain
    data['users'][loser]['레이팅'] -= gain

    # 대결 종료
    data['대결'].pop(user1, None)
    data['대결'].pop(user2, None)

    save_data(data)

    await ctx.send(
        f"🎉 `{score1}:{score2}` 결과로 {winner_obj.mention}이 승리하였습니다!\n"
        f"📈 `{winner_obj.display_name}`의 레이팅 +{gain} → {data['users'][winner]['레이팅']}점\n"
        f"📉 `{상대.display_name if winner_obj == ctx.author else ctx.author.display_name}`의 레이팅 -{gain} → {data['users'][loser]['레이팅']}점"
    )

@bot.command()
async def 대결취소(ctx, 상대: discord.Member):
    user1 = str(ctx.author.id)
    user2 = str(상대.id)
    data = load_data()

    # 둘 다 대결 목록에 있어야 하고 서로 맞상대인지 확인
    if user1 not in data['대결'] or data['대결'][user1].get("상대") != user2:
        await ctx.send("현재 {상대.display_name}님과 대결 중이 아니에요.")
        return

    # 상대방도 같은 대결 정보여야 확실하게 삭제
    if user2 in data['대결'] and data['대결'][user2].get("상대") == user1:
        del data['대결'][user2]

    del data['대결'][user1]
    save_data(data)

    await ctx.send(f"{ctx.author.mention}와 {상대.mention}의 대결이 강제로 종료되었습니다.")

@bot.command()
@commands.has_permissions(administrator=True)
async def 레이팅설정(ctx, 대상: Optional[discord.Member], 점수: Optional[int]):
    if 대상 is None or 점수 is None:
        await ctx.send("❗ 사용법: `!레이팅설정 @유저 123`")
        return

    user_id = str(대상.id)
    data = load_data()

    if user_id not in data['users']:
        data['users'][user_id] = {
            "대표쿠키": "없음",
            "전적": {"승": 0, "패": 0},
            "레이팅": 1000
        }

    data['users'][user_id]['레이팅'] = 점수
    save_data(data)

    await ctx.send(f"🔧 {대상.display_name}의 레이팅이 `{점수}`점으로 설정되었습니다.")

@bot.command()
async def 랭킹(ctx):
    data = load_data()
    유저들 = data.get('users', {})

    if not 유저들:
        await ctx.send("📉 등록된 유저가 없습니다.")
        return

    # 정렬
    랭킹리스트 = sorted(
        유저들.items(),
        key=lambda item: item[1].get("레이팅", 1000),
        reverse=True
    )

    # 상위 10명 표시
    랭킹출력 = []
    for 순위, (uid, 정보) in enumerate(랭킹리스트[:15], start=1):
        유저 = await bot.fetch_user(int(uid))
        닉네임 = 유저.display_name if 유저 else f"User {uid}"
        점수 = 정보.get("레이팅", 1000)
        랭킹출력.append(f"{순위}위 🏅 `{닉네임}` - {점수}점")

    await ctx.send("🏆 **레이팅 랭킹** 🏆\n" + "\n".join(랭킹출력))

@bot.command()
async def 대표쿠키목록(ctx):
    data = load_data()
    users = data.get("users", {})
    if not users:
        await ctx.send("등록된 유저가 없습니다.")
        return

    lines = []
    for user_id, info in users.items():
        대표쿠키 = info.get("대표쿠키", None)
        레이팅 = info.get("레이팅", 1000)
        try:
            user_obj = await bot.fetch_user(int(user_id))
            if 대표쿠키:
                lines.append((레이팅, f"`{user_obj.display_name}` \n대표쿠키: {대표쿠키}\n"))
        except:
            continue  # 혹시 유저 정보를 못 가져오면 무시

    if not lines:
        await ctx.send("대표 쿠키를 설정한 유저가 없습니다.")
        return

    # 레이팅 기준 내림차순 정렬
    lines.sort(reverse=True)

    # 상위 20명까지만 출력
    결과 = "\n".join([f"{i+1}. {line[1]}" for i, line in enumerate(lines[:20])])
    await ctx.send(f"📋 **대표 쿠키 목록 (Top 20)**\n{결과}")

@bot.command()
async def 매칭대기(ctx):
    user_id = str(ctx.author.id)
    data = load_data()
    
    if "매칭대기" not in data:
        data["매칭대기"] = []

    if user_id not in data["매칭대기"]:
        data["매칭대기"].append(user_id)
        save_data(data)
        await ctx.send(f"{ctx.author.mention} 님이 매칭 대기 목록에 추가되었습니다.")
    else:
        await ctx.send(f"{ctx.author.mention} 님은 이미 매칭 대기 중입니다.")

    # 다른 유저 목록 출력
    others = [uid for uid in data["매칭대기"] if uid != user_id]
    if not others:
        await ctx.send("현재 다른 매칭 대기자는 없습니다.")
    else:
        names = []
        for uid in others:
            try:
                user = await bot.fetch_user(int(uid))
                names.append(user.name)
            except:
                continue
        await ctx.send(f"현재 매칭 대기 중인 유저들: {', '.join(names)}")

@bot.command()
async def 대기취소(ctx):
    user_id = str(ctx.author.id)
    data = load_data()

    if "매칭대기" in data and user_id in data["매칭대기"]:
        data["매칭대기"].remove(user_id)
        save_data(data)
        await ctx.send(f"{ctx.author.mention} 님이 매칭 대기 목록에서 제거되었습니다.")
    else:
        await ctx.send(f"{ctx.author.mention} 님은 현재 매칭 대기 중이 아닙니다.")




    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("알 수 없는 명령어예요.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("명령어에 필요한 요소가 빠졌어요.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("명령어 작성 형식이 잘못됐어요. 예: `!결과 @상대 123456:123123`")
    else:
        await ctx.send("알 수 없는 오류가 발생했어요.")
        raise error

keep_alive()
import os

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)