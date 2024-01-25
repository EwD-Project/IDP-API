# IDP API Conversion Steps

Legend:
  - SE: Standard English
  - SEGPM: SE Grapheme—Phoneme Mapping
  - EDS: English Diacritical System
  - EwD: English with Diacritics

## Steps

1. Preprocessing

    1.1. For each word of the text, get the following infos:
    
    - Position in the text.
      > This info will be used in Step 3.1.
    
    - Word case.
      > This info will be also used in Step 3.1.
    
    - English phonemes for the selected accent.
      > This info will be used in Step 2.2.
      > The accent info comes as endpoint parameter.
      
    1.2. Return the relation of words and their respective infos.

2. EDS Processing

    2.1. For each word in the relation, compare the graphemes with the phonemes to establish the SEGPMs.

    2.2. For each SEGPM of each word, apply the EDS logic to return the corresponding EwD grapheme of each SE grapheme.
    
    2.3. Append the “EwD word” info to each word in the relation.

    2.4. Return the updated relation of words and their respective infos.

3. Postprocessing

    3.1. Put each converted word back in the original text with its original case.
    
    3.2. Return the result text.