import re
import pandas as pd
from pathlib import Path

log_path = r"C:\\Path\\To\\Your\\log file.log"  # Change this
log_file = Path(log_path)

text = log_file.read_text(encoding="utf-8", errors="ignore")

# Grab blocks from the console dump
blocks = re.findall(r"\{.*?\}", text, re.DOTALL)

def get_val(key, block):
    # handle commas inside the value
    m = re.search(rf"{key}\s*:\s*'(.*?)'", block, re.IGNORECASE | re.DOTALL)
    if not m:
        m = re.search(rf'{key}\s*:\s*"(.*?)"', block, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip()

    # Capture until next brace or line end (allow commas)
    m = re.search(rf"{key}\s*:\s*([^\n}}]+)", block, re.IGNORECASE)
    if m:
        return m.group(1).strip().strip("'\"")
    return ""

rows = []
for block in blocks:
    pid   = get_val("pageId", block)
    vid   = get_val("name", block)    
    vtyp  = get_val("type", block)
    vttl  = get_val("title", block)

    if pid and vid and vtyp:
        rows.append({
            "Page ID": pid.strip("'\""),
            "Visual ID": vid.strip("'\""),
            "Visual Type": vtyp.strip("'\""),
            "Visual Title": vttl.strip("'\""),
        })

df = pd.DataFrame(rows)
if not df.empty:
    df = df.sort_values(["Page ID", "Visual ID"]).reset_index(drop=True)

out_xlsx = log_file.with_name("visuals_extracted.xlsx")
df.to_excel(out_xlsx, index=False, engine="openpyxl")