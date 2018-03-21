# -*- coding: utf-8 -*-

"""Feed news under rss news sites.
Refence sites:
-Uol.
-Terra.
-G1.
-Valor Econômico
-Times.
"""

import feedparser
import json
import os
from datetime import datetime
from time import strftime
import calendar

current_file = os.path.realpath(__file__)
current_path = current_file[:current_file.rfind("/")]
site_file = "{0}/{1}".format(current_path, 'sites.json')


def published_parsed(date=None):
    if date:
        return strftime('%d/%m/%Y - %H:%M', date)
    else:
        return ''


class UolNoticias(object):
    """Uol Notícias.
    Will be acquireds news from uol of the categories:
    - Technology
    - News
    - Economy
    """

    def __init__(self):
        """Uol Notícias Constructor."""
        if os.path.isfile(site_file):
            try:
                with open(site_file, 'r') as sites:
                    site_json = json.load(sites)
                    self.__uol_tec = site_json['UolNoticias']['uol_tec']
                    self.__uol_news = site_json['UolNoticias']['uol_news']
                    self.__uol_econ = site_json['UolNoticias']['uol_econ']
            except:
                pass

    @property
    def uol_tec(self):
        """Return all information about uol technology."""
        try:
            return feedparser.parse(self.__uol_tec)
        except:
            pass

    @property
    def uol_news(self):
        """Return all information about uol news."""
        return feedparser.parse(self.__uol_news)

    @property
    def uol_econ(self):
        """Return all information about uol economy."""
        try:
            return feedparser.parse(self.__uol_econ)
        except:
            pass


class ValorEconomico(object):
    """Valor Economico.
    Will be acquireds news from valor economico of the categories:
    - Finanacial
    - Politics
    - Business
    - International
    """

    def __init__(self):
        """Valor Economico Constructor."""
        if os.path.isfile(site_file):
            try:
                with open(site_file, 'r') as sites:
                    site_json = json.load(sites)

                    """The r variable it is being used to reduce the variable
                    name.
                    """
                    r = site_json['ValorEconomico']
                    self.__valor_financial = r['valor_fin']
                    self.__valor_politics = r['valor_pol']
                    self.__valor_business = r['valor_bus']
                    self.__valor_international = r['valor_inter']
            except IOError as err:
                print('Error to open file: ' + str(err))

    @property
    def valor_financial(self):
        """Return all information about  valor financial."""
        try:
            return feedparser.parse(self.__valor_financial)
        except:
            pass

    @property
    def valor_politics(self):
        """Return all information about valor politics."""
        try:
            return feedparser.parse(self.__valor_politics)
        except:
            pass

    @property
    def valor_business(self):
        """Return all information about valor business."""
        try:
            return feedparser.parse(self.__valor_business)
        except:
            pass

    @property
    def valor_international(self):
        """Return all information about valor international."""
        try:
            return feedparser.parse(self.__valor_international)
        except:
            pass


class NewsBTC(object):
    def __init__(self):
        """NewsBTC Constructor."""
        global site_file
        self.__site_file = site_file
        if os.path.isfile(self.__site_file):
            with open(site_file, 'r') as sites:
                site_json = json.load(sites)
                self.__news_btc = site_json['NewsBTC']['newsbtc']

    @property
    def news_btc(self):
        try:
            return feedparser.parse(self.__news_btc)
        except:
            pass


class BitcoinNews(object):
    def __init__(self):
        """Bitcoin News Constructor."""
        global site_file
        self.__site_file = site_file
        if os.path.isfile(self.__site_file):
            with open(site_file, 'r') as sites:
                site_json = json.load(sites)
                self.__bitcoin_news = site_json['BitcoinNews']['bitcoin_news']

    @property
    def bitcoin_news(self):
        try:
            return feedparser.parse(self.__bitcoin_news)
        except:
            pass
