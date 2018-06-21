import string as str
import re
import matplotlib.pylab as grf
import numpy as np
import matplotlib.ticker as ticker


def total_de_letras(texto, letters):
    for letter in texto:
        letters[letter] = letters.get(letter, 0) + 1
    totalLetters = sum(letters.values())

    ##print("O total de letras é: ", letters)
    ##print("A soma total é: ", totalLetters)

    return totalLetters


def letras(texto, letters):
    for letter in texto:
        letters[letter] = letters.get(letter, 0) + 1

    return letters


def primeira_questao(texto, letters):
    totalLetters = total_de_letras(texto, letters)

    for i in letters:
        letters[i] = round(letters[i] / totalLetters, 5)

    return letters


def plotar_grafico(letters):
    x = list(letters.keys())
    ymin = [0] * len(letters)
    y = list(letters.values())

    grf.vlines(x, ymin=ymin, ymax=y)
    grf.show()


def segunda_questao(alphabet, bigram, texto):
    for i in alphabet:
        for j in alphabet:
            bigram[i + j] = 0

    for i in range(len(texto) - 1):
        bigram[texto[i] + texto[i + 1]] += 1
    ##print("O total de bigramas é: ", bigram)

    for i in bigram:
        bigram[i] = round(bigram[i] / (len(texto) - 1), 5)

    ##print("A probabilidade de bigramas é: ", bigram)

    return bigram


def plot_graf_sec(bigram):
    z = list(bigram.values())

    z = np.array(z).reshape(27, 27)

    x = list(bigram.keys())

    ##print(x)

    y = list(bigram.keys())

    fig = grf.figure()

    fig, ax = grf.subplots(1, 1, figsize=(27, 27))
    heatplot = ax.imshow(z, cmap='RdPu')
    ax.set_xticklabels(x)
    ax.set_yticklabels(y)

    tick_spacing = 0.8

    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_title("Bigram Plot")
    ax.set_xlabel('Letters')
    ax.set_ylabel('Letters')

    grf.show()


def terceira_questao(bigram, letters):
    probCond = {}
    probCond2 = {}
    for i in letters:
        for j in letters:
            probCond[i + j] = round(bigram[j + i] / letters[i], 6)

    print("prob x|y: ", probCond)

    for i in letters:
        for j in letters:
            probCond2[i + j] = round(bigram[i + j] / letters[i], 6)

    print("prob y|x ", probCond2)

    plot_graf_sec(probCond)
    plot_graf_sec(probCond2)


def main():
    alphabet = str.ascii_lowercase + ' '
    letters = {}
    bigram = {}

    for letter in alphabet:
        letters[letter] = 0

    arquivo = open('test.txt', 'r')
    vetor_texto = arquivo.read().lower()

    vetor_texto = re.sub('[^a-zA-Z ]', '', re.sub(r'\.', ' ', vetor_texto))

    plotar_grafico(primeira_questao(vetor_texto, letters))

    plot_graf_sec(segunda_questao(alphabet, bigram, vetor_texto))

    terceira_questao(segunda_questao(alphabet, bigram, vetor_texto), letras(vetor_texto,     letters))

    arquivo.close()

if __name__ == '__main__':
    main()



