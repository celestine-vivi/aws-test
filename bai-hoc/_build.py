# -*- coding: utf-8 -*-
"""Gộp các bài tuần thành bộ trang hoàn chỉnh.

Hai chế độ:
- python bai-hoc/_build.py          -> bai-hoc/dist/ để publish artifact claude.ai (index.html dạng headless).
- python bai-hoc/_build.py --pages  -> site/ ở gốc repo cho GitHub Pages (mọi trang là HTML đầy đủ, có .nojekyll).


- index.html: dashboard, giữ dạng headless (artifact bọc skeleton), chỉ thay /*WEEKS*/ bằng dữ liệu thật.
- tuan-XX.html, tuan-XX.ja.html: bọc doctype/head/body, chèn thanh trên cùng (về dashboard + chuyển ngôn ngữ)
  và script ghi nhớ ngôn ngữ đã chọn.
Chạy: python bai-hoc/_build.py  (từ thư mục Desktop\\AWS)
"""
import io, os, re, json, sys, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = "--pages" in sys.argv
DIST = os.path.join(os.path.dirname(HERE), "site") if PAGES else os.path.join(HERE, "dist")
if PAGES and os.path.isdir(DIST):
    shutil.rmtree(DIST)
os.makedirs(DIST, exist_ok=True)

ORDER = ["tuan-01", "tuan-02-03", "tuan-03", "tuan-04", "tuan-05", "tuan-06",
         "tuan-07", "tuan-08", "tuan-09", "tuan-10", "tuan-11", "tuan-12"]

TOPBAR_CSS = """
/* Thanh trên cùng do _build.py chèn: về dashboard và chuyển ngôn ngữ */
.topbar{max-width:1120px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;gap:12px;padding-top:12px;font-size:.88rem;flex-wrap:wrap}
.topbar a{text-decoration:none}
.topbar .lang{display:flex;gap:4px}
.topbar .lang a{padding:3px 11px;border:1px solid var(--line);border-radius:99px;color:var(--muted)}
.topbar .lang a.on{background:var(--accent-soft);color:var(--accent);border-color:var(--accent)}
.topbar .lang a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
"""

HEAD_RESET = ('<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
              '<style>html,body{margin:0}[hidden]{display:none!important}img{max-width:100%}'
              ':root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>')


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


def count_ck(src):
    return len(re.findall(r'<input[^>]*data-ck', src))


def wrap(src, lang, this_file, other_file):
    """src: nội dung headless (title, meta, link, style, header...). Trả về tài liệu HTML đầy đủ."""
    marker = '<header class="hero">'
    i = src.index(marker)
    head, body = src[:i], src[i:]
    head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">', '')
    head = head.replace('</style>', TOPBAR_CSS + '</style>', 1)
    back = '← Tổng quan 12 tuần' if lang == 'vi' else '← 12週間の一覧'
    vi_a = ('<a class="on">Tiếng Việt</a>' if lang == 'vi'
            else '<a href="%s" data-setlang="vi">Tiếng Việt</a>' % other_file)
    if other_file is None and lang == 'vi':
        ja_a = ''
    else:
        ja_a = ('<a class="on">日本語</a>' if lang == 'ja'
                else '<a href="%s" data-setlang="ja">日本語</a>' % other_file)
    topbar = ('<div class="topbar"><a href="index.html">%s</a>'
              '<span class="lang" role="group" aria-label="Language">%s%s</span></div>\n' % (back, vi_a, ja_a))
    other_js = json.dumps(other_file) if other_file else 'null'
    lang_js = ("<script>(function(){var L=%s,O=%s;try{var p=localStorage.getItem('saa-lang');"
               "if(O&&p&&p!==L&&(p==='vi'||p==='ja')){location.replace(O);return}}catch(e){}"
               "document.querySelectorAll('[data-setlang]').forEach(function(a){a.addEventListener('click',function(){"
               "try{localStorage.setItem('saa-lang',a.getAttribute('data-setlang'))}catch(e){}})})})();</script>\n"
               % (json.dumps(lang), other_js))
    return ('<!doctype html>\n<html lang="%s">\n<head>\n%s\n%s</head>\n<body>\n%s%s\n%s</body>\n</html>\n'
            % (lang, HEAD_RESET, head.strip() + "\n", topbar, body.strip(), lang_js))


weeks = []
for name in ORDER:
    vi_path = os.path.join(HERE, name + ".html")
    ja_path = os.path.join(HERE, name + ".ja.html")
    if not os.path.exists(vi_path):
        print("bỏ qua, thiếu", vi_path)
        continue
    vi = read(vi_path)
    has_ja = os.path.exists(ja_path)
    weeks.append({"file": name, "total": count_ck(vi), "ja": has_ja})
    write(os.path.join(DIST, name + ".html"), wrap(vi, "vi", name + ".html", name + ".ja.html" if has_ja else None))
    if has_ja:
        ja = read(ja_path)
        if count_ck(ja) != count_ck(vi):
            print("CẢNH BÁO: số mục checklist lệch", name, count_ck(vi), count_ck(ja))
        write(os.path.join(DIST, name + ".ja.html"), wrap(ja, "ja", name + ".ja.html", name + ".html"))

idx = read(os.path.join(HERE, "index.html"))
idx = re.sub(r'/\*WEEKS\*/.*?/\*/WEEKS\*/', '/*WEEKS*/' + json.dumps(weeks, ensure_ascii=False) + '/*/WEEKS*/', idx, flags=re.S)
if PAGES:
    # GitHub Pages không bọc skeleton như artifact, nên tự thêm doctype/head/body cho dashboard.
    i = idx.index('<div class="wrap">')
    head = idx[:i].replace('<meta charset="utf-8">', '').replace('<meta name="claude:viewport-fit-sides" content="cover">', '')
    idx = ('<!doctype html>\n<html lang="vi">\n<head>\n%s\n%s</head>\n<body>\n%s</body>\n</html>\n'
           % (HEAD_RESET, head.strip() + "\n", idx[i:].strip() + "\n"))
    write(os.path.join(DIST, ".nojekyll"), "")
write(os.path.join(DIST, "index.html"), idx)

print("dist:", ", ".join(w["file"] + ("+ja" if w["ja"] else "") for w in weeks))
if PAGES:
    print("site:", DIST)
    sys.exit(0)
print("files map:")
files = {}
for w in weeks:
    files[w["file"] + ".html"] = "bai-hoc/dist/" + w["file"] + ".html"
    if w["ja"]:
        files[w["file"] + ".ja.html"] = "bai-hoc/dist/" + w["file"] + ".ja.html"
print(json.dumps(files, indent=1))
