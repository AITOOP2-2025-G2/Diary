from diaries.yumaDiary import yumaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [yumaDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()