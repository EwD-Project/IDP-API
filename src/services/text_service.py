import re
from enums.phoneme import Phoneme

from models.word_info import WordInfo
from services.phonetics_service import PhoneticsService


class TextService:
    """
    Provides services for converting English text to English with Diacritics (EwD).

    This service is responsible for the conversion process which includes preprocessing the input text, 
    appending phonetic and EwD representations to words, and reconstructing the text with converted words.
    """

    def __init__(self):
        """
        Initializes the TextService with a PhoneticsService instance and a word pattern.
        """
        self.phonetics_service = PhoneticsService()
        self.word_pattern = r'\b\w+\b'

    def convert_en_to_ewd(self, input_text: str, accent: str) -> str:
        """
        Converts Standard English text to English with Diacritics (EwD) format.

        The method includes preprocessing of the text, appending phonetic representations, converting to EwD, 
        and postprocessing to reconstruct the final text.

        Args:
            input_text (str): The original English text to be converted.
            accent (str): The accent to use for phonetic conversion.

        Returns:
            str: The converted text in EwD format.
        """
        #
        # Preprocess
        #
        word_infos = self.preprocess_text(input_text)

        #
        # Main Process
        #

        word_infos_with_phone_combs = self.append_phone_combs(
            word_infos, input_text, accent)
        print('word_infos_with_phone_combs:')
        print(word_infos_with_phone_combs)

        word_infos_with_ewd_words = self.append_ewd_words(
            word_infos_with_phone_combs, accent)
        print('word_infos_with_ewd_words:')
        print(word_infos_with_ewd_words)

        #
        # Postprocess
        #
        return self.postprocess_text(input_text, word_infos_with_ewd_words)

    #
    # Preprocess
    #

    def preprocess_text(self, input_text: str) -> list[WordInfo]:
        """
        Extracts words from the input text and creates a list of WordInfo objects.

        Each WordInfo object contains the extracted word, its position in the text, and its case. 
        This method represents the preprocessing step in the conversion process.

        Args:
            input_text (str): The text to be processed for word extraction.

        Returns:
            list[WordInfo]: A list of WordInfo objects representing the extracted words.
        """
        word_infos: list[WordInfo] = []

        # Finding words, their positions, and cases
        for match in re.finditer(self.word_pattern, input_text):
            word = match.group()
            word_info = WordInfo(
                en_word=word,
                phone_combs='',
                ewd_word='',
                case='upper' if word.isupper() else 'lower' if word.islower(
                ) else 'title' if word.istitle() else 'mixed',
                start_pos=match.start(),
                end_pos=match.end()
            )
            word_infos.append(word_info)

        return word_infos

    #
    # Main Process
    #

    def append_phone_combs(self, word_infos: list[WordInfo], input_text: str, accent: str) -> list[WordInfo]:
        """
        Appends phonetic representations (phone combs) to each word in the given list of WordInfo objects.

        This method retrieves the phonetic representation of the entire input text and then
        associates each phone sequence with the corresponding word in the word_infos list.

        Args:
            word_infos (list[WordInfo]): A list of WordInfo objects containing words from the input text.
            input_text (str): The original text from which the words were extracted.
            accent (str): The accent to use for phonetic conversion.

        Returns:
            list[WordInfo]: The list of WordInfo objects with appended phonetic representations.

        Raises:
            ValueError: If the number of words in the input text does not match the number of phonetic representations returned.
        """

        phonetized_words = self.phonetics_service.phonetize_text(
            input_text, accent)

        if len(phonetized_words) != len(word_infos):
            raise ValueError(
                "Mismatch in word and phonetic representation counts.")

        for index, phone_comb in enumerate(phonetized_words):
            word_infos[index].phone_combs = phone_comb

        return word_infos

    def append_ewd_words(self, word_infos_with_phone_combs: list[WordInfo], accent: str) -> list[WordInfo]:
        """
        Appends English with Diacritics (EwD) representation to each WordInfo object.

        This method processes each WordInfo object to convert English words to EwD format based on their phonetic representations.

        Args:
            word_infos_with_phone_combs (list[WordInfo]): A list of WordInfo objects with appended phonetic representations.
            accent (str): The accent to be considered for conversion.

        Returns:
            list[WordInfo]: The list of WordInfo objects with appended EwD representations.
        """
        word_infos_with_ewd_words: list[WordInfo] = []

        for word_info in word_infos_with_phone_combs:
            word_info.ewd_word = self.get_ewd_word(word_info, accent)

        return word_infos_with_ewd_words

    def get_ewd_word(self, word_info: WordInfo, accent: str) -> str:
        """
        Generates an EwD representation of a word based on its phonetic representation.

        This method iteratively processes each grapheme-phoneme pair within a word to generate the corresponding EwD representation.

        Args:
            word_info (WordInfo): The WordInfo object containing the English word and its phonetic representation.
            accent (str): The accent to be used for determining phonetic characteristics.

        Returns:
            str: The EwD representation of the word.
        """
        word = word_info.en_word
        edw_graphemes: list[str] = []
        phonemes = self.get_phonemes(word_info.phone_combs, accent)
        print(f"'{word_info.en_word}' phonemes:")
        print(phonemes)

        letter_index = 0
        phoneme_index = 0
        while letter_index < len(word) and phoneme_index < len(phonemes):
            remaining_letters = word[letter_index:]
            phoneme = phonemes[phoneme_index]

            # Get max letter comb size up to 3
            max_letter_comb_size: int
            if len(remaining_letters) > 3:
                max_letter_comb_size = 3
            else:
                max_letter_comb_size = len(remaining_letters)

            # Iterate letter combs reversely
            for letter_comb_length in range(max_letter_comb_size, -1, -1):
                # Get letter comb
                letter_comb = remaining_letters[letter_index:letter_index+letter_comb_length]  # nopep8
                print(f'letter_comb: {letter_comb}')

                # Get next 2, 1 or 0 letters
                next_letters_after_comb = remaining_letters[max_letter_comb_size:]
                next_letters_size: int
                if len(next_letters_after_comb) > 2:
                    next_letters_size = 2
                else:
                    next_letters_size = len(next_letters_after_comb)
                next_letters = next_letters_after_comb[0:next_letters_size]
                print(f'next_letters: {next_letters}')

                # Get and append EwD grapheme if found one
                ewd_grapheme = self.phonetics_service.get_ewd_grapheme(
                    letter_comb,
                    next_letters,
                    phoneme
                )
                if ewd_grapheme:
                    edw_graphemes.append(ewd_grapheme)
                    letter_index += len(letter_comb)
                    phoneme_index += 1
                    break
                else:
                    # If no EwD grapheme is to be found, append original letter
                    if letter_comb_length == 1:
                        edw_graphemes.append(letter_comb)
                        letter_index += 1
                        phoneme_index += 1
                        break

        return word_info.en_word

    def get_phonemes(self, phone_combs: str, accent: str) -> list[Phoneme]:
        """
        Converts a string of phonetic representations (phone combinations) into a list of Phoneme objects.

        This method splits a string of phone combinations and maps each to its corresponding Phoneme based on the provided accent.

        Args:
            phone_combs (str): A string of phone combinations separated by dashes.
            accent (str): The accent to be used for phoneme mapping.

        Returns:
            list[Phoneme]: A list of Phoneme objects corresponding to the provided phone combs and accent.
        """
        split_phone_combs = phone_combs.split('-')
        phonemes: list[Phoneme] = []

        for phone_comb in split_phone_combs:
            phonemes.append(
                self.phonetics_service.get_phoneme_from_phone_comb(phone_comb, accent))

        return phonemes

    #
    # Postprocess
    #

    def postprocess_text(self, input_text: str, word_infos: list[WordInfo]):
        """
        Reconstructs the original text with converted EwD words.

        This method replaces each word in the original text with its EwD representation, maintaining the original word's position and case.

        Args:
            input_text (str): The original text to be processed.
            word_infos (list[WordInfo]): A list of WordInfo objects containing EwD representations of words.

        Returns:
            str: The reconstructed text with EwD words.
        """
        result_text = input_text
        offset: int = 0

        for word_info in word_infos:
            ewd_word = word_info.ewd_word
            start_pos = word_info.start_pos + offset
            end_pos = word_info.end_pos + offset

            # Adjust case
            if word_info.case == 'upper':
                ewd_word = ewd_word.upper()
            elif word_info.case == 'lower':
                ewd_word = ewd_word.lower()
            elif word_info.case == 'title':
                ewd_word = ewd_word.title()

            result_text = result_text[:start_pos] + \
                ewd_word + result_text[end_pos:]
            offset += len(ewd_word) - (end_pos - start_pos)

        return result_text
