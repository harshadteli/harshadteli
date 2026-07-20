#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ASCII_LINES = [
    r"            .--.            ",
    r"         .-'    '-.         ",
    r"       .'  .--.    '.       ",
    r"      /  .'    '.    \\      ",
    r"     |  /  .--.  \\    |     ",
    r"     | |  /    \\  |   |     ",
    r"     | | | .  . | |   |     ",
    r"     | |  \\ -- /  |   |     ",
    r"     |  \\  '--'  /    |     ",
    r"      \\  '.____.'    /      ",
    r"       '.          .'       ",
    r"     .-' '.____.'\ '-.     ",
    r"   .'  .-.        .-.  '.   ",
    r"  /   /   \\  ..  /   \\   \\  ",
    r" |   |  .--\\    /--.  |   | ",
    r" |   | |    '  '    | |   | ",
    r"  \\   \\ \\          / /   /  ",
    r"   '.  '.\\        /.'  .'   ",
    r"     '-.  '------'  .-'     ",
    r"        '-..____..-'        ",
]

TYPING_PHRASES = [
    "Software Developer",
    "Full Stack Engineer",
    "AI Enthusiast",
    "Open Source Contributor",
    "Java · Python · .NET",
]

SKILLS = [
    "Java", "Python", "C#", ".NET", "JavaScript", "PHP",
    "HTML/CSS", "Docker", "Postgres", "MongoDB", "Git", "MySQL",
]

NAME = "Harshad Teli"
LOCATION = "Kolhapur, India"
EDUCATION = "B.C.S,M.C.A"
FOCUS = "Software Enginner and AI Developer"
PORTFOLIO = "https://harshadteli.onrender.com"
EMAIL = "harshadteli697@gmail.com"

THEMES = {
    "dark": {
        "bg": "#030712", "panel": "#0F172A", "border": "rgba(255,255,255,0.08)",
        "text": "#F8FAFC", "muted": "#94A3B8", "dim": "#64748B",
        "accent1": "#7C3AED", "accent2": "#22D3EE", "accent3": "#10B981",
        "ascii1": "#22D3EE", "ascii2": "#A78BFA", "ascii3": "#7C3AED",
        "glow_cyan": "#22D3EE", "glow_violet": "#7C3AED", "glow_emerald": "#10B981",
        "glow_blue": "#3B82F6", "terminal_bar": "#0B1220",
        "dot_r": "#F87171", "dot_y": "#FBBF24", "dot_g": "#34D399",
        "pill_bg": "rgba(124,58,237,0.12)", "pill_border": "rgba(34,211,238,0.25)",
        "noise_opacity": "0.045", "glass_opacity": "0.07", "particle": "#22D3EE",
        "scanline": "rgba(34,211,238,0.07)", "icon_fill": "#94A3B8", "prompt": "#22D3EE",
    },
    "light": {
        "bg": "#FFFFFF", "panel": "#F8FAFC", "border": "rgba(15,23,42,0.08)",
        "text": "#0F172A", "muted": "#475569", "dim": "#64748B",
        "accent1": "#2563EB", "accent2": "#06B6D4", "accent3": "#10B981",
        "ascii1": "#2563EB", "ascii2": "#06B6D4", "ascii3": "#0EA5E9",
        "glow_cyan": "#06B6D4", "glow_violet": "#2563EB", "glow_emerald": "#10B981",
        "glow_blue": "#3B82F6", "terminal_bar": "#F1F5F9",
        "dot_r": "#EF4444", "dot_y": "#F59E0B", "dot_g": "#10B981",
        "pill_bg": "rgba(37,99,235,0.08)", "pill_border": "rgba(6,182,212,0.28)",
        "noise_opacity": "0.028", "glass_opacity": "0.5", "particle": "#2563EB",
        "scanline": "rgba(37,99,235,0.055)", "icon_fill": "#475569", "prompt": "#2563EB",
    },
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
