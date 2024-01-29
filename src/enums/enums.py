"""
Defines various enums used throughout the IDP API for representing different linguistic and phonetic concepts.
These enums facilitate the categorization and handling of accents, letter types, phoneme types, and vowel lengths.
"""

from enum import Enum, auto


class Accent(Enum):
    """
    [Currently unused]

    Enum for representing different accents in English.

    The accents are currently represented as language codes compatible with phonemizer.
    """
    AMERICAN = 'en-us'
    BRITISH = 'en-gb'


class LetterType(Enum):
    """
    Enum for distinguishing between vowels and consonants in a text.

    This classification aids in the phonetic and diacritic processing of letters.
    """
    VOWEL = auto()
    CONSONANT = auto()


class PhonemeType(Enum):
    """
    Enum for representing different types of phonemes in English.

    This classification helps in determining how to process and convert phonemes to diacritics.
    """
    # Placeholder for phonemes that are NOT YET treated.
    # TODO: Treat them.
    UNTREATED = auto()

    NON_RHOTIC_VOWEL = auto()
    RHOTIC_VOWEL = auto()
    CONSONANT = auto()


class VowelLength(Enum):
    """
    Enum for representing the length of vowel sounds.

    This distinction is crucial for determining the correct diacritics in the conversion process.
    """
    LONG = auto()
    SHORT = auto()
