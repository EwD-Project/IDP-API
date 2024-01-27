
from phonemizer import phonemize  # type: ignore
from phonemizer.separator import Separator
from enums.letter_type import LetterType
from enums.phoneme import Phoneme
from enums.vowel_naturality import VowelNaturality  # type: ignore

from mappings.mappings import phone_to_phoneme_mapping


class PhoneticsService:
    @staticmethod  # type: ignore
    def phonefy_text(text: str, accent: str):
        """
        Uses the phonemizer library to get the phones of a text.

        Args:
        text (str): The input text.
        accent (EnglishAccent): The specified English accent.

        Returns:
        str: The phonefied text.
        """

        # Map English accent to a language code compatible with phonemizer
        # accent_mapping = {
        #     Accent.AMERICAN: 'en-us',
        #     Accent.BRITISH: 'en-gb'  # example, adjust as needed
        # }

        # Phonemize the text
        phonefied_text = str(phonemize(
            text,
            language=accent,
            backend='espeak',
            strip=True,
            preserve_punctuation=False,
            with_stress=True,
            # tie=True,
            separator=Separator(phone='-', syllable='|', word=' ')
        ))

        print('phonefied_text:')
        print(phonefied_text)

        return phonefied_text.split()

    @staticmethod  # type: ignore
    def get_phoneme_from_phone(phone: str, accent: str) -> Phoneme:
        """
        Maps a phone string to a Phoneme based on the specified Accent.

        Args:
        phone (str): The phone string.
        accent (str): The specified accent.

        Returns:
        Phoneme: The corresponding phoneme.
        """

        # Example mapping logic

        # Returns None if the phone is not found
        return phone_to_phoneme_mapping['espeak'][accent].get(phone, Phoneme.unimplemented)
    

    def get_ewd_grapheme_from_en_grapheme(self, ewd_grapheme: str, next_letters: str) -> str:
        mapping = {}

        if self.is_monograph_vowel(ewd_grapheme):
            nat = self.get_vowel_naturality(ewd_grapheme, next_letters)

            mapping = {
                'en-us': {
                    'a': {
                        Phoneme.long_a: 'a' if nat == N else 'ā', 
                    }
                },
                'en-gb': {
                    # unimplemented
                }
        }
            
    def get_vowel_with_diacritic(self, monograph_vowel: str, next_letters: str, phoneme: Phoneme) -> str:
        if len(next_letters) == 1:
            next_letter_type = self.get_letter_type(next_letters[0])
            if next_letter_type == LetterType.CONSONANT:
                return monograph_vowel + chr(304)
        if len(next_letters) == 2:
            next_letter_type_1 = self.get_letter_type(next_letters[0])
            next_letter_type_2 = self.get_letter_type(next_letters[1])
            if next_letter_type_1 == next_letter_type_2 == LetterType.CONSONANT:
                return monograph_vowel + 


    def is_monograph_vowel(self, ewd_grapheme: str) -> bool:
        if ewd_grapheme in ['a', 'e', 'i', 'y', 'o', 'u']:
            return True
        return False


    def get_letter_type(self, letter: str) -> LetterType:
        if letter in ['a', 'e', 'i', 'y' 'o', 'u']:
            return LetterType.VOWEL
        return LetterType.CONSONANT

