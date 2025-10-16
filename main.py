from diaries.DiarySample import DiarySample
from diaries.JumpeiDiary import JumpeiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), JumpeiDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()