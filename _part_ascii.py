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

PHRASES = ["Software Engineer","AI Developer","Full Stack & AI Engineer","Machine Learning","Java · Python · PyTorch"]
SKILLS = ["Java", "Python", "C#", ".NET", "TypeScript", "React", "PyTorch", "FastAPI", "Docker", "Postgres", "LLMs & AI", "Git"]
NAME="Harshad Teli"; LOC="Kolhapur, India"; EDU="B.C.S, M.C.A (Master in Computer Applications)"; FOCUS="Software Engineer & AI Developer"; PORT="harshadteli.github.io"; EMAIL="harshadteli697@gmail.com"

DARK = dict(bg="#080b11",panel="#0f1420",border="rgba(255,255,255,0.08)",text="#F8FAFC",muted="#94A3B8",dim="#64748B",a1="#8b5cf6",a2="#06b6d4",a3="#6366f1",as1="#06b6d4",as2="#a78bfa",as3="#8b5cf6",gc="#06b6d4",gv="#8b5cf6",ge="#6366f1",gb="#3b82f6",tbar="#0a0d16",dr="#F87171",dy="#FBBF24",dg="#34D399",pbg="rgba(139,92,246,0.1)",pbd="rgba(6,182,212,0.2)",noise="0.045",glass="0.07",part="#06b6d4",scan="rgba(6,182,212,0.07)",icon="#94A3B8",prompt="#06b6d4")
LIGHT = dict(bg="#FFFFFF",panel="#F8FAFC",border="rgba(15,23,42,0.08)",text="#0F172A",muted="#475569",dim="#64748B",a1="#4F46E5",a2="#06B6D4",a3="#4F46E5",as1="#4F46E5",as2="#06B6D4",as3="#0ea5e9",gc="#06B6D4",gv="#4F46E5",ge="#10B981",gb="#3B82F6",tbar="#F1F5F9",dr="#EF4444",dy="#F59E0B",dg="#10B981",pbg="rgba(79,70,229,0.06)",pbd="rgba(6,182,212,0.2)",noise="0.028",glass="0.5",part="#4F46E5",scan="rgba(79,70,229,0.055)",icon="#475569",prompt="#4F46E5")

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

print("ASCII lines:", len(ASCII))
print("sample:", ASCII[4])
Path("_ascii_ok.txt").write_text("\n".join(ASCII), encoding="utf-8")
