# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import requests


def sanitize_xml(string: str) -> str:
    string = string.replace('&lt', '<')
    string = string.replace('&gt', '>')
    string = string.replace('&amp', '&')
    string = string.replace('&nbsp', ' ')
    return string


def sanitize_string(string: str) -> str:
    string = string.replace('\r', '')
    string = string.replace('\t', '')
    string = string.replace('\n', '')
    return string


def init_cambio() -> str:
    cambio = request.urlopen('https://www.melhorcambio.com/bitcoin').read()
    cambio = str(cambio)
    cambio = sanitize_string(cambio)
    cambio = bytes(cambio, 'iso-8859-1').decode('unicode_escape', 'ignore')
    cambio = sanitize_xml(cambio)
    return cambio


cambio = init_cambio()
soup = BeautifulSoup(cambio, 'lxml')


class BitcoinCotation(object):
    def __init__(self):
        """Bitcoin Cotation Constructor."""
        global cambio
        self.__cambio = cambio

    def bitcoin_price(self, currency: str='real') -> str:
        """Return bitcoin's price updated converted to currency Real"""
        find_begin = '<span itemprop="price">'
        find_end = '</span><input name="valor_minimo_especie" type="hidden"'\
                   ' id="valor_minimo_especie" value=""/>'
        position_begin = int(self.__cambio.index(find_begin) + len(find_begin))
        position_end = int(self.__cambio.index(find_end))

        if currency.upper() == 'REAL':
            return cambio[position_begin: position_end]
        elif currency.upper() == 'REAL':
            pass
        elif currency.upper() == 'EURO':
            pass

    def bitcoin_published(self) -> str:
        """Return the bitcoin's value publication date."""
        find_begin = '<img src="/images/atualizado.png" width="12"> '
        find_end = '</p>      <ul class="coluna-resultados '\
                   'resultados-especie" style="margin-top:0px">'
        position_begin = int(self.__cambio.index(find_begin) + len(find_begin))
        position_end = int(self.__cambio.index(find_end))
        return self.__cambio[position_begin: position_end].replace('Ã s', 'às')

    def bitcoin_icon(self):
        pass


class MercadoBitcoin(object):
    def __init__(self):
        """Mercado Bitcoin Constructor."""
        global cambio
        self.__cambio = cambio

    def mercado_btc_price(self):
        find = '<b>Mercado Bitcoin</b>        <!--         <br><img src="" width="70" > ;        <span style="font-size:10px;color:#999">( <img src="/images/people-cinza.png" width="15"> ; )</span>    --></p>                  <p class="valor" style="color: #f26522;margin: 7px 0 0 0; width: 130px;">           '
        position = int(self.__cambio.index(find) + len(find))
        return self.__cambio[position: position + 9]
