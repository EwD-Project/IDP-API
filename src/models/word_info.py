from dataclasses import dataclass


@dataclass
class WordInfo:
    en_word: str
    phones: str
    ewd_word: str
    case: str
    start_pos: int
    end_pos: int

# class WordInfo:

#     def __init__(self, en_word: str, phones: str, ewd_word: str, case: str, start_pos: int, end_pos: int):
#         self.en_word = en_word
#         self.phones = phones
#         self.ewd_word = ewd_word
#         self.case = case
#         self.start_pos = start_pos
#         self.end_pos = end_pos

#     def __str__(self):
#         return (f"WordInfo(en_word='{self.en_word}', "
#                 f"phones='{self.phones}', "
#                 f"ewd_word='{self.ewd_word}', "
#                 f"case='{self.case}', "
#                 f"start_pos={self.start_pos}, "
#                 f"end_pos={self.end_pos})")

#     def __repr__(self):
#         return self.__str__()
