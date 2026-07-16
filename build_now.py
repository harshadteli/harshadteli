from pathlib import Path
import base64
import io

try:
    from PIL import Image
except ImportError:
    Image = None

def load_photo_data_uri():
    photo_path = Path("photo.png")
    if not photo_path.exists():
        raise FileNotFoundError("photo.png not found — place it next to build_now.py")
    raw = photo_path.read_bytes()
    mime = "image/png"
    if Image is not None:
        im = Image.open(photo_path).convert("RGB")
        # Fit left panel (~430x570) at 2x for sharpness, keep file small
        im.thumbnail((860, 1140), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=88, optimize=True)
        raw = buf.getvalue()
        mime = "image/jpeg"
    return "data:%s;base64,%s" % (mime, base64.b64encode(raw).decode("ascii"))

PHOTO_URI = load_photo_data_uri()

PHRASES = ["Software Developer","Full Stack Engineer","AI Enthusiast","Open Source Contributor","Java · Python · .NET"]
# Safe pixel widths for font-size 22 / weight 600 (Inter/Segoe) + padding so nothing clips
PHRASE_WIDTHS = [255, 250, 175, 330, 265]
SKILLS = ["Java","Python","C#",".NET","JavaScript","PHP","HTML/CSS","Docker","Postgres","MongoDB","Git","MySQL"]
NAME="Harshad Teli"; LOC="Kolhapur, India"; EDU="B.C.S · The New College"; FOCUS="New Horizon · AI Tech"; PORT="harshadteli.github.io"; EMAIL="harshadteli697@gmail.com"

def fmt_kt(*times):
    """Strictly increasing keyTimes in [0, 1] (SVG rejects duplicates)."""
    out = []
    prev = -1.0
    for i, t in enumerate(times):
        t = max(0.0, min(1.0, float(t)))
        if i == 0:
            t = 0.0
        elif i == len(times) - 1:
            t = 1.0
        if t <= prev:
            t = min(1.0, prev + 0.0001)
        out.append("%.4f" % t)
        prev = t
    return ";".join(out)

