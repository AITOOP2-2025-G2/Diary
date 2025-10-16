from diaries.AbstractDiary import AbstractDiary

class JumpeiDiary(AbstractDiary):
    
    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "ブランチの仕組みを理解するのに時間がかかった"
    
    def get_author(self):
        return "jumpei28"