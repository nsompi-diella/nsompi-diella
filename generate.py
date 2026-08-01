import json
import os

# Création du dossier assets s'il n'existe pas
os.makedirs("assets", exist_ok=True)

# Lecture du fichier JSON
with open("skills.json", "r") as file:
    skills = json.load(file)

BAR_WIDTH = 280
BAR_HEIGHT = 20

for skill in skills:

    progress = skill["progress"]
    color = skill["color"]
    name = skill["name"]

    filled_width = BAR_WIDTH * progress / 100

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{BAR_WIDTH}"
height="{BAR_HEIGHT}"
viewBox="0 0 {BAR_WIDTH} {BAR_HEIGHT}">

<rect
x="0"
y="0"
width="{BAR_WIDTH}"
height="{BAR_HEIGHT}"
rx="10"
fill="#2b2f3a"/>

<rect
x="0"
y="0"
width="{filled_width}"
height="{BAR_HEIGHT}"
rx="10"
fill="{color}"/>

<text
x="{BAR_WIDTH-8}"
y="14"
text-anchor="end"
font-family="Verdana"
font-size="11"
font-weight="bold"
fill="white">

{progress}%

</text>

</svg>
"""

    filename = f"assets/{name.lower().replace(' ', '_')}.svg"

    with open(filename, "w") as file:
        file.write(svg)

    print(f"{filename} créé.")

print("\nTous les SVG ont été générés.")
