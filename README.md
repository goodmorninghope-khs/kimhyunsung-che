# 김현성체

정책셰프 김현성(태하)의 문체를 담은 Claude 스킬 모음이다. 2010년부터 2026년까지 쓴 기고 31편, 페이스북 글 2,800여 편, 연설·대필·보고 메모, 『물음』 원고를 원문 창고 '글주방'에 모으고, AI와 함께 쓰기 이전의 글을 기준으로 문장 버릇을 셈해 만들었다.

## 스킬

| 폴더 | 맡는 일 |
|---|---|
| `skills/golmok-writer` | 김현성체 본체. 매체별 목소리, 공통 바탕, AI 티 점검표, 발행물별 적용표(16장) |
| `skills/golmok-diagnosis` | 현실을 규정하고 다음을 예측하는 칼럼·기고의 형식 |
| `skills/golmok-narrative` | 인물과 장면으로 끌고 가는 서사형 글의 형식 |
| `skills/writing-form-map` | 요청을 받으면 글의 종류와 형식을 고르고 알맞은 스킬로 연결 |

문장과 목소리는 언제나 golmok-writer가 정하고, 나머지 셋은 형식을 맡는다.

## 쓰는 법

- Claude: 각 폴더를 스킬로 올린다. "김현성체로 기고문 써 줘", "페북 글 써 줘"처럼 부르면 된다.
- 스킬이 없는 환경: `git clone --depth 1 https://github.com/goodmorninghope-khs/kimhyunsung-che`로 받아 `skills/golmok-writer/SKILL.md`를 먼저 읽힌다.

## 발행물

김현성체가 쓰이는 지면은 신문 기고, 페이스북, 뉴스레터 '뜻땀때 소포', JUNGNANG SIGNAL, 브런치 연재 '구청에 AI가 출근했다', 기관장 명의 메시지, 보고 메모, 단행본 원고다. 지면마다 얼마나 얹을지는 golmok-writer 16장의 표를 따른다.

## 원본과 사본

규칙의 원본은 Claude 계정 스킬이고, 이 저장소는 같은 내용을 담는 사본이다. 스킬을 고치면 `skills/golmok-writer/SKILL.md` 끝의 '버전' 줄을 올리고 같은 파일을 여기에 커밋한다. 커밋 메시지는 `sync: vYYYY.MM.DD-N — 바뀐 내용 한 줄`로 쓴다.

원문 창고 '글주방'의 원문 자체는 이 저장소에 넣지 않는다.
