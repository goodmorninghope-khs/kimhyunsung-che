# 김현성체

정책셰프 김현성(태하)의 문체를 담은 Claude 스킬 모음이다. 2010년부터 2026년까지 쓴 기고 31편, 페이스북 글 2,800여 편, 연설·대필·보고 메모, 『물음』 원고를 원문 창고 '글주방'에 모으고, AI와 함께 쓰기 이전의 글을 기준으로 문장 버릇을 셈해 만들었다.

## 스킬

| 폴더 | 층 | 맡는 일 |
|---|---|---|
| `skills/writing-form-map` | 접수 | 요청을 받으면 글의 종류와 형식을 고르고 알맞은 스킬로 연결 |
| `skills/portal-news-brief` | 접수 | 포털 브리핑에서 글감을 뽑아 김현성체 글쓰기까지 도는 루프 |
| `skills/golmok-diagnosis` | 형식 | 현실을 규정하고 다음을 예측하고 대안을 내는 칼럼·기고의 형식 |
| `skills/golmok-narrative` | 형식 | 인물과 장면으로 끌고 가는 서사형 글의 형식 |
| `skills/drama-writer` | 형식 | 극본·기획안, 그리고 강연·칼럼에 빌려 쓰는 로그라인과 매력 공식 |
| `skills/golmok-writer` | 문체 | 김현성체 본체. 매체별 목소리, 사다리(2-1), 두 번 쓰기(2-2), AI 티 점검표, 발행물별 적용표(16장) |
| `skills/golmok-factcheck` | 검수 | 내기 전 숫자·날짜·직함·인용을 출처와 대조한 판정표 |
| `skills/golmok-rebuttal-reader` | 검수 | 내기 전 가장 센 반박과 처음 읽는 독자의 막힘을 미리 받기 |
| `skills/golmok-revision-learning` | 학습 | 저자가 고쳐 올린 최종본을 초안과 견줘 김현성체 규칙 후보를 뽑기 |

문장과 목소리는 언제나 golmok-writer가 정한다. 형식 스킬은 뼈대를, 검수 스킬은 권고를 맡고 글을 직접 고치지 않는다.

## 글쓰기 루프

접수 → 형식 → 문체(한 줄 설계 → 문 닫고 초고 → 문 열고 2고) → 검수(팩트체크 → 반론 독자) → 발행 → 학습(퇴고 학습 → 김현성체 개정)

가벼운 SNS 글은 접수에서 golmok-writer 4-1장으로 바로 가고 검수를 거치지 않는다.

## 장부

- `revision-log.md`: 저자가 초안을 고친 방향 가운데 아직 규칙이 되지 못한 관찰. 같은 방향이 두 번 쌓이면 규칙으로 올린다.
- `prediction-log.md`: 낸 글에 담긴 예측과 선행지표, 검증 시점. '예측 복기' 글의 재료다.

## 쓰는 법

- Claude: 각 폴더를 스킬로 올린다. "김현성체로 기고문 써 줘", "페북 글 써 줘"처럼 부르면 된다.
- 스킬이 없는 환경: `git clone --depth 1 https://github.com/goodmorninghope-khs/kimhyunsung-che`로 받아 `skills/golmok-writer/SKILL.md`를 먼저 읽힌다.

## 발행물

김현성체가 쓰이는 지면은 신문 기고, 페이스북·스레드, 뉴스레터 '뜻땀때 소포', JUNGNANG SIGNAL, 브런치 연재 '구청에 AI가 출근했다', 기관장 명의 메시지, 보고 메모, 단행본 원고다. 지면마다 얼마나 얹을지는 golmok-writer 16장의 표를 따른다.

## 도구와 시험

- `tools/kimhyunsung_lint.py`: golmok-writer 12장 AI 티 점검표에서 셀 수 있는 항목을 세는 점검기. `python3 tools/kimhyunsung_lint.py 원고.txt --medium column` (페북은 `sns`, 가벼운 글은 `sns-light`).
- `tests/blind-test.md`: 점검기, 블라인드 시험, 동선 시험의 절차와 기록.
- `references/craft-shelf.md`: 작법 서가. 스티븐 킹·이기원처럼 이미 들인 작법과, 오웰·진서·맥피·강원국·유시민·이태준·이오덕처럼 견줘만 본 작법. 새 작법은 여기를 거쳐 스킬로 올린다.

## 원본과 사본

규칙의 원본은 Claude 계정 스킬이고, 이 저장소는 같은 내용을 담는 사본이다. 스킬을 고치면 그 스킬의 '버전' 줄을 올리고 같은 파일을 여기에 커밋한다. 점검할 때는 계정 판과 이 사본을 diff로 먼저 견준다. 2026년 11월 점검에서 계정 판이 사본보다 옛 판이어서 규칙이 서로 부딪친 적이 있다. 커밋 메시지는 `sync: vYYYY.MM.DD-N — 바뀐 내용 한 줄`로 쓴다.

원문 창고 '글주방'의 원문 자체는 이 저장소에 넣지 않는다.

## 연계 (밸류체인)

이 저장소는 [policy-media-desk](https://github.com/goodmorninghope-khs/policy-media-desk) 밸류체인의 **② 제작 (문체)** 고리다. 상태: 제안 (발행인 확인 후 실제로 이으면 '연계'로 바꾼다).

- 받음: 정책 미디어의 '평가로 느껴지지 않는 문체' 기준과 바꿔 쓰기 예
- 넘김: 발행인 목소리 기준 → 창간사·특집 지면
- 넘길 때는 출처 지면(지면명·호수·날짜·링크)과 '닿는 공약'을 붙이고, 침은 의견으로 남긴다. 결정은 받는 고리의 책임자가 한다.

전체 사슬: [references/value-chain.md](https://github.com/goodmorninghope-khs/policy-media-desk/blob/main/references/value-chain.md)
