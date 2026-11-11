#!/usr/bin/env python3
"""김현성체 AI 티 점검기.

golmok-writer 12장 점검표 가운데 셀 수 있는 항목을 센다.
쓰는 법:  python3 tools/kimhyunsung_lint.py 원고.txt [--medium column|sns|sns-light]
         cat 원고.txt | python3 tools/kimhyunsung_lint.py -
문장 길이는 공백을 빼고 센다(2026-11-12 글주방 AI 이전 기고 3편으로 보정: 공백 제외 평균 40.6자, 60자 넘는 문장 11%). 스크립트가 못 보는 것(메타 문장, 어체의 이어짐,
지어낸 대사, 사실 오류)은 사람이 본다. 통과는 '저자처럼 읽힌다'의 필요조건일 뿐이다.
"""
import argparse, re, sys

REPERTOIRE = ["마차", "라면", "언발에 오줌", "언 발에 오줌", "그림의 떡", "기침", "물고기 잡는",
    "씨앗 속 사과", "우분투", "심판과 선수", "잊지 않아야", "봄을 이기는", "눈가리고 아웅",
    "눈 가리고 아웅", "호떡집", "혹세무민", "슘페터", "아인슈타인", "리나 칸", "그람시",
    "스티글리츠", "김구", "김대중", "다윗", "소 무 12조", "지산D소", "1소1상"]
BUFFERS = ["듯하다", "듯 하다", "듯", "생각이다", "아울러", "아닐까 싶다", "이야말로", "란다"]
ADVERBS = ["매우", "정말", "너무", "굉장히"]
META_WORDS = ["구조", "설계", "작동", "역설"]
BANNED = ["라 부른다", "라고 부른다", "같은 시각", "누군가는 말한다", "질문이 바뀌었다"]
SNS_AVOID = ["할 수 있습니다", "함께 만들어가요", "중요합니다", "더 나은", "에 있어서"]
PASSIVE = [r"되어[지진졌]", r"지어[지진졌]", r"에 의해", r"에 의하여"]

def sentences(text):
    body = re.sub(r"^#.*$", "", text, flags=re.M)
    parts = re.split(r"(?<=[.?!])[\"'’”)]*\s+|\n{2,}", body)
    return [p.strip() for p in parts if p and len(p.strip()) > 1]

