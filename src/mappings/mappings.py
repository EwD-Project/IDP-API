"""
This module contains mappings used in the IDP API for converting phonetic representations (phone combinations)
to their corresponding phonemes. These mappings are specific to different accents and the phonetization backend used.
"""
from enums.phoneme import Phoneme

# Mappings from phone combinations to Phonemes for various accents and potential backends.
# Currently, the only mapping provided is for the espeak backend, but the object can be extended to include others.
phone_comb_to_phoneme_mapping = {
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
            'ɑ': Phoneme.short_o,
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

            # TODO: From here below, pending.

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
