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
        # Pre process
        #
        word_infos = self.preprocess_text(input_text)

        #
        # Main process
        #

        word_infos_with_phones = self.append_phones(
            word_infos, input_text, accent)
        print('word_infos_with_phones:')
        print(word_infos_with_phones)

        word_infos_with_ewd_words = self.append_ewd_words(
            word_infos_with_phones)
        print('word_infos_with_ewd_words:')
        print(word_infos_with_ewd_words)

        #
        # Post process
        #
        return self.postprocess_text(input_text, word_infos_with_ewd_words)

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

    def append_phones(self,
                      word_infos: list[WordInfo],
                      input_text: str,
                      accent: str):

        phonefied_words = self.phonetics_service.phonefy_text(
            input_text, accent)

        for index in range(len(word_infos)):
            if index < len(phonefied_words):
                word_info = word_infos[index]
                word_info.phones = phonefied_words[index]
            else:
                # Handle the case where phonefied_words is shorter than word_infos
                break

        return word_infos

    # def get_phonemes(self, word, accent):
    #     # Implement phoneme retrieval logic based on the word and accent
    #     return []

    def append_ewd_words(self, word_infos_with_phones: list[WordInfo], accent: str) -> list[WordInfo]:
        word_infos_with_ewd_words: list[WordInfo] = []

        for word_info in word_infos_with_phones:
            word_info.ewd_word = self.get_ewd_word(word_info, accent)

        return word_infos_with_ewd_words

    def get_ewd_word(self, word_info: WordInfo, accent: str) -> str:
        phonemes = self.get_phonemes(word_info.phones, accent)
        phoneme_index = 0
        word_length = len(word_info.en_word)

        for letter_index in range(word_length):
            if word_length >= 2:
                
                 

        return word_info.en_word

    def get_phonemes(self, phones: str, accent: str) -> list[Phoneme]:
        split_phones = phones.split('-')
        phonemes: list[Phoneme] = []

        for phone in split_phones:
            phonemes.append(
                self.phonetics_service.get_phoneme_from_phone(phone, accent))

        return phonemes

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
