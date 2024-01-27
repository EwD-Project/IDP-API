import re
from enums.phoneme import Phoneme

from models.word_info import WordInfo
from services.phonetics_service import PhoneticsService


class TextService:
    def __init__(self):
        self.phonetics_service = PhoneticsService()
        self.word_pattern = r'\b\w+\b'

    def convert_en_to_ewd(self, input_text: str, accent: str):
        #
        # Preprocess
        #
        word_infos = self.preprocess_text(input_text)

        #
        # Main Process
        #

        word_infos_with_phones = self.append_phones(
            word_infos, input_text, accent)
        print('word_infos_with_phones:')
        print(word_infos_with_phones)

        word_infos_with_ewd_words = self.append_ewd_words(
            word_infos_with_phones, accent)
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
        word_infos: list[WordInfo] = []

        # Finding words, their positions, and cases
        for match in re.finditer(self.word_pattern, input_text):
            word = match.group()
            word_info = WordInfo(
                en_word=word,
                phones='',
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

    def append_phones(self, word_infos: list[WordInfo], input_text: str, accent: str) -> list[WordInfo]:
        """
        Appends phonetic representations (phones) to each word in the given list of WordInfo objects.

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

        phonefied_words = self.phonetics_service.phonefy_text(
            input_text, accent)

        if len(phonefied_words) != len(word_infos):
            raise ValueError(
                "Mismatch in word and phonetic representation counts.")

        for index, phone in enumerate(phonefied_words):
            word_infos[index].phones = phone

        return word_infos

    def append_ewd_words(self, word_infos_with_phones: list[WordInfo], accent: str) -> list[WordInfo]:
        word_infos_with_ewd_words: list[WordInfo] = []

        for word_info in word_infos_with_phones:
            word_info.ewd_word = self.get_ewd_word(word_info, accent)

        return word_infos_with_ewd_words

    def get_ewd_word(self, word_info: WordInfo, accent: str) -> str:
        word = word_info.en_word
        edw_graphemes: list[str] = []
        phonemes = self.get_phonemes(word_info.phones, accent)
        print(f"'{word_info.en_word}' phonemes:")
        print(phonemes)

        letter_index = 0
        phoneme_index = 0
        while letter_index < len(word) and phoneme_index < len(phonemes):
            remaining_letters = word[letter_index:]
            phoneme = phonemes[phoneme_index]

            # Get max letter group size up to 3
            max_letter_group_size: int
            if len(remaining_letters) > 3:
                max_letter_group_size = 3
            else:
                max_letter_group_size = len(remaining_letters)

            # Iterate letter groups reversely
            for letter_group_length in range(max_letter_group_size, -1, -1):
                # Get letter group
                letter_group = remaining_letters[letter_index:letter_index+letter_group_length]  # nopep8
                print(f'letter_group: {letter_group}')

                # Get next 2, 1 or 0 letters
                next_letters_after_group = remaining_letters[max_letter_group_size:]
                next_letters_size: int
                if len(next_letters_after_group) > 2:
                    next_letters_size = 2
                else:
                    next_letters_size = len(next_letters_after_group)
                next_letters = next_letters_after_group[0:next_letters_size]
                print(f'next_letters: {next_letters}')

                # TODO: Get and append EwD grapheme if found one
                ewd_grapheme = self.phonetics_service.get_ewd_grapheme(
                    letter_group,
                    next_letters,
                    phoneme
                )
                if (ewd_grapheme):
                    edw_graphemes.append(ewd_grapheme)
                    letter_index += len(letter_group)
                    phoneme_index += 1
                    break
                else:
                    # If no EwD grapheme is to be found, append original letter
                    if letter_group_length == 1:
                        edw_graphemes.append(letter_group)
                        letter_index += 1
                        phoneme_index += 1
                        break

        return word_info.en_word

    def get_phonemes(self, phones: str, accent: str) -> list[Phoneme]:
        split_phones = phones.split('-')
        phonemes: list[Phoneme] = []

        for phone in split_phones:
            phonemes.append(
                self.phonetics_service.get_phoneme_from_phone(phone, accent))

        return phonemes

    #
    # Postprocess
    #

    def postprocess_text(self, input_text: str, word_infos: list[WordInfo]):
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
