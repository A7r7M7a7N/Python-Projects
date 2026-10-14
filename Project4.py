# Markdown to HTML Converter
import re

def convert_md_to_html(md_text):
    html = md_text
    
    # Headings
    html = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^# (.*?)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)
    
    # Bold & Italic
    html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.*?)\*", r"<em>\1</em>", html)
    
    # Bullet Lists
    html = re.sub(r"^\* (.*?)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    html = re.sub(r"(<li>.*?</li>)", r"<ul>\1</ul>", html, flags=re.DOTALL)
    
    return f"<!DOCTYPE html>\n<html>\n<body>\n{html}\n</body>\n</html>"