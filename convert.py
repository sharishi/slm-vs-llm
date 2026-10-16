from bs4 import BeautifulSoup
import re, requests, html2text

url = "https://arxiv.org/html/2106.09685v2"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

for m in soup.find_all("math"):
    latex = m.get("alttext", "")
    if latex:
        # display или inline
        disp = m.get("display") == "block"
        m.replace_with(f"$${latex}$$" if disp else f"${latex}$")

h = html2text.HTML2Text()
h.body_width = 0
md = h.handle(str(soup))
open("data/01_LLM/LoRA_Low-Rank_Adaptation_of_Large_Language_Models.md", "w", encoding="utf-8").write(md)