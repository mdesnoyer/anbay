# -*- coding: utf-8 -*-

import datetime as dt
from flask import Flask, render_template, request

app = Flask(__name__)

_deploy_day = dt.datetime.now().date().isoformat()

categories = [
    'Priorities',
    'Healthcare',
    'Education',
    'Environment',
    'Economy',
    'Security',
    'Immigration',
    'Governance',
    'Veterans'
]

@app.route('/sitemap.xml')
def sitemap():
    pages = [
        '/us/house/ca-39',
        '/us/house/ca-48',
    ]

    return render_template(
        'sitemap_template.xml',
        pages = [(x, _deploy_day) for x in pages]
        )

@app.route('/us/house/ca-39')
@app.route('/')
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
          'val': u'Healthcare',  'url': 'https://votersedge.org/en/ca/ballot/election/area/69/contests/contest/16621/candidate/138040?id=statewide-69-ca'},
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
          
        { 'candidate': 'Gil Cisneros', 'category': 'Healthcare',
          'val': u'Protect existing coverage in the ACA',  'url': 'https://cisnerosforcongress.com/gilsplan/healthcare-for-all/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Healthcare',
          'val': u'▼ drug prices by allowing the government to negotiate with drug companies.',  'url': 'https://cisnerosforcongress.com/gilsplan/healthcare-for-all/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Healthcare',
          'val': u'Allow anybody to buy into Medicare.',  'url': 'https://cisnerosforcongress.com/gilsplan/healthcare-for-all/' },
        { 'candidate': 'Gil Cisneros', 'category': 'Healthcare',
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

@app.route('/us/house/ca-48')
def ca48():
    candidates = [
        {
            'name': 'Harley Rouda',
            'party': 'Democrat',
            'url': 'https://www.harleyforcongress.com/',
        },
        {
            'name': 'Dana Rohrabacher',
            'party': 'Republican',
            'url': 'http://www.rohrabacher.com',
            },
    ]

    positions = [
        { 'candidate': 'Harley Rouda', 'category': 'Priorities',
          'val': u'Healthcare',  'url': 'https://votersedge.org/en/ca/ballot/election/area/69/contests/contest/16630/candidate/138091?id=statewide-69-ca'},
        { 'candidate': 'Harley Rouda', 'category': 'Priorities',
          'val': u'Environment',  'url': 'https://votersedge.org/en/ca/ballot/election/area/69/contests/contest/16630/candidate/138091?id=statewide-69-ca'},
        { 'candidate': 'Harley Rouda', 'category': 'Priorities',
          'val': u'Education',  'url': 'https://votersedge.org/en/ca/ballot/election/area/69/contests/contest/16630/candidate/138091?id=statewide-69-ca'},

        { 'candidate': 'Harley Rouda', 'category': 'Economy',
          'val': u'Close tax loopholes for the wealthy',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Economy',
          'val': u'▲ taxes on old industries',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Economy',
          'val': u'Invest in education',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Education',
          'val': u'Universal pre-kindergarten',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Education',
          'val': u'Tuition-free university and college',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Education',
          'val': u'▲ trade apprentiships',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Education',
          'val': u'Tax credit for employers who contribute to employees\' student loans',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Security',
          'val': u'▼ the risk of gun violence',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Healthcare',
          'val': u'Protect pre-existing coverage in the ACA',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Healthcare',
          'val': u'Expand Medicare',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Healthcare',
          'val': u'Stop the abuse of opioids',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Governance',
          'val': u'Stop corporate political spending',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Environment',
          'val': u'Protect the California coast from drilling',  'url': 'https://www.harleyforcongress.com/issues/'},
        { 'candidate': 'Harley Rouda', 'category': 'Environment',
          'val': u'▲ clean energy investment',  'url': 'https://www.harleyforcongress.com/issues/'},


        { 'candidate': 'Dana Rohrabacher', 'category': 'Priorities',
          'val': u'Immigration',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Priorities',
          'val': u'Technology',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Priorities',
          'val': u'Energy',  'url': 'http://www.rohrabacher.com/issues.html'},

        { 'candidate': 'Dana Rohrabacher', 'category': 'Economy',
          'val': u'▼ all taxes',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Economy',
          'val': u'Protect patents',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Economy',
          'val': u'▲ aerospace spending',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Environment',
          'val': u'▲ oil and gas drilling and fracking',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Environment',
          'val': u'Build solar farms on federal land',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Environment',
          'val': u'Build water reclamation and desalination plants',  'url': 'https://voiceofoc.org/2018/08/epa-provides-135-million-for-innovative-groundwater-replenishment-project-expansion-in-orange-county/'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Environment',
          'val': u'▼ oversight of water pollution',  'url': 'https://www.congress.gov/bill/115th-congress/house-bill/953'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Environment',
          'val': u'Global warming does not exist',  'url': 'https://en.wikipedia.org/wiki/Dana_Rohrabacher#Global_warming'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Security',
          'val': u'▼ the number of troops',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Security',
          'val': u'▲ spending on military technology',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Immigration',
          'val': u'▲ screening of people applying for jobs',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Immigration',
          'val': u'▲ requirements to use the safety net',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Immigration',
          'val': u'No citizenship for immigrants without papers',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Security',
          'val': u'▲ spending on border security',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Education',
          'val': u'Remove federal education standards',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Security',
          'val': u'Reduce surveillance within the US',  'url': 'http://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Healthcare',
          'val': u'▼ insurance coverage',  'url': 'https://en.wikipedia.org/wiki/American_Health_Care_Act_of_2017#Estimated_impact_of_the_Republican_AHCA_and_BCRA'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Healthcare',
          'val': u'▼ premiums for younger people',  'url': 'https://en.wikipedia.org/wiki/American_Health_Care_Act_of_2017#Insurance_costs_and_quality'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Healthcare',
          'val': u'▲ premiums for older people',  'url': 'https://en.wikipedia.org/wiki/American_Health_Care_Act_of_2017#Insurance_costs_and_qualityhttp://www.rohrabacher.com/issues.html'},
        { 'candidate': 'Dana Rohrabacher', 'category': 'Governance',
          'val': u'Release the 9/11 and Kennedy assasination reports',  'url': 'http://www.rohrabacher.com/issues.html'},

    ]

    position_categories = set([x['category'] for x in positions])

    return render_template(
        'candidate_comparison.html',
        body_name = 'US House',
        district = 'CA-48',
        candidates = candidates,
        categories = [x for x in categories if x in position_categories],
        positions = positions
    )
