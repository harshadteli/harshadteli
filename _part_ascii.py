from pathlib import Path

# Build ASCII without embedding pipe chars in source that PS might break
# Use # and / \ . for a cyber terminal face
P = chr(124)  # pipe
ASCII = [
"            .--.            ",
"         .-'    '-.         ",
"       .'  .--.    '.       ",
"      /  .'    '.    \\      ",
"     "+P+"  /  .--.  \\    "+P+"     ",
"     "+P+" "+P+"  /    \\  "+P+"   "+P+"     ",
"     "+P+" "+P+" "+P+" .  . "+P+" "+P+"   "+P+"     ",
"     "+P+" "+P+"  \\ -- /  "+P+"   "+P+"     ",
"     "+P+"  \\  '--'  /    "+P+"     ",
"      \\  '.____.'    /      ",
"       '.          .'       ",
"     .-' `'.____.'` '-.     ",
"   .'  .-.        .-.  '.   ",
"  /   /   \\  ..  /   \\   \\  ",
" "+P+"   "+P+"  .--\\    /--.  "+P+"   "+P+" ",
" "+P+"   "+P+" "+P+"    '  '    "+P+" "+P+"   "+P+" ",
"  \\   \\ \\          / /   /  ",
"   '.  '.\\        /.'  .'   ",
"     '-.  '------'  .-'     ",
"        '-..____..-'        ",
]

PHRASES = ["Software Developer","Full Stack Engineer","AI Enthusiast","Open Source Contributor","Java · Python · .NET"]
SKILLS = ["Java","Python","C#",".NET","JavaScript","PHP","HTML/CSS","Docker","Postgres","MongoDB","Git","MySQL"]
NAME="Harshad Teli"; LOC="Kolhapur, India"; EDU="B.C.S · The New College"; FOCUS="New Horizon · AI Tech"; PORT="harshadteli.github.io"; EMAIL="harshadteli697@gmail.com"

DARK = dict(bg="#030712",panel="#0F172A",border="rgba(255,255,255,0.08)",text="#F8FAFC",muted="#94A3B8",dim="#64748B",a1="#7C3AED",a2="#22D3EE",a3="#10B981",as1="#22D3EE",as2="#A78BFA",as3="#7C3AED",gc="#22D3EE",gv="#7C3AED",ge="#10B981",gb="#3B82F6",tbar="#0B1220",dr="#F87171",dy="#FBBF24",dg="#34D399",pbg="rgba(124,58,237,0.12)",pbd="rgba(34,211,238,0.25)",noise="0.045",glass="0.07",part="#22D3EE",scan="rgba(34,211,238,0.07)",icon="#94A3B8",prompt="#22D3EE")
LIGHT = dict(bg="#FFFFFF",panel="#F8FAFC",border="rgba(15,23,42,0.08)",text="#0F172A",muted="#475569",dim="#64748B",a1="#2563EB",a2="#06B6D4",a3="#10B981",as1="#2563EB",as2="#06B6D4",as3="#0EA5E9",gc="#06B6D4",gv="#2563EB",ge="#10B981",gb="#3B82F6",tbar="#F1F5F9",dr="#EF4444",dy="#F59E0B",dg="#10B981",pbg="rgba(37,99,235,0.08)",pbd="rgba(6,182,212,0.28)",noise="0.028",glass="0.5",part="#2563EB",scan="rgba(37,99,235,0.055)",icon="#475569",prompt="#2563EB")

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

print("ASCII lines:", len(ASCII))
print("sample:", ASCII[4])
Path("_ascii_ok.txt").write_text("\n".join(ASCII), encoding="utf-8")
