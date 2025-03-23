:uk: For an English version, see [README-EN](https://github.com/lidimayra/raspagem-de-dados-fatec/blob/main/README-EN.md)
:uk:

## Raspagem de dados Web com Python @ FATEC Jundiaí

Minicurso realizado durante a Semana de Tecnologia 2017 na Fatec Jundiaí

Nós participamos do curso [Hackeando Dados Públicos usando Python](https://www.facebook.com/events/240063436506115) com o [Fernando Masanori](https://github.com/fmasanori), onde aprendemos técnicas muuuito legais e decidimos levar o nosso aprendizado para a [Semana de Tecnologia](http://www.fatecjd.edu.br/semtec/) da Fatec. Os exemplos utilizados continuarão disponíveis aqui.

## O que é
A **raspagem de dados** (_data scraping_) é uma técnica computacional de coleta automatizada de dados. Durante o curso focaremos no _web scraping_, cuja finalidade consiste em extrair dados que podem ser visualizados em um navegador web.

## Pré-requisitos
- Instalação do [Python](https://www.python.org/downloads/release/python-3132/)

- Instalação das bibliotecas. A partir do terminal de comando execute:
```
pip install beautifulsoup4 requests numpy scipy matplotlib
```

:heavy_exclamation_mark: Estas recomendações são necessárias para quem optar por levar o próprio notebook. Pediremos ao Nathan pra deixar os computadores do laboratório já preparados no dia! :confetti_ball:

:small_orange_diamond: Para os scripts que usaremos durante o minicurso, a instalação do `beautifulsoup4` é suficiente. `numpy`, `scipy` e `matplotlib` serão utilizadas apenas em exemplos mais avançados que envolvem visualização de dados e não serão abordados durante a apresentação devido ao tempo.

Para garantir que a instalação foi realizada com sucesso, abra o console Python, faça a importação da biblioteca e chame pela classe `BeautifulSoup`:

```
>>> from bs4 import BeautifulSoup
>>> BeautifulSoup
<class 'bs4.BeautifulSoup'>
```

## Para saber mais:
- [Github do Marco Tulio Pires](https://github.com/mtrpires)
- [Repositório de treinamento do Masanori](https://github.com/fmasanori/treinamento)
- [Livro Web Scraping com Python](https://novatec.com.br/livros/web-scraping-com-python/)

### Nossa equipe:
* Ana Carolina Lopes ([@anacls](https://github.com/anacls))
* Jennifer Martins ([@jeemartins](https://github.com/jeemartins))
* Lidiane Taquehara ([@lidimayra](https://github.com/lidimayra))
* Mikaeri Ohana ([@miohana](https://github.com/miohana))
