# pylint: disable=invalid-name

from enum import Enum, auto

from enums.enums import PhonemeType, VowelLength


class Phoneme(Enum):
    """
    Enum representing various phonemes in English language phonetics.

    This class also categorizes phonemes into different types such as vowels, consonants, and their specific subtypes.
    """
    # TODO: Implement.
    unimplemented = auto()

    # Non-Rhotic Vowels
    long_a = auto()
    short_a = auto()
    long_e = auto()
    short_e = auto()
    long_i = auto()
    short_i = auto()
    long_o = auto()
    short_o = auto()
    long_u = auto()
    short_u = auto()
    long_oo = auto()
    short_oo = auto()
    ah = auto()
    oy = auto()
    aw = auto()
    ow = auto()
    schwa = auto()

    # Rhotic Vowels
    rhotic_a = auto()
    rhotic_ah = auto()
    rhotic_e = auto()
    rhotic_i = auto()
    rhotic_o = auto()
    rhotic_u = auto()
    rhotic_stressed_neutral = auto()
    rhotic_oo = auto()
    rhotic_aw = auto()
    rhotic_ow = auto()
    rhotic_schwa = auto()

    # Paired Consonants
    p = auto()
    b = auto()
    t = auto()
    d = auto()
    unvoiced_th = auto()
    voiced_th = auto()
    ch = auto()
    j = auto()
    k = auto()
    g = auto()
    qu = auto()
    gu = auto()
    unvoiced_x = auto()
    voiced_x = auto()
    f = auto()
    v = auto()
    s = auto()
    z = auto()
    sh = auto()
    zh = auto()

    # Unpaired Consonants
    h = auto()
    l = auto()
    r = auto()
    m = auto()
    n = auto()
    ng = auto()
    w = auto()
    wh = auto()
    y = auto()

    def get_type(self) -> PhonemeType:
        """
        Determines the type of the phoneme.

        Returns:
            PhonemeType: The type of the phoneme based on its classification.
        """
        if self.is_basic_long_or_short_vowel():
            return PhonemeType.NON_RHOTIC_VOWEL
        if self in [Phoneme.long_oo, Phoneme.short_oo, Phoneme.ah, Phoneme.oy, Phoneme.aw, Phoneme.ow]:
            return PhonemeType.NON_RHOTIC_VOWEL
        # TODO: Treat.
        return PhonemeType.UNTREATED

    def is_basic_long_or_short_vowel(self) -> bool:
        """
        Checks if the phoneme is a basic long or short vowel.

        Returns:
            bool: True if the phoneme is a basic long or short vowel, False otherwise.
        """
        if self in [Phoneme.long_a, Phoneme.long_e, Phoneme.long_i, Phoneme.long_o, Phoneme.long_u]:
            return True
        if self in [Phoneme.short_a, Phoneme.short_e, Phoneme.short_i, Phoneme.short_o, Phoneme.short_u]:
            return True
        return False

    def get_non_rhotic_vowel_length(self) -> VowelLength:
        """
        Determines the length of a non-rhotic vowel.

        Returns:
            VowelLength: The length of the vowel (LONG or SHORT).

        Raises:
            ValueError: If the phoneme is not a non-rhotic long/short vowel.
        """
        if self in [Phoneme.long_a, Phoneme.long_e, Phoneme.long_i, Phoneme.long_o, Phoneme.long_u, Phoneme.long_oo]:
            return VowelLength.LONG
        if self in [Phoneme.short_a, Phoneme.short_e, Phoneme.short_i, Phoneme.short_o, Phoneme.short_u, Phoneme.short_oo]:
            return VowelLength.SHORT
        raise ValueError('Expected a non-rhotic long/short vowel.')
