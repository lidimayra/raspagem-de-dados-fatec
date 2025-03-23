## Data scraping with Python @ FATEC Jundiaí

Workshop that happened during the Technology Week 2017 at FATEC Jundiaí

We previously took part on the workshop [Hacking Public Data With Python](https://www.facebook.com/events/240063436506115)
with Professor [Fernando Masanori](https://github.com/fmasanori), where we learned very cool techniques and we decided
to bring our learnings to the [Technology Week](http://www.fatecjd.edu.br/semtec/) at FATEC.

We'll keep the examples we used available in this repo.

## What
**Data scraping** is a computational technique to automate data collection. During the workshop, we'll focus on
_web scraping_, which aims to collect data available on the web.

## Pré-requisitos
- [Python](https://www.python.org/downloads/release/python-3132/) installation

- Required libraries installation. From the command line, run:
```
pip install beautifulsoup4 requests numpy scipy matplotlib
```

:heavy_exclamation_mark: These recommendations are needed for whoever decides to bring their own laptops. We'll ask
Nathan to prepare the machines on the lab beforehand! :confetti_ball:

:small_orange_diamond: For the scripts used during the workshop, installing only `beautifulsoup4` is enough. `scipy`
and `matplotlib` will only be needed on more advanced examples that require data visualization and will be available
here on the repository, but it won't be part of the workshop due to time constraints.

To ensure the installation is successful, open the Python console, import the library and invoke the `BeautifulSoup`
class

```
>>> from bs4 import BeautifulSoup
>>> BeautifulSoup
<class 'bs4.BeautifulSoup'>
```

## References:
- [Marco Tulio Pires GitHub profile](https://github.com/mtrpires)
- [Professor Masanori training repository](https://github.com/fmasanori/treinamento)
- [Book: Web Scraping with Python](https://www.oreilly.com/library/view/web-scraping-with/9781491910283/)

### Our team:
* Ana Carolina Lopes ([@anacls](https://github.com/anacls))
* Jennifer Martins ([@jeemartins](https://github.com/jeemartins))
* Lidiane Taquehara ([@lidimayra](https://github.com/lidimayra))
* Mikaeri Ohana ([@miohana](https://github.com/miohana))
