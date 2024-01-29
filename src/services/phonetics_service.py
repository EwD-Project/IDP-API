from phonemizer import phonemize  # type: ignore
from phonemizer.separator import Separator  # type: ignore
from enums.enums import LetterType, PhonemeType, VowelLength
from enums.phoneme import Phoneme

from mappings.mappings import phone_comb_to_phoneme_mapping
from singletons.diacritics import Diacritics

_diacritics = Diacritics()


class PhoneticsService:
    """
    Provides phonetic services for text conversion and EwD grapheme determination.

    This service handles the phonetization of text based on specified accents and determines 
    appropriate English with Diacritics (EwD) graphemes based on phone and letter combinations.
    """

    @staticmethod
    def phonetize_text(text: str, accent: str) -> list[str]:
        """
        Converts the given text into a phonetic representation based on the specified accent.

        This method utilizes the phonemizer library to convert text into a list of phonetic transcriptions.

        Args:
            text (str): The text to be phonetized.
            accent (str): The accent to be used for phonetic conversion.

        Returns:
            list[str]: A list of phonetic transcriptions for the text (phonetized text).
        """
        # Map English accent to a language code compatible with phonemizer
        # accent_mapping = {
        #     Accent.AMERICAN: 'en-us',
        #     Accent.BRITISH: 'en-gb'  # example, adjust as needed
        # }

        phonetized_text = str(phonemize(
            text,
            language=accent,
            backend='espeak',
            strip=True,
            preserve_punctuation=False,
            with_stress=True,
            # tie=True,
            separator=Separator(phone='-', syllable='|', word=' ')
        ))

        print('phonetized_text:')
        print(phonetized_text)

        return phonetized_text.split()

    @staticmethod
    def get_phoneme_from_phone_comb(phone_comb: str, accent: str) -> Phoneme:
        """
        Retrieves the corresponding Phoneme for a given phone combination based on the specified accent.

        Args:
            phone_comb (str): The phone combination string.
            accent (str): The specified accent for phoneme retrieval.

        Returns:
            Phoneme: The corresponding Phoneme for the given phone combination.
        """
        # Returns None if the phone comb is not found
        return phone_comb_to_phoneme_mapping['espeak'][accent].get(phone_comb, Phoneme.unimplemented)

    def get_ewd_grapheme(self, letter_comb: str, next_letters: str, phoneme: Phoneme) -> str | None:
        """
        Determines the appropriate English with Diacritics (EwD) grapheme for a given letter comb and phoneme.

        This method considers the current letter comb, the next letters, and the associated phoneme
        to derive the corresponding EwD grapheme.

        Args:
            letter_comb (str): The letter combination from the original text.
            next_letters (str): The subsequent letters following the letter comb.
            phoneme (Phoneme): The phoneme associated with the letter comb.

        Returns:
            str | None: The corresponding EwD grapheme if one can be determined, otherwise None.
        """
        if phoneme.get_type() == PhonemeType.NON_RHOTIC_VOWEL:
            # Treat separately monograph long/short vowels
            if self.is_monograph_vowel(letter_comb):
                if phoneme.is_basic_long_or_short_vowel():
                    return self.get_monograph_with_diacritic(
                        letter_comb, next_letters, phoneme)

            # Treat other non rhotic vowels
            eds_mapping = {
                'a': {
                    Phoneme.short_e: 'a̤',
                    Phoneme.short_i: 'ȧ',
                    Phoneme.ah: 'ä',
                    Phoneme.aw: 'a' if next_letters in ['l', 'll'] else 'a' + _diacritics.w_above  # nopep8
                },
                # TODO
                # 'ai': {}
            }

            # Return EwD grapheme if found, otherwise return letter_comb
            eds_mapping[letter_comb].get(phoneme, letter_comb)

        else:
            return letter_comb

    def get_monograph_with_diacritic(self, monograph_vowel: str, next_letters: str, phoneme: Phoneme) -> str:
        """
        Determines the appropriate diacritic for a monograph vowel based on its phonetic context.

        Args:
            monograph_vowel (str): A single vowel grapheme.
            next_letters (str): The letters following the vowel in the text, up to 2.
            phoneme (Phoneme): The phoneme associated with the vowel.

        Returns:
            str: The vowel grapheme with the appropriate diacritic based on the phoneme.
        """
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

    def get_letter_type(self, letter: str) -> LetterType:
        """
        Determines the type of a given letter; whether it's a vowel or a consonant.

        Args:
            letter (str): The letter to be classified.

        Returns:
            LetterType: The classification of the letter as either a vowel or a consonant.

        Raises:
            ValueError: If the input is not a single character.
        """
        if len(letter) > 1:
            raise ValueError('Expected a single character string.')
        if self.is_monograph_vowel(letter):
            return LetterType.VOWEL
        return LetterType.CONSONANT

    def is_monograph_vowel(self, ewd_grapheme: str) -> bool:
        """
        Checks if a given grapheme is a monograph vowel.

        Args:
            ewd_grapheme (str): The grapheme to be checked.

        Returns:
            bool: True if the grapheme is a monograph vowel, False otherwise.
        """
        if ewd_grapheme in 'aeiyou':
            return True
        return False
