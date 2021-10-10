Aluno: Giovani G. Marciniak
GRR20182981

O trabalho contém dois arquivos, sendo:
- histograma.py : implementação dos testes em cor (três bandas)
- histogramaPB.py : implementação testes preto e branco

Dependências:
É necessário o pacote OpenCV e Python3.

Para executar:
$ python3 histograma.py
$ python3 histogramaPB.py

- Quantas imagens foram classificadas corretamente usando cada uma das distâncias?
COLORIDO:
O método Correlation acertou 8 . Taxa de acerto:  57.14285714285714 %
O método Chi-Square acertou 10 . Taxa de acerto:  71.42857142857143 %
O método Intersection acertou 6 . Taxa de acerto:  42.857142857142854 %
O método Bhattacharyya acertou 11 . Taxa de acerto:  78.57142857142857 %

NÍVEIS DE CINZA
O método Correlation acertou 7 . Taxa de acerto:  50.0 %
O método Chi-Square acertou 7 . Taxa de acerto:  50.0 %
O método Intersection acertou 5 . Taxa de acerto:  35.714285714285715 %
O método Bhattacharyya acertou 8 . Taxa de acerto:  57.14285714285714 %

- O desempenho usando imagens coloridas e em nível de cinza foi o mesmo? Se não, porque? 
Não. As imagens em geral possuem iluminação semelhante, o principal fator para fazer a diferenciação é a cor.
Ao converter para níveis de cinza a informação de cor é perdida e consequentemente o classificador tem mais dificuldade em classificar corretamente.
