from diaries.DiarySample import DiarySample
from diaries.Diaryebi import Diaryebi
from diaries.JumpeiDiary import JumpeiDiary
from diaries.kurotsukaDiary import kurotsukaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           JumpeiDiary(),
           Diaryebi(),
        kurotsukaDiary(),
           ] 




for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
