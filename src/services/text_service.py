from ast import Dict
import re
from typing import List, SupportsIndex, Union

from services.phonetics_service import PhoneticsService


class TextService:
    def __init__(self):
        self.phonetics_service = PhoneticsService()
        self.word_pattern = r'\b\w+\b'

    def convert_text(self, input_text, accent):
        word_infos = self.preprocess_text(input_text, accent)
        word_infos = self.append_phones_to_word_infos(word_infos, input_text)
        word_infos = self.eds_process(word_infos)
        return self.postprocess_text(
            input_text, word_infos)

    def preprocess_text(self, input_text, accent='en-us'):
        word_infos = []

        # Finding words, their positions, and cases
        for match in re.finditer(self.word_pattern, input_text):
            word = match.group()
            word_info = {
                'word': word,
                'start_pos': match.start(),
                'end_pos': match.end(),
                'case': 'upper' if word.isupper() else 'lower' if word.islower() else 'title' if word.istitle() else 'mixed',
            }
            word_infos.append(word_info)

        return word_infos

    def append_phones_to_word_infos(self, word_infos, input_text, accent='en-us'):
        phonefied_words = self.phonetics_service.phonefy_text(
            input_text, accent)

        for index in range(len(word_infos)):  # type: ignore
            if index < len(phonefied_words):
                word_infos[index]['phones'] = phonefied_words[index]  # type: ignore # nopep8
            else:
                # Handle the case where phonefied_words is shorter than word_infos
                break

        return word_infos

    def get_phonemes(self, word, accent):
        # Implement phoneme retrieval logic based on the word and accent
        return []

    def eds_process(self, words_and_infos):
        updated_words_and_infos = []

        for word_info in words_and_infos:
            # Logic to apply EDS and get EwD grapheme
            # Function to apply EDS, to be implemented
            ewd_grapheme = self.apply_eds_to_word(
                word_info['word'], word_info['phonemes'])
            word_info['ewd_word'] = ewd_grapheme
            updated_words_and_infos.append(word_info)

        return updated_words_and_infos

    def apply_eds_to_word(self, word, phonemes):
        # TODO: Implement EDS logic to convert word to EwD based on phonemes
        return word

    def postprocess_text(self, input_text, words_and_infos):
        result_text = input_text
        offset = 0

        for word_info in words_and_infos:
            ewd_word = word_info['ewd_word']
            start_pos = word_info['start_pos'] + offset
            end_pos = word_info['end_pos'] + offset

            # Adjust case
            if word_info['case'] == 'upper':
                ewd_word = ewd_word.upper()
            elif word_info['case'] == 'lower':
                ewd_word = ewd_word.lower()
            elif word_info['case'] == 'title':
                ewd_word = ewd_word.title()

            result_text = result_text[:start_pos] + \
                ewd_word + result_text[end_pos:]
            offset += len(ewd_word) - (end_pos - start_pos)

        return result_text
