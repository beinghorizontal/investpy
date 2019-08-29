#!/usr/bin/env python

# Copyright 2018-2019 Alvaro Bartolome
# See LICENSE for details.

import pytest

import investpy

from investpy.user_agent import get_random, clear_file, delete_file


def test_equity_errors():
    """
    This function raises errors on equity functions
    """

    params = [
        {
            'equity': None,
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'as_json': 'error',
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'as_json': True,
            'order': 'error',
            'debug': True
        },
        {
            'equity': 'error',
            'as_json': True,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': ['error'],
            'as_json': True,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'as_json': True,
            'order': 'ascending',
            'debug': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_recent_data(equity=param['equity'],
                                     as_json=param['as_json'],
                                     order=param['order'],
                                     debug=param['debug'])
        except:
            pass

    params = [
        {
            'equity': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2019',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/1999',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/1950',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2019',
            'to_date': '01/01/1999',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'equity': 'bbva',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_historical_data(equity=param['equity'],
                                         from_date=param['from_date'],
                                         to_date=param['to_date'],
                                         as_json=param['as_json'],
                                         order=param['order'],
                                         debug=param['debug'])
        except:
            pass

    params = [
        {
            'equity': None,
            'language': 'spanish'
        },
        {
            'equity': 'bbva',
            'language': 'error'
        },
        {
            'equity': 'error',
            'language': 'spanish'
        },
        {
            'equity': ['error'],
            'language': 'spanish'
        },
    ]

    for param in params:
        try:
            investpy.get_equity_company_profile(equity=param['equity'],
                                                language=param['language'])
        except:
            pass


def test_fund_errors():
    """
    This function raises errors on fund functions
    """

    params = [
        {
            'columns': None,
            'as_json': 'error'
        },
        {
            'columns': 0,
            'as_json': True
        },
        {
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_funds_dict(columns=param['columns'],
                                    as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'fund': None,
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'as_json': 'error',
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'as_json': True,
            'order': 'error',
            'debug': True
        },
        {
            'fund': 'error',
            'as_json': True,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': ['error'],
            'as_json': True,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'as_json': True,
            'order': 'ascending',
            'debug': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_fund_recent_data(fund=param['fund'],
                                          as_json=param['as_json'],
                                          order=param['order'],
                                          debug=param['debug'])
        except:
            pass

    params = [
        {
            'fund': 'quality inversion conservadora fi',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'from_date': '01/01/2019',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': ['error'],
            'from_date': '01/01/1998',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'from_date': '01/01/1998',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'from_date': '01/01/2019',
            'to_date': '01/01/1998',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'fund': 'quality inversion conservadora fi',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_fund_historical_data(fund=param['fund'],
                                              from_date=param['from_date'],
                                              to_date=param['to_date'],
                                              as_json=param['as_json'],
                                              order=param['order'],
                                              debug=param['debug'])
        except:
            pass

    params = [
        {
            'fund': None,
            'as_json': False
        },
        {
            'fund': 'quality inversion conservadora fi',
            'as_json': 'error'
        },
        {
            'fund': 'error',
            'as_json': True
        },
        {
            'fund': ['error'],
            'as_json': True
        },
    ]

    for param in params:
        try:
            investpy.get_fund_information(fund=param['fund'],
                                          as_json=param['as_json'])
        except:
            pass


def test_etf_errors():
    """
    This function raises errors on etf functions
    """

    params = [
        {
            'country': None,
            'columns': None,
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': 'error'
        },
        {
            'country': 'spain',
            'columns': 0,
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_etf_dict(country=param['country'],
                                  columns=param['columns'],
                                  as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'etf': None,
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'as_json': 'error',
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'as_json': True,
            'order': 'error',
            'debug': True
        },
        {
            'etf': 'error',
            'as_json': True,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': ['error'],
            'as_json': True,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'as_json': True,
            'order': 'ascending',
            'debug': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_etf_recent_data(etf=param['etf'],
                                         as_json=param['as_json'],
                                         order=param['order'],
                                         debug=param['debug'])
        except:
            pass

    params = [
        {
            'etf': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'from_date': '01/01/2019',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'from_date': '01/01/1998',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'from_date': '01/01/2019',
            'to_date': '01/01/1998',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'as_json': False,
            'order': 'ascending',
            'debug': True
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'debug': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_etf_historical_data(etf=param['etf'],
                                             from_date=param['from_date'],
                                             to_date=param['to_date'],
                                             as_json=param['as_json'],
                                             order=param['order'],
                                             debug=param['debug'])
        except:
            pass


def test_user_agent_errors():
    """
    This function raises errors on user_agent functions
    """

    clear_file()
    try:
        get_random()
    except:
        pass

    delete_file()
    try:
        get_random()
    except:
        pass


if __name__ == '__main__':
    test_equity_errors()
    test_fund_errors()
    test_etf_errors()
    test_user_agent_errors()
