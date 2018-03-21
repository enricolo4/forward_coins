from urllib import request
import json
import requests
from bs4 import BeautifulSoup


def sanitize_xml(string: str) -> str:
    """Clean trash strings."""
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


def remove_duplicate_dict(dictionary: dict={}) -> dict:
    pass


class MarketCap(object):

    def __init__(self):
        """Coin Market Cap Constructor."""
        self.__url_currencies = 'https://api.coinmarketcap.com/v1/ticker/'
        self.__currencies = None
        self.__url_currency = 'https://coinmarketcap.com/currencies/'
        self.__marketcap_url = 'https://coinmarketcap.com/currencies/'

    def get_currencies(self,
                       currency_id: str = '',
                       start: int = 0,
                       limit: int = 0,
                       convert: str = '') -> list:
        """
        Return a list of the currencies.
        @param currency_id: Currency Id like bitcoin.
        @param start: Start the search from desired position until the last\
         currency of the list.
        @param limit: Print a limited amount of the currencies.
        @param convert: Used to convert the currency value another currency\
         value as such Bitcoin to Dolar/Bitcoin to Euro.

        """
        if currency_id:
            suf = currency_id
        else:
            suf = '?start=%d&limit=%d&convert=%s' % (start, limit, convert)

        try:
            self.__currencies = requests.request(
                method='GET',
                url=self.__url_currencies + suf
                )
            return self.__currencies.json()
        except:
            pass

    @property
    def currency_ids(self) -> dict:
        """Create a dict with all currencies' id."""
        suf = '?&limit=0'

        try:
            self.__currencies = requests.request(
                method='GET',
                url=self.__url_currencies + suf
                )
            dict_id = {}
            for k in self.__currencies.json():
                dict_id.update({k['name']: k['id']})
            return dict_id
        except:
            pass

    def traders_currencies(self,
                           currency_id: str = 'bitcoin',
                           generate_file: bool = False) -> dict:
        sufixo = '%s/#markets' % (currency_id)
        dict_traders = {}

        try:
            url = request.urlopen(self.__marketcap_url + sufixo)
            soup = BeautifulSoup(url, 'html.parser')
            traders_attrs = list(soup.find('tbody').find_all('tr'))

            for k in traders_attrs:
                pair = str(k.find_all('td')[2].get_text())

                volume_24 = sanitize_string(str(k.find('span', class_="volume")
                                                .get_text()))

                price = sanitize_string(str(k.find('span', class_="price")
                                            .get_text()))

                volume_percent = sanitize_string(str(k.find_all('td')[5]
                                                     .get_text()))

                dict_traders.update(
                    {
                        str(k.td.get_text()):
                        {
                            'source': str(k.a.get_text()),
                            'pair': pair,
                            'volume_24': volume_24,
                            'price': price,
                            'volume_percent': volume_percent
                        }
                    })

            if generate_file:
                with open(currency_id + '.json', 'w') as currency_json:
                    json.dump(dict_traders, currency_json, indent=4)
            return dict_traders
        except:
            pass
