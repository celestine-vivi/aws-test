#!/bin/sh
# Kiểm tra cấu trúc từng file bai-hoc/tuan-XX.html
cd "$(dirname "$0")"
for f in tuan-*.html; do
  n=$(echo "$f" | sed 's/tuan-\(..\).*/\1/')
  size=$(wc -c < "$f")
  title=$(grep -o '<title>[^<]*' "$f" | head -1 | sed 's/<title>//')
  secs=$(grep -c '<section' "$f")
  ck=$(grep -c 'data-ck' "$f")
  pct=$(grep -o 'id="pct">[^<]*' "$f" | sed 's/.*>//')
  scripts=$(grep -c '<script' "$f")
  key=$(grep -o "KEY='[^']*'" "$f")
  q=$(grep -c 'data-reveal' "$f")
  style=$(grep -c '<style' "$f")
  tocn=$(grep -o 'class="toc"' "$f" | wc -l)
  echo "$f | $size B | $title | sections=$secs | checklist=$ck pct=$pct | q=$q | script=$scripts style=$style toc=$tocn | $key"
done
