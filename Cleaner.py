import re
import json

input_file = "input.txt"
output_file = "cleaned.txt"

with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()

objects = re.findall(r'\{.*?\}', data)

proxies = []

for obj in objects:
    try:
        parsed = json.loads(obj)
        ip = parsed.get("ip")
        port = parsed.get("port")
        if ip and port:
            proxies.append(f"{ip}:{port}")
    except:
        continue

# duplicates remove
proxies = list(set(proxies))

with open(output_file, "w") as f:
    for proxy in proxies:
        f.write(proxy + "\n")

print(f"Done ✅ {len(proxies)} proxies saved in {output_file}")