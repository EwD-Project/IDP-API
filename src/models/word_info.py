from dataclasses import dataclass


@dataclass
class WordInfo:
    """
    Represents the necessary information about a word during the text conversion process.

    This class encapsulates details about a word extracted from the input text, including its
    original form, phonetic representation, converted form with diacritics, and positional
    information within the text.

    Attributes:
        en_word (str): The original English word.
        phone_combs (str): The phonetic representation (phone combinations) of the word.
        ewd_word (str): The word converted into English with Diacritics (EwD).
        case (str): The original case of the word (e.g., 'upper', 'lower', 'title', 'mixed').
        start_pos (int): The starting position of the word in the original text.
        end_pos (int): The ending position of the word in the original text.
    """
    en_word: str
    phone_combs: str
    ewd_word: str
    case: str
    start_pos: int
    end_pos: int