def check(text, medium):
    S = sentences(text)
    n = max(len(S), 1)
    lens = [len(re.sub(r"\s", "", s)) for s in S]
    L = dict(zip(map(id, S), lens))
    chars = len(re.sub(r"\s", "", text))
    scale = max(chars / 2000, 0.5)
    rows = []
    def row(name, val, ok, limit, note=""):
        rows.append((name, val, limit, "통과" if ok else "고칠 것", note))
    def find(pat):
        return [s for s in S if re.search(pat, s)]

    d = len(re.findall(r"[—–―]", text))
    row("대시", d, d == 0, "0")
    pq = find(r"(는가|인가|은가|던가|까)\.$")
    row("마침표로 끝난 물음", len(pq), not pq, "0", " / ".join(x[-18:] for x in pq[:3]))
    rev = sum(1 for a, b in zip(S, S[1:]) if re.search(r"(아니다|않는다)\.$", a) and L[id(b)] <= 18 and b.endswith("다."))
    row("짧은 반전 대구(A가 아니다. B다.)", rev, rev <= 1, "1 이하")
    anira = len(re.findall(r"[이가] 아니라", text))
    row("'~가 아니라 ~'", anira, anira <= 2, "2 이하")
    nominal = [s for s in S if L[id(s)] <= 12 and s.endswith(".") and not re.search(r"(다|요|죠|까|가|라|자)\.$", s)]
    row("동사 없는 명사 단문", len(nominal), len(nominal) <= 2, "2 이하", " / ".join(nominal[:3]))
    pairs = sum(1 for a, b in zip(S, S[1:]) if L[id(a)] <= 18 and L[id(b)] <= 18 and a.endswith("다.") and b.endswith("다."))
    row("18자 이하 '~다. ~다.' 연속", pairs, pairs <= 1, "1쌍 이하")
    if medium == "column":
        avg = sum(lens) / n
        row("평균 문장 길이(공백 제외)", f"{avg:.1f}자", avg >= 30, "30자 이상")
        long60 = sum(1 for l in lens if l > 60)
        need = max(1, round(3 * scale))
        row("60자 넘는 문장", long60, long60 >= need, f"{need}개 이상", f"전체의 {100*long60/n:.0f}% (저자 원문 10~15%)")
    mw = sum(text.count(w) for w in META_WORDS) - len(re.findall(r"산업구조|구조조정|구조개혁", text))
    row("구조·설계·작동·역설", mw, mw <= 1, "1 이하")
    for w in ("그런데", "하지만"):
        c = len(re.findall(rf"(?:^|[.?!]\s+|\n){w}", text))
        row(f"문두 '{w}'", c, c <= 1, "1 이하")
    we = text.count("우리는")
    row("주어 '우리는'", we, we <= 3, "3 이하")
    bold = len(re.findall(r"\*\*[^*]+\*\*", text)) + len(re.findall(r"^>", text, flags=re.M))
    row("굵은 글씨·인용블록", bold, bold == 0, "0")
    bn = [w for w in BANNED if w in text]
    row("금지 공식", len(bn), not bn, "0", ", ".join(bn))
    buf = [w for w in BUFFERS if w in text]
    if medium != "sns-light":
        row("완충어·연결어", len(buf), bool(buf), "1 이상", ", ".join(buf[:4]))
    rep = sorted({w.replace(" ", "") for w in REPERTOIRE if w in text})
    row("레퍼토리·속담·권위자(사전에 있는 것만)", len(rep), len(rep) <= 2, "2 이하", ", ".join(rep))
    if medium == "column":
        adv = {w: len(re.findall(rf"(?<![가-힣]){w}", text)) for w in ADVERBS}
        tot = sum(adv.values())
        row("강조 부사", tot, tot <= 1, "1 이하", ", ".join(f"{k}{v}" for k, v in adv.items() if v))
    pas = [m for w in PASSIVE for m in re.findall(w, text)]
    row("피동 표지(되어지다·에 의해)", len(pas), not pas, "0", ", ".join(pas))
    soft = find(r"(됐다|되었다|된다|되고 있다)\.$")
    row("'~됐다'로 끝난 문장(행위자 확인)", len(soft), True, "참고", " / ".join(x[-20:] for x in soft[:3]))
    if medium.startswith("sns"):
        bad = re.findall(r"ㅎㅎ|ㅠㅠ|[\U0001F300-\U0001FAFF☀-➿]", text)
        row("ㅎㅎ·ㅠㅠ·그림 이모지", len(bad), not bad, "0")
        lone = len(re.findall(r"(?<!ㅋ)ㅋ(?!ㅋ)", text))
        row("ㅋ 하나", lone, lone == 0, "0")
        ex = [m for m in re.findall(r"!+", text) if len(m) not in (1, 3)]
        row("느낌표(구호 뒤는 꼭 세 개)", len(ex), not ex, "1개 또는 3개")
        av = [w for w in SNS_AVOID if w in text]
        row("피할 말", len(av), not av, "0", ", ".join(av))
        endq = S[-1].endswith("?") if S else False
        row("질문으로 맺음", int(endq), True, "참고", "저자 글의 5%뿐")
    if medium == "sns-light":
        num = len(re.findall(r"\d[\d,.]*\s?(%|원|명|건|개|배)", text))
        row("근거 숫자", num, num <= 1, "1 이하")
        lst = len(re.findall(r"^\s*(\d+[.)]|[-•])\s", text, flags=re.M))
        row("번호·글머리 목록", lst, lst == 0, "0")
    return chars, n, rows

def main():
    ap = argparse.ArgumentParser(description="김현성체 AI 티 점검기 (golmok-writer 12장)")
    ap.add_argument("file")
    ap.add_argument("--medium", choices=["column", "sns", "sns-light"], default="column")
    a = ap.parse_args()
    text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8").read()
    chars, n, rows = check(text, a.medium)
    fails = [r for r in rows if r[3] == "고칠 것"]
    print(f"매체: {a.medium} · 글자 수(공백 제외) {chars} · 문장 {n}개 · 고칠 것 {len(fails)}건\n")
    print("| 항목 | 값 | 기준 | 판정 | 메모 |\n|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: r[3] != "고칠 것"):
        print("| " + " | ".join(str(x) for x in r) + " |")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