DARK = dict(bg="#030712",panel="#0F172A",border="rgba(255,255,255,0.08)",text="#F8FAFC",muted="#94A3B8",dim="#64748B",a1="#7C3AED",a2="#22D3EE",a3="#10B981",as1="#22D3EE",as2="#A78BFA",as3="#7C3AED",gc="#22D3EE",gv="#7C3AED",ge="#10B981",gb="#3B82F6",tbar="#0B1220",dr="#F87171",dy="#FBBF24",dg="#34D399",pbg="rgba(124,58,237,0.12)",pbd="rgba(34,211,238,0.25)",noise="0.045",glass="0.07",part="#22D3EE",scan="rgba(34,211,238,0.07)",icon="#94A3B8",prompt="#22D3EE")
LIGHT = dict(bg="#FFFFFF",panel="#F8FAFC",border="rgba(15,23,42,0.08)",text="#0F172A",muted="#475569",dim="#64748B",a1="#2563EB",a2="#06B6D4",a3="#10B981",as1="#2563EB",as2="#06B6D4",as3="#0EA5E9",gc="#06B6D4",gv="#2563EB",ge="#10B981",gb="#3B82F6",tbar="#F1F5F9",dr="#EF4444",dy="#F59E0B",dg="#10B981",pbg="rgba(37,99,235,0.08)",pbd="rgba(6,182,212,0.28)",noise="0.028",glass="0.5",part="#2563EB",scan="rgba(37,99,235,0.055)",icon="#475569",prompt="#2563EB")

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def build(tid, t):
    parts = []
    A = parts.append
    A('<?xml version="1.0" encoding="UTF-8"?>')
    A('<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1180 610" role="img" aria-label="Harshad Teli Software Developer GitHub profile banner">')
    A('<title>Harshad Teli Premium GitHub Profile Banner ('+tid+')</title>')
    A('<defs>')
    A('<linearGradient id="'+tid+'-accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    for off, col, vals in [("0%",t["a1"],t["a1"]+";"+t["a2"]+";"+t["a3"]+";"+t["a1"]),("50%",t["a2"],t["a2"]+";"+t["a3"]+";"+t["a1"]+";"+t["a2"]),("100%",t["a3"],t["a3"]+";"+t["a1"]+";"+t["a2"]+";"+t["a3"])]:
        A('<stop offset="'+off+'" stop-color="'+col+'"><animate attributeName="stop-color" values="'+vals+'" dur="8s" repeatCount="indefinite"/></stop>')
    A('<animateTransform attributeName="gradientTransform" type="translate" values="-0.3 0;0.3 0;-0.3 0" dur="6s" repeatCount="indefinite"/>')
    A('</linearGradient>')
    A('<linearGradient id="'+tid+'-borderShimmer" x1="0%" y1="0%" x2="100%" y2="100%">')
    A('<stop offset="0%" stop-color="'+t["a1"]+'" stop-opacity="0"/><stop offset="40%" stop-color="'+t["a2"]+'" stop-opacity="0.85"/><stop offset="60%" stop-color="'+t["a1"]+'" stop-opacity="0.85"/><stop offset="100%" stop-color="'+t["a3"]+'" stop-opacity="0"/>')
    A('<animateTransform attributeName="gradientTransform" type="rotate" from="0 0.5 0.5" to="360 0.5 0.5" dur="10s" repeatCount="indefinite"/>')
    A('</linearGradient>')
    A('<linearGradient id="'+tid+'-glassReflect" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.14"/><stop offset="35%" stop-color="#FFFFFF" stop-opacity="0.03"/><stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>')
    A('<linearGradient id="'+tid+'-photoVignette" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#000000" stop-opacity="0.35"/><stop offset="28%" stop-color="#000000" stop-opacity="0"/><stop offset="72%" stop-color="#000000" stop-opacity="0"/><stop offset="100%" stop-color="#000000" stop-opacity="0.45"/></linearGradient>')
    A('<radialGradient id="'+tid+'-bgGlow1" cx="18%" cy="30%" r="42%"><stop offset="0%" stop-color="'+t["gb"]+'" stop-opacity="0.22"/><stop offset="100%" stop-color="'+t["gb"]+'" stop-opacity="0"/></radialGradient>')
    A('<radialGradient id="'+tid+'-bgGlow2" cx="82%" cy="25%" r="40%"><stop offset="0%" stop-color="'+t["gv"]+'" stop-opacity="0.2"/><stop offset="100%" stop-color="'+t["gv"]+'" stop-opacity="0"/></radialGradient>')
    A('<radialGradient id="'+tid+'-bgGlow3" cx="70%" cy="85%" r="38%"><stop offset="0%" stop-color="'+t["ge"]+'" stop-opacity="0.14"/><stop offset="100%" stop-color="'+t["ge"]+'" stop-opacity="0"/></radialGradient>')
    A('<clipPath id="'+tid+'-frame"><rect x="0" y="0" width="1180" height="610" rx="28" ry="28"/></clipPath>')
    A('<clipPath id="'+tid+'-leftPanel"><rect x="20" y="20" width="430" height="570" rx="22" ry="22"/></clipPath>')
    A('<filter id="'+tid+'-noise" x="0%" y="0%" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="4" stitchTiles="stitch"><animate attributeName="baseFrequency" values="0.85;0.9;0.85" dur="8s" repeatCount="indefinite"/></feTurbulence><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="linear" slope="0.55"/></feComponentTransfer></filter>')
    A('<filter id="'+tid+'-softGlow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    A('<filter id="'+tid+'-panelShadow" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="12" stdDeviation="24" flood-color="#000000" flood-opacity="0.35"/></filter>')
    A('<filter id="'+tid+'-pillGlow" x="-30%" y="-40%" width="160%" height="180%"><feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    phrase_dur=3.6; type_in=1.55; hold_tail=0.55; erase_tail=0.2
    total=len(PHRASES)*phrase_dur
    for i,phrase in enumerate(PHRASES):
        begin=i*phrase_dur
        max_w=PHRASE_WIDTHS[i]
        # type: begin → begin+type_in | hold → begin+phrase_dur-hold_tail | erase → begin+phrase_dur-erase_tail
        t0=begin/total
        t1=(begin+type_in)/total
        t2=(begin+phrase_dur-hold_tail)/total
        t3=(begin+phrase_dur-erase_tail)/total
        A('<clipPath id="'+tid+'-typeClip'+str(i)+'"><rect x="0" y="-8" width="0" height="40"><animate attributeName="width" values="0;0;'+str(max_w)+';'+str(max_w)+';0;0" keyTimes="'+fmt_kt(0,t0,t1,t2,t3,1)+'" dur="'+("%.1f"%total)+'s" repeatCount="indefinite" calcMode="linear"/></rect></clipPath>')
    A('</defs>')
    A('<g clip-path="url(#'+tid+'-frame)">')
    A('<rect width="1180" height="610" fill="'+t["bg"]+'"/>')
    A('<ellipse cx="220" cy="200" rx="280" ry="240" fill="url(#'+tid+'-bgGlow1)"><animate attributeName="cx" values="220;260;220" dur="12s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.7;1;0.7" dur="6s" repeatCount="indefinite"/></ellipse>')
    A('<ellipse cx="920" cy="160" rx="300" ry="260" fill="url(#'+tid+'-bgGlow2)"><animate attributeName="cy" values="160;200;160" dur="14s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;1;0.6" dur="7s" repeatCount="indefinite"/></ellipse>')
    A('<ellipse cx="800" cy="520" rx="260" ry="200" fill="url(#'+tid+'-bgGlow3)"><animate attributeName="cx" values="800;760;800" dur="11s" repeatCount="indefinite"/></ellipse>')
    A('<rect width="1180" height="610" filter="url(#'+tid+'-noise)" opacity="'+t["noise"]+'"/>')
    A('<rect x="0" y="-40" width="1180" height="48" fill="'+t["scan"]+'" pointer-events="none"><animate attributeName="y" values="-40;650" dur="5.5s" repeatCount="indefinite"/></rect>')
    A('<g opacity="0.85">')
    coords=[(120,80,1.6,"0s",7),(220,160,1.2,"1.2s",9),(80,280,1.4,"0.6s",8),(340,120,1.1,"2s",10),(280,360,1.5,"0.3s",7.5),(160,420,1.0,"1.8s",11),(400,240,1.3,"0.9s",8.5),(60,500,1.2,"2.4s",9.5),(720,90,1.1,"0.4s",8),(900,180,1.4,"1.5s",10),(1040,320,1.0,"0.7s",7),(820,450,1.3,"2.1s",9),(980,520,1.2,"1.1s",8),(1100,140,1.0,"2.8s",11),(640,540,1.5,"0.2s",7.5)]
    for x,y,r,begin,dur in coords:
        A('<circle cx="'+str(x)+'" cy="'+str(y)+'" r="'+str(r)+'" fill="'+t["part"]+'" opacity="0.35" filter="url(#'+tid+'-softGlow)"><animate attributeName="cy" values="'+str(y)+';'+str(y-28)+';'+str(y)+'" dur="'+str(dur)+'s" begin="'+begin+'" repeatCount="indefinite"/><animate attributeName="opacity" values="0.15;0.55;0.15" dur="'+str(dur)+'s" begin="'+begin+'" repeatCount="indefinite"/><animate attributeName="r" values="'+str(r)+';'+("%.2f"%(r*1.4))+';'+str(r)+'" dur="'+("%.1f"%(dur*1.2))+'s" begin="'+begin+'" repeatCount="indefinite"/></circle>')
    A('</g>')
    A('<g filter="url(#'+tid+'-panelShadow)"><rect x="20" y="20" width="430" height="570" rx="22" ry="22" fill="'+t["panel"]+'" stroke="url(#'+tid+'-borderShimmer)" stroke-width="1.25" opacity="0.96"/><rect x="21.5" y="21.5" width="427" height="567" rx="21" ry="21" fill="none" stroke="'+t["border"]+'" stroke-width="1"/></g>')
    A('<g clip-path="url(#'+tid+'-leftPanel)">')
    A('<image href="'+PHOTO_URI+'" x="20" y="20" width="430" height="570" preserveAspectRatio="xMidYMid slice" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.8s" begin="0.15s" fill="freeze"/></image>')
    A('<rect x="20" y="20" width="430" height="570" fill="url(#'+tid+'-photoVignette)" opacity="0.85" pointer-events="none"/>')
    A('<rect x="20" y="20" width="430" height="120" fill="url(#'+tid+'-glassReflect)" opacity="0.55" pointer-events="none"/>')
    A('</g>')
    A('<g transform="translate(40, 38)" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.5s" fill="freeze"/><circle cx="0" cy="0" r="5" fill="'+t["dr"]+'" opacity="0.95"/><circle cx="16" cy="0" r="5" fill="'+t["dy"]+'" opacity="0.95"/><circle cx="32" cy="0" r="5" fill="'+t["dg"]+'" opacity="0.95"/><text x="52" y="4" fill="#F8FAFC" font-family="JetBrains Mono,Consolas,monospace" font-size="11" opacity="0.9">photo://portrait</text></g>')
    A('<rect x="20" y="20" width="430" height="570" rx="22" ry="22" fill="none" stroke="url(#'+tid+'-borderShimmer)" stroke-width="1.25" pointer-events="none"/>')
    A('<g filter="url(#'+tid+'-panelShadow)"><rect x="470" y="20" width="690" height="570" rx="22" ry="22" fill="'+t["panel"]+'" stroke="url(#'+tid+'-borderShimmer)" stroke-width="1.25" opacity="0.97"/><rect x="470" y="20" width="690" height="200" rx="22" ry="22" fill="url(#'+tid+'-glassReflect)" opacity="'+t["glass"]+'"/><rect x="471.5" y="21.5" width="687" height="567" rx="21" ry="21" fill="none" stroke="'+t["border"]+'" stroke-width="1"/></g>')
    A('<rect x="470" y="20" width="690" height="44" rx="22" ry="22" fill="'+t["tbar"]+'" opacity="0.92"/><rect x="470" y="42" width="690" height="22" fill="'+t["tbar"]+'" opacity="0.92"/>')
    A('<g transform="translate(492, 42)"><circle cx="0" cy="0" r="5" fill="'+t["dr"]+'"/><circle cx="16" cy="0" r="5" fill="'+t["dy"]+'"/><circle cx="32" cy="0" r="5" fill="'+t["dg"]+'"/><text x="56" y="4" fill="'+t["dim"]+'" font-family="JetBrains Mono,Consolas,monospace" font-size="11.5">harshadteli@github ~ profile</text></g>')
    A('<g transform="translate(500, 100)">')
    A('<text x="0" y="0" fill="'+t["text"]+'" font-family="Inter,SF Pro Display,system-ui,sans-serif" font-size="28" font-weight="700" letter-spacing="-0.5" opacity="0">Hi &#x1F44B; I\'m '+esc(NAME)+'<animate attributeName="opacity" values="0;1" dur="0.55s" begin="0.2s" fill="freeze"/><animateTransform attributeName="transform" type="translate" from="0 12" to="0 0" dur="0.55s" begin="0.2s" fill="freeze"/></text>')
    A('<g transform="translate(0, 42)"><text x="0" y="0" fill="'+t["prompt"]+'" font-family="JetBrains Mono,Consolas,monospace" font-size="14" opacity="0">$ whoami<animate attributeName="opacity" values="0;1" dur="0.4s" begin="0.7s" fill="freeze"/></text></g>')
    A('<g transform="translate(0, 78)">')
    for i,phrase in enumerate(PHRASES):
        begin=i*phrase_dur
        max_w=PHRASE_WIDTHS[i]
        # Visible slightly before type starts; hide after erase completes
        o0=begin/total
        o1=(begin+0.02)/total
        o2=(begin+phrase_dur-erase_tail)/total
        o3=(begin+phrase_dur-0.02)/total
        A('<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="'+fmt_kt(0,o0,o1,o2,o3,1)+'" dur="'+("%.1f"%total)+'s" repeatCount="indefinite"/>')
        A('<g clip-path="url(#'+tid+'-typeClip'+str(i)+')"><text x="0" y="0" fill="url(#'+tid+'-accentGrad)" font-family="Inter,SF Pro Display,Segoe UI,system-ui,sans-serif" font-size="22" font-weight="600" letter-spacing="-0.2">'+esc(phrase)+'</text></g></g>')
        # Cursor tracks this phrase's type/hold/erase window
        c0=begin/total
        c1=(begin+type_in)/total
        c2=(begin+phrase_dur-hold_tail)/total
        c3=(begin+phrase_dur-erase_tail)/total
        A('<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="'+fmt_kt(0,o0,o1,o2,o3,1)+'" dur="'+("%.1f"%total)+'s" repeatCount="indefinite"/>')
        A('<rect x="0" y="-16" width="2.5" height="22" rx="1" fill="'+t["a2"]+'" filter="url(#'+tid+'-softGlow)">')
        A('<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.48;0.5;1" dur="0.85s" repeatCount="indefinite"/>')
        A('<animate attributeName="x" values="0;0;'+str(max_w)+';'+str(max_w)+';0;0" keyTimes="'+fmt_kt(0,c0,c1,c2,c3,1)+'" dur="'+("%.1f"%total)+'s" repeatCount="indefinite" calcMode="linear"/>')
        A('</rect></g>')
    A('</g>')
    A('<g transform="translate(0, 118)">')
    rows=[("Location",LOC),("Education",EDU),("Focus",FOCUS),("Portfolio",PORT),("Email",EMAIL)]
    for i,(label,value) in enumerate(rows):
        y=i*26; delay=3.0+i*0.35
        A('<g transform="translate(0,'+str(y)+')" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.45s" begin="'+("%.2f"%delay)+'s" fill="freeze"/><animateTransform attributeName="transform" type="translate" from="0 '+str(y+10)+'" to="0 '+str(y)+'" dur="0.45s" begin="'+("%.2f"%delay)+'s" fill="freeze"/><text x="0" y="0" fill="'+t["dim"]+'" font-family="JetBrains Mono,Consolas,monospace" font-size="12">'+esc(label)+'</text><text x="100" y="0" fill="'+t["muted"]+'" font-family="Inter,system-ui,sans-serif" font-size="12.5" font-weight="500">'+esc(value)+'</text></g>')
    A('</g>')
    A('<g transform="translate(0, 268)" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="4.6s" fill="freeze"/><text x="0" y="0" fill="'+t["dim"]+'" font-family="JetBrains Mono,Consolas,monospace" font-size="11" letter-spacing="1.2">SKILLS</text><g transform="translate(0, 24)">')
    x=y=0; gap_x=8; gap_y=10; row_h=30; max_w=620; pad_x=12
    for i,skill in enumerate(SKILLS):
        tw=len(skill)*6.8+pad_x*2
        if x+tw>max_w:
            x=0; y+=row_h+gap_y
        delay=4.8+i*0.12
        A('<g transform="translate('+str(x)+','+str(y)+')" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="'+("%.2f"%delay)+'s" fill="freeze"/><g><animateTransform attributeName="transform" type="scale" values="1;1.045;1" dur="'+("%.1f"%(2.8+(i%5)*0.35))+'s" begin="'+("%.2f"%(delay+0.5))+'s" repeatCount="indefinite" additive="sum"/><rect x="0" y="-14" width="'+("%.1f"%tw)+'" height="28" rx="14" fill="'+t["pbg"]+'" stroke="'+t["pbd"]+'" stroke-width="1" filter="url(#'+tid+'-pillGlow)"><animate attributeName="stroke-opacity" values="0.4;1;0.4" dur="'+("%.1f"%(2.4+(i%4)*0.4))+'s" begin="'+("%.2f"%delay)+'s" repeatCount="indefinite"/></rect><text x="'+("%.1f"%(tw/2))+'" y="2" text-anchor="middle" fill="'+t["text"]+'" font-family="Inter,system-ui,sans-serif" font-size="11.5" font-weight="500">'+esc(skill)+'</text></g></g>')
        x+=tw+gap_x
    A('</g></g>')
    A('<g transform="translate(0, 380)"><text x="0" y="0" fill="'+t["dim"]+'" opacity="0" font-family="JetBrains Mono,Consolas,monospace" font-size="11" letter-spacing="1.2">CONNECT<animate attributeName="opacity" values="0;1" dur="0.4s" begin="6.0s" fill="freeze"/></text><g transform="translate(0, 18)">')
    gh='<path d="M12 2C6.48 2 2 6.58 2 12.26c0 4.52 2.87 8.35 6.84 9.7.5.1.68-.22.68-.48 0-.24-.01-.87-.01-1.7-2.78.62-3.37-1.37-3.37-1.37-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.63.07-.63 1 .07 1.53 1.06 1.53 1.06.89 1.56 2.34 1.11 2.91.85.09-.66.35-1.11.63-1.37-2.22-.26-4.56-1.14-4.56-5.07 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.7 0 0 .84-.27 2.75 1.05A9.3 9.3 0 0 1 12 6.8c.85 0 1.71.12 2.51.35 1.91-1.32 2.75-1.05 2.75-1.05.55 1.4.2 2.44.1 2.7.64.72 1.03 1.63 1.03 2.75 0 3.94-2.34 4.8-4.57 5.06.36.32.68.94.68 1.9 0 1.37-.01 2.47-.01 2.81 0 .26.18.58.69.48A10.03 10.03 0 0 0 22 12.26C22 6.58 17.52 2 12 2z" fill="currentColor"/>'
    li='<path d="M4.98 3.5C4.98 4.88 3.86 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8.5h4V23h-4V8.5zm7.5 0h3.8v2h.05c.53-1 1.82-2.05 3.75-2.05 4.01 0 4.75 2.64 4.75 6.07V23h-4v-6.7c0-1.6-.03-3.66-2.23-3.66-2.23 0-2.57 1.74-2.57 3.54V23h-4V8.5z" fill="currentColor"/>'
    yt='<path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31.5 31.5 0 0 0 0 12a31.5 31.5 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31.5 31.5 0 0 0 24 12a31.5 31.5 0 0 0-.5-5.8zM9.75 15.5v-7l6.5 3.5-6.5 3.5z" fill="currentColor"/>'
    pf='<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
    for i,path in enumerate([gh,li,yt,pf]):
        cx=i*52; delay=6.2+i*0.15
        A('<g transform="translate('+str(cx)+',0)" opacity="0" color="'+t["icon"]+'"><animate attributeName="opacity" values="0;1" dur="0.4s" begin="'+("%.2f"%delay)+'s" fill="freeze"/><circle cx="16" cy="16" r="16" fill="'+t["pbg"]+'" stroke="'+t["pbd"]+'" stroke-width="1"><animate attributeName="stroke-opacity" values="0.35;0.9;0.35" dur="3s" begin="'+("%.2f"%delay)+'s" repeatCount="indefinite"/></circle><g transform="translate(8,8) scale(0.66)" filter="url(#'+tid+'-softGlow)">'+path+'</g><animateTransform attributeName="transform" type="translate" values="'+str(cx)+',0;'+str(cx)+',-2;'+str(cx)+',0" dur="'+("%.1f"%(3.2+i*0.4))+'s" begin="'+("%.2f"%delay)+'s" repeatCount="indefinite"/></g>')
    A('</g></g>')
    A('</g>')
    A('<rect x="1" y="1" width="1178" height="608" rx="27" ry="27" fill="none" stroke="url(#'+tid+'-borderShimmer)" stroke-width="1.5" opacity="0.7"/>')
    A('</g></svg>')
    return "\n".join(parts)

out = Path('.')
for name, theme in (("dark", DARK), ("light", LIGHT)):
    path = out / (name + ".svg")
    path.write_text(build(name, theme), encoding="utf-8")
    print("Wrote", path.name, path.stat().st_size, "bytes")