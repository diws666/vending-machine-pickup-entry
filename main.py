import os

LINE = "Are you exact change? Because every time you walk by, I light up and forget how to give refunds."  # 96 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
