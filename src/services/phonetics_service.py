
from phonemizer import phonemize  # type: ignore
from phonemizer.separator import Separator  # type: ignore
from enums.enums import LetterType, PhonemeType, VowelLength
from enums.phoneme import Phoneme

from mappings.mappings import phone_to_phoneme_mapping
from singletons.diacritics import Diacritics

_diacritics = Diacritics()


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

    def get_ewd_grapheme(self, letter_group: str, next_letters: str, phoneme: Phoneme) -> str | None:
        if phoneme.get_type() == PhonemeType.NON_RHOTIC_VOWEL:
            # Treat separately monograph long/short vowels
            if self.is_monograph_vowel(letter_group):
                if phoneme.is_basic_long_or_short_vowel():
                    return self.get_monograph_with_diacritic(
                        letter_group, next_letters, phoneme)

            # Treat other non rhotic vowels
            eds_mapping = {
                'a': {
                    Phoneme.short_e: 'a̤',
                    Phoneme.short_i: 'ȧ',
                    Phoneme.ah: 'ä',
                    Phoneme.short_e: 'a̤',
                    Phoneme.aw: 'a' if next_letters in ['l', 'll'] else 'a' + _diacritics.w_above  # nopep8
                },
                # TODO
                # 'ai': {}
            }

            # Return EwD grapheme if found, otherwise return letter_group
            eds_mapping[letter_group].get(phoneme, letter_group)

        else:
            return letter_group

    def get_monograph_with_diacritic(self, monograph_vowel: str, next_letters: str, phoneme: Phoneme) -> str:
        if phoneme.get_non_rhotic_vowel_length() == VowelLength.LONG:
            if len(next_letters) == 0:
                # Don't append diacritic to natural short vowel at final position except for "a" and "e"
                if monograph_vowel in ['a', 'e']:
                    return monograph_vowel + _diacritics.macron
                return monograph_vowel
            if len(next_letters) == 1:
                # Append Macron to non-natural long vowel
                next_letter_type = self.get_letter_type(next_letters[0])
                if next_letter_type == LetterType.CONSONANT:
                    return monograph_vowel + _diacritics.macron
            if len(next_letters) == 2:
                next_letter_type_1 = self.get_letter_type(next_letters[0])
                next_letter_type_2 = self.get_letter_type(next_letters[1])
                # Append Macron to non-natural long vowel
                if next_letter_type_1 == next_letter_type_2 == LetterType.CONSONANT:
                    return monograph_vowel + _diacritics.macron

        if phoneme.get_non_rhotic_vowel_length() == VowelLength.SHORT:
            if len(next_letters) == 0:
                # Append Breve to non-natural short vowel at final position (which is antinatural in English)
                return monograph_vowel + _diacritics.breve
            if len(next_letters) == 1:
                # Don't append Breve to natural short vowel
                next_letter_type = self.get_letter_type(next_letters[0])
                if next_letter_type == LetterType.CONSONANT:
                    pass
            if len(next_letters) == 2:
                next_letter_type_1 = self.get_letter_type(next_letters[0])
                next_letter_type_2 = self.get_letter_type(next_letters[1])
                # Append Breve to non-natural short vowel
                if next_letter_type_1 == LetterType.CONSONANT and next_letter_type_2 == LetterType.VOWEL:
                    return monograph_vowel + _diacritics.breve

        return monograph_vowel

    def is_monograph_vowel(self, ewd_grapheme: str) -> bool:
        if ewd_grapheme in ['a', 'e', 'i', 'y', 'o', 'u']:
            return True
        return False

    def get_letter_type(self, letter: str) -> LetterType:
        if letter in ['a', 'e', 'i', 'y' 'o', 'u']:
            return LetterType.VOWEL
        return LetterType.CONSONANT
