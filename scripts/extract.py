import glob
import os, re, shutil, sys

file = sys.argv[1]
dir = sys.argv[2]

urls = set()
with open(file) as f:
    for line in f:
        m = re.match("(http[s]?:[^ ]*) へ到達できません。", line)
        if m:
            print(m.group(1))
            urls.add(m.group(1))

def replaceText(m):
    if m.group(2) in urls:
        print(f"##found: {m.group(2)}")
        return f"<!-- CO {m.group(1)}{m.group(2)}{m.group(3)} -->{m.group(4)}<!-- {m.group(5)} -->"
    else:
        return f"{m.group(0)}"

l = glob.glob(f"{dir}**/*.htm*", recursive=True)
for html in l:
    if html.endswith(".tmp"):
        continue
    print(html)
    replaced = False
    src_name = html
    dst_name = f"{html}.tmp"
    with open(src_name) as src, open(dst_name, "w") as dst:
        text = src.read()
        m = re.search(
            '(<a\s+href=")(https?:[^"]*)("[^>]*>)([^<]+)(</a>)',
            text,
            flags=(re.MULTILINE | re.DOTALL))
        if m and m.group(2) in urls:
            print(f"found: {m.group(2)}")
        newText = re.sub(
            '(<a\s+href=")(https?:[^"]*)("[^>]*>)(.*?)(</a>)',
            replaceText,
            text,
            flags=(re.MULTILINE | re.DOTALL)
            )
        if text != newText:
#                print(m.group(1))
            print("replaced")
            replaced = True
        dst.write(newText)
    if replaced:
        shutil.copy(dst_name, src_name)
    os.remove(dst_name)
