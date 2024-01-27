from enum import Enum, auto


class Accent(Enum):
    # currently unused

    AMERICAN = 'en-us'
    BRITISH = 'en-gb'


class LetterType(Enum):
    VOWEL = auto()
    CONSONANT = auto()


class PhonemeType(Enum):
    # TODO
    UNTREATED = auto()

    NON_RHOTIC_VOWEL = auto()
    RHOTIC_VOWEL = auto()
    CONSONANT = auto()


class VowelLength(Enum):
    LONG = auto()
    SHORT = auto()
