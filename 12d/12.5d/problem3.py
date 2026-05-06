def analyze_sentence(sentence: str) -> dict:
    dct = {}

    words = sentence.split()

    dct["words"] = len(words)
    dct["longest"] = max(words, key=lambda x: len(x))
    dct["ends_with_dot"] = True if sentence.endswith(".") else False

    return dct


print(analyze_sentence("Python dasturi juda qulay va dasturchilarga yoqadi."))
# words=7 longest="dasturchilarga" ends_with_dot=True


print(analyze_sentence("Salom dunyo"))
# words=2 longest="dunyo" ends_with_dot=False
