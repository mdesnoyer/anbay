# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/us/house/ca-39')
def ca_39():
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
    ]

    categories = [
        'Priorities',
        'Health Care',
        'Education',
        'Environment',
        'Economy',
        'Security',
        'Immigration',
        'Governance',
        'Veterans'
    ]
    
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
          'val': u'▼ corporate oversight', 'url':  'https://www.kimforcongress2018.com/issues/'},

        { 'candidate': 'Young Kim', 'category': 'Veterans',
          'val': u'Change the VA', 'url':  'https://www.kimforcongress2018.com/issues/'},

        { 'candidate': 'Young Kim', 'category': 'Immigration',
          'val': u'▲ border security', 'url':  'https://www.kimforcongress2018.com/issues/'},
        { 'candidate': 'Young Kim', 'category': 'Immigration',
          'val': u'Stop separating families', 'url':  'https://www.kimforcongress2018.com/young-kim-congress-must-act-to-stop-future-family-separation/'},

        { 'candidate': 'Young Kim', 'category': 'Security',
          'val': u'Provide high tech equipment to first responders', 'url':  'https://www.kimforcongress2018.com/issues/'},
        { 'candidate': 'Young Kim', 'category': 'Security',
          'val': u'Build international consensus', 'url':  'https://www.kimforcongress2018.com/issues/'},

        { 'candidate': 'Young Kim', 'category': 'Education',
          'val': u'▼ federal education standards', 'url':  'https://www.kimforcongress2018.com/issues/'},
        { 'candidate': 'Young Kim', 'category': 'Education',
          'val': u'▲ STEM funding', 'url':  'https://www.kimforcongress2018.com/issues/'},


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
          
        { 'candidate': 'Gil Cisneros', 'category': 'Education',
          'val': u'▲ K-12 per pupil spending',  'url': 'https://cisnerosforcongress.com/gils-education-plan/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Education',
          'val': u'Reform the student loan system',  'url': 'https://cisnerosforcongress.com/gils-education-plan/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Education',
          'val': u'▲ investment in early childhood education and summer programs',  'url': 'https://cisnerosforcongress.com/gils-education-plan/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Education',
          'val': u'▲ funding for STEAM programs',  'url': 'https://cisnerosforcongress.com/gils-education-plan/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Education',
          'val': u'Invest in teachers',  'url': 'https://cisnerosforcongress.com/gils-education-plan/' },
          
        { 'candidate': 'Gil Cisneros', 'category': 'Environment',
          'val': u'Protect National Parks and the California Coast',  'url': 'https://cisnerosforcongress.com/gil-cisneros-plan-defend-environment/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Environment',
          'val': u'Take action to limit climate change',  'url': 'https://cisnerosforcongress.com/gil-cisneros-plan-defend-environment/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Environment',
          'val': u'▲ R&D and business investment in clean energy',  'url': 'https://cisnerosforcongress.com/gil-cisneros-plan-defend-environment/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Environment',
          'val': u'Strengthen the Clean Air and Water Acts',  'url': 'https://cisnerosforcongress.com/gil-cisneros-plan-defend-environment/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Environment',
          'val': u'▲ water efficiency and recycling investments',  'url': 'https://cisnerosforcongress.com/gil-cisneros-plan-defend-environment/' },

        { 'candidate': 'Gil Cisneros', 'category': 'Security',
          'val': u'Focus on diplomatic solutions',  'url': 'https://cisnerosforcongress.com/gilsplan/national-security-terrorism/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Security',
          'val': u'Work with allies',  'url': 'https://cisnerosforcongress.com/gilsplan/national-security-terrorism/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Security',
          'val': u'▲ intelligence sharing',  'url': 'https://cisnerosforcongress.com/gilsplan/national-security-terrorism/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Security',
          'val': u'Support two-state solution in Israel',  'url': 'https://cisnerosforcongress.com/gilsplan/national-security-terrorism/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Security',
          'val': u'▼ the risk of gun violence',  'url': 'https://cisnerosforcongress.com/gils-gun-violence-prevention-plan/' },


        { 'candidate': 'Gil Cisneros', 'category': 'Immigration',
          'val': u'Protect DREAMers',  'url': 'https://cisnerosforcongress.com/gils-plan-for-immigration-and-protecting-dreamers/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Immigration',
          'val': u'Invest in smart border security, not a wall',  'url': 'https://cisnerosforcongress.com/gils-plan-for-immigration-and-protecting-dreamers/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Immigration',
          'val': u'Keep immigrant families together',  'url': 'https://cisnerosforcongress.com/gils-plan-for-immigration-and-protecting-dreamers/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Immigration',
          'val': u'Support asylum seekers',  'url': 'https://cisnerosforcongress.com/gils-plan-for-immigration-and-protecting-dreamers/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Immigration',
          'val': u'Protect immigrants here legally',  'url': 'https://cisnerosforcongress.com/gils-plan-for-immigration-and-protecting-dreamers/' },

        { 'candidate': 'Gil Cisneros', 'category': 'Governance',
          'val': u'Stop corporate political spending',  'url': 'https://cisnerosforcongress.com/gilsplan/get-corporate-money-politics/' },

        { 'candidate': 'Gil Cisneros', 'category': 'Veterans',
          'val': u'Protect the Post 9/11 G.I. Bill',  'url': 'https://cisnerosforcongress.com/gils-plan-honor-veterans/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Veterans',
          'val': u'Fully fund the VA',  'url': 'https://cisnerosforcongress.com/gils-plan-honor-veterans/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Veterans',
          'val': u'Expand support for injured veteran\'s caregivers',  'url': 'https://cisnerosforcongress.com/gils-plan-honor-veterans/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Veterans',
          'val': u'Protect Vets from discrimination',  'url': 'https://cisnerosforcongress.com/gils-plan-honor-veterans/' },
    ]

    position_categories = set([x['category'] for x in positions])
    
    return render_template(
        'candidate_comparison.html',
        body_name = 'US House',
        district = 'CA-39',
        candidates = candidates,
        categories = [x for x in categories if x in position_categories],
        positions = positions
    )
