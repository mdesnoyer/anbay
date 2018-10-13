# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/us/house/ca-39')
def ca_39():
    return render_template(
        'candidate_comparison.html',
        body_name = 'US House',
        district = 'CA-39',
        candidates = [
            {
                'name': 'Gil Cisneros',
                'party': 'Democrat',
                'url': 'https://cisnerosforcongress.com/',
            },
            {
                'name': 'Young Kim',
                'party': 'Republican',
                'url': 'https://www.kimforcongress2018.com',
            },
        ],
        categories = [
            'Priorities',
            'Health Care',
            'Education',
            'Environment',
            'Economy',
            'Security',
            'Immigration',
        ],
        positions = [
            { 'candidate': 'Young Kim', 'category': 'Priorities',
              'val': 'Economy', 'url': 'https://www.kimforcongress2018.com/issues/'},
            { 'candidate': 'Young Kim', 'category': 'Priorities',
              'val': 'Security', 'url': 'https://www.kimforcongress2018.com/issues/'},
            { 'candidate': 'Young Kim', 'category': 'Priorities',
              'val': 'Veterans', 'url': 'https://www.kimforcongress2018.com/issues/'},
            { 'candidate': 'Young Kim', 'category': 'Economy',
              'val': u'▼ all taxes', 'url':  'https://www.kimforcongress2018.com/issues/'},
            { 'candidate': 'Young Kim', 'category': 'Economy',
              'val': u'▲ trade', 'url':  'https://www.kimforcongress2018.com/issues/'},
            { 'candidate': 'Young Kim', 'category': 'Economy',
              'val': u'▼ corporate standards', 'url':  'https://www.kimforcongress2018.com/issues/'},
            { 'candidate': 'Gil Cisneros', 'category': 'Priorities',
              'val': u'Education',  'url': 'https://votersedge.org/en/ca/ballot/election/area/69/contests/contest/16621/candidate/138040?id=statewide-69-ca'},
            { 'candidate': 'Gil Cisneros', 'category': 'Priorities',
              'val': u'Health Care',  'url': 'https://cisnerosforcongress.com/'},
            { 'candidate': 'Gil Cisneros', 'category': 'Priorities',
              'val': u'Veterans',  'url': 'https://votersedge.org/en/ca/ballot/election/area/69/contests/contest/16621/candidate/138040?id=statewide-69-ca'},
            { 'candidate': 'Gil Cisneros', 'category': 'Economy',
              'val': u'▲ the minimum wage',  'url': 'https://cisnerosforcongress.com/gilsplan/economy-works-middle-class/'},
            { 'candidate': 'Gil Cisneros', 'category': 'Economy',
              'val': u'▲ taxes on corporations',  'url': 'https://cisnerosforcongress.com/gilsplan/economy-works-middle-class/' },
            { 'candidate': 'Gil Cisneros', 'category': 'Economy',
              'val': u'▼ taxes on the middle class',  'url': 'https://cisnerosforcongress.com/gilsplan/economy-works-middle-class/' },
            { 'candidate': 'Gil Cisneros', 'category': 'Economy',
              'val': u'Invest in education and childcare',  'url': 'https://cisnerosforcongress.com/gilsplan/economy-works-middle-class/' },
            { 'candidate': 'Gil Cisneros', 'category': 'Economy',
              'val': u'Paid family leave',  'url': 'https://cisnerosforcongress.com/gilsplan/economy-works-middle-class/' },
            { 'candidate': 'Gil Cisneros', 'category': 'Health Care',
              'val': u'Protect existing coverage in the ACA',  'url': 'https://cisnerosforcongress.com/gilsplan/healthcare-for-all/' },
            { 'candidate': 'Gil Cisneros', 'category': 'Health Care',
              'val': u'▼ drug prices by allowing the government to negotiate with drug companies.',  'url': 'https://cisnerosforcongress.com/gilsplan/healthcare-for-all/' },
            { 'candidate': 'Gil Cisneros', 'category': 'Health Care',
              'val': u'Allow anybody to buy into Medicare.',  'url': 'https://cisnerosforcongress.com/gilsplan/healthcare-for-all/' },
            { 'candidate': 'Gil Cisneros', 'category': 'Health Care',
              'val': u'Sponsor the Disability Integration Act.',  'url': 'https://cisnerosforcongress.com/gils-plan-americans-disabilities/' },
        ],
    )
