
from enums.phoneme import Phoneme

from phonemizer import phonemize  # type: ignore
from phonemizer.separator import Separator  # type: ignore


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
    def get_phoneme_from_phone(phone: str, accent: str):
        """
        Maps a phone string to a Phoneme based on the specified Accent.

        Args:
        phone (str): The phone string.
        accent (str): The specified accent.

        Returns:
        Phoneme: The corresponding phoneme.
        """

        # Example mapping logic
        mapping = {
            'espeak': {
                'en-us': {
                    # Paired Vowels
                    'e͡ɪ': Phoneme.long_a,
                    'æ': Phoneme.short_a,
                    'iː': Phoneme.long_e,
                    'ɛ': Phoneme.short_e,
                    'a͡ɪ': Phoneme.long_i,
                    'ɪ': Phoneme.short_i,
                    'ᵻ': Phoneme.short_i,
                    'o͡ʊ': Phoneme.long_o,
                    'ɑː': Phoneme.short_o,
                    'juː': Phoneme.long_u,
                    'ʌ': Phoneme.short_u,
                    'uː': Phoneme.long_oo,
                    'ʊ': Phoneme.short_oo,

                    # Unpaired Vowels
                    'ɑː': Phoneme.ah,
                    'ɔ͡ɪ': Phoneme.oy,
                    'ɔː': Phoneme.aw,
                    'a͡ʊ': Phoneme.ow,
                    'ɐ': Phoneme.schwa,
                    'ə': Phoneme.schwa,

                    # TODO: from here below, pending

                    # Rhotic Vowels
                    # 'ɑː͡ɹ': Phone

                    # Consonants
                    # 'd': Phoneme.d,
                    # 'f': Phoneme.f,
                    # 'g': Phoneme.g,
                    # 'h': Phoneme.h,
                    # 'k': Phoneme.k,
                    # 'l': Phoneme.l,
                    # 'm': Phoneme.m,
                    # 'n': Phoneme.n,
                    # 'ŋ': Phoneme.ng,
                    # 'p': Phoneme.p,
                    # 'r': Phoneme.r,
                    # 'ɚr': Phoneme.r_schwa,
                    # 'ɚ': Phoneme.r_schwa,
                    # 't͡ʃ': Phoneme.ch,
                    # 'θ': Phoneme.unvoiced_th,
                    # 'v': Phoneme.v,
                    # 'w': Phoneme.w,
                },
                'en-gb': {
                    # unimplemented
                }
            }
        }

        # Returns None if the phone is not found
        return mapping['espeak'][accent].get(phone, None)
