import json
import os

with open("skills.json", "r") as f:
    skills = json.load(f)

def make_bar(percent, color):
    fill_width = round(280 * percent / 100)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="280" height="20" viewBox="0 0 280 20">
  <rect x="0" y="0" width="280" height="20" rx="10" fill="#2b2f3a"/>
  <rect x="0" y="0" width="{fill_width}" height="20" rx="10" fill="{color}"/>
  <text x="272" y="14" text-anchor="end" font-family="Verdana, sans-serif" font-size="11" font-weight="bold" fill="#ffffff">{percent}%</text>
</svg>'''

os.makedirs("assets", exist_ok=True)

for name, data in skills.items():
    svg_content = make_bar(data["percent"], data["color"])
    path = f"assets/{name}.svg"
    with open(path, "w") as f:
        f.write(svg_content)
    print(f"Généré : {path} ({data['percent']}%)")
