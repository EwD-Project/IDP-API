from dataclasses import dataclass


@dataclass
class WordInfo:
    en_word: str
    phones: str
    ewd_word: str
    case: str
    start_pos: int
    end_pos: int
