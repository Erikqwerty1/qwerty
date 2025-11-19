import re
def normalize(text, *, casefold = True, yo2e = True):
    text = re.sub(r"[\t\r\n\f\v]", " ", text)
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    text = re.sub(r" +", " ", text)
    text = text.strip()
    return text
print('A1')
print("ТЕСТ ДЛЯ NORMALIZE:")
text = "ПрИвЕт\nМИр\t"
text = normalize(text)
print(text)
text = "ёжик, Ёлка"
text = normalize(text)
print(text)
text = "Hello\r\nWorld"
text = normalize(text)
print(text)
text = "  двойные   пробелы  "
text = normalize(text)
print(text)

def tokenize(text):
    pattern = r"\b[\w]+(?:-[\w]+)*\b"
    return re.findall(pattern, text)
print('A2')
print("ТЕСТ ДЛЯ TOKENIZE:")
text = "привет мир"
text = tokenize(text)
print(text)
text = "hello,world!!!"
text = tokenize(text)
print(text)
text = "по-настоящему круто"
text = tokenize(text)
print(text)
text = "2025 год"
text = tokenize(text)
print(text)
text = "emoji 😀 не слово"
text = tokenize(text)
print(text)

def count_freq(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] = freq[token] + 1
        else:
            freq[token] = 1
    return freq
def top_n(freq, n = 2):
    spisok = []
    for word in freq:
        spisok.append((freq[word], word))
    spisok.sort(reverse=True)
    sortelement = []
    for count, word in spisok:
        sortelement.append((word, count))   
    return sortelement[:n]
print('A3')
print("ТЕСТ ДЛЯ COUNT_FREQ + TOP_N:")
tokens = ["a", "b", "a", "c", "b", "a"]
otvet=count_freq(tokens)
print(otvet)
freq=top_n(otvet)
print(freq)
tokens = ["bb", "aa", "bb", "aa", "cc"]
otvet=count_freq(tokens)
print(otvet)
freq=top_n(otvet)
print(freq)
