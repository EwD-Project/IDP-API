import requests


def test_get_phonetized_text_american_accent():
    url = 'http://localhost:5000/api/v1/get-phonetized-text'
    input_text = "Last night, at the local diner, Emily ordered a delicious steak and a glass of red wine. Her friend, Michael, chose a light salad and a sparkling water. They talked about their recent trip to California, the sunny beaches they visited, and the interesting people they met. Emily shared stories from her work at the hospital, and Michael discussed his new project in architecture. After dinner, they decided to watch an old movie at the theater nearby. It was a wonderful way to spend a Friday evening."
    data = {'text': input_text, 'accent': 'en-us'}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    phonetized_text = 'lˈæst nˈa͡ɪt æt ðə lˈo͡ʊkə͡l dˈa͡ɪnɚɹ ˈɛmᵻli ˈɔː͡ɹdɚd ɐ dᵻlˈɪʃəs stˈe͡ɪk ænd ɐ ɡlˈæs ʌv ɹˈɛd wˈa͡ɪn hɜː fɹˈɛnd mˈa͡ɪkə͡l t͡ʃˈo͡ʊz ɐ lˈa͡ɪt sˈæləd ænd ɐ spˈɑː͡ɹklɪŋ wˈɔːɾɚ ðe͡ɪ tˈɔːkt ɐbˌa͡ʊt ðɛ͡ɹ ɹˈiːsənt tɹˈɪp tə kˌælɪfˈoː͡ɹni͡ə ðə sˈʌni bˈiːt͡ʃᵻz ðe͡ɪ vˈɪzɪɾᵻd ænd ðɪ ˈɪntɹɛstɪŋ pˈiːpə͡l ðe͡ɪ mˈɛt ˈɛmᵻli ʃˈɛ͡ɹd stˈoːɹiz fɹʌm hɜː wˈɜːk æt ðə hˈɑːspɪɾə͡l ænd mˈa͡ɪkə͡l dɪskˈʌst hɪz nˈuː pɹˈɑːd͡ʒɛkt ɪn ˈɑː͡ɹkɪtˌɛkt͡ʃɚɹ ˈæftɚ dˈɪnɚ ðe͡ɪ dᵻsˈa͡ɪdᵻd tə wˈɑːt͡ʃ ɐn ˈo͡ʊld mˈuːvi æt ðə θˈi͡əɾɚ nˈɪ͡ɹba͡ɪ ɪt wʌzɐ wˈʌndɚfə͡l wˈe͡ɪ tə spˈɛnd ɐ fɹˈa͡ɪde͡ɪ ˈiːvnɪŋ'
    assert phonetized_text in response.json(
    )['phonetized_text']  # Replace with expected output

# Additional tests for other accents and edge cases
