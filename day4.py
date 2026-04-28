import json
with open("students.json", "r", encoding="utf8") as fayl:
    data = json.load(fayl)

best = max(data, key=lambda x:x["grade"])

# 3. Eng past baholi talaba
worst = min(data, key=lambda x:x["grade"])

# 4. O'rtacha baho
average =  sum(s["grade"] for s in data) / len(data)

# 5. Natijani chiqarish
print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")