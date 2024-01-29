class Diacritics:
    """
    Provides a collection of diacritic characters used in the IDP API.

    This class offers easy access to various Unicode diacritic characters that are
    applied to graphemes during the conversion of English text to English with Diacritics (EwD).
    It simplifies the usage of diacritic symbols by encapsulating their Unicode representations.

    Attributes:
        macron (str): The Unicode character for the macron diacritic (U+0304).
        breve (str): The Unicode character for the breve diacritic (U+0306).
        w_above (str): The Unicode character representing a 'w' symbol above the letter (U+1DF1).
    """

    def __init__(self):
        self.macron = chr(0x000304)
        self.breve = chr(0x000306)
        self.w_above = chr(0x001DF1)
