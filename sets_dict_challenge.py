# Challenge-1:
# Create a Python script that removes all the elements of a list that are duplicates.
# Do the challenge in a single line of code using sets.

#CHALLENGE -2:
# Consider a list of words (strings). Write a Python script that generates a dictionary where the key is the word in the list and the value is its length.
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# words_length=dict()
# for item in words:
#     words_length[item]=len(item)
# print(words_length)

#CHALLENGE 3-
# Considering the following dict, get a dict representation sorted by key.
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# d2=sorted(d1.items(), key=lambda x:x[0])
# print(d2)
# print(d2)

#CHALLENGE-4 :
# Considering the following dict, get a dict representation sorted by value.
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# d2=sorted((d1.items()), key=lambda x:x[1])
# print(d2)

#CHALLENGE-5 :
# Let's generalize the last challenge and sort a dictionary by any field of its values if the value is a composite type (list, tuple, etc).
# Example: Considering this dictionary print a sorted view of the dictionary by the second field of its values.
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# d1=sorted(employees.items(), key=lambda x:x[1][1])
# print(d1)

#CHALLENGE 6:
# Consider this dictionary. Print a sorted view of the dictionary by the third field of its values, in reverse order.
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# d1=sorted(employees.items(), key=lambda x:x[1][2], reverse=True)
# print(d1)

#CHALLENGE 7:Print a sorted view of the dictionary, by the key (country code).
# country = {
# "MX":"MEXICO",
# "RW":"RWANDA",
# "BI":"BURUNDI",
# "PR":"PUERTO RICO",
# "GM":"GAMBIA",
# "SR":"SURINAME",
# "KG":"KYRGYZSTAN",
# "GA":"GABON",
# "CK":"COOK ISLANDS",
# "VN":"VIET NAM",
# "UZ":"UZBEKISTAN",
# "BG":"BULGARIA",
# "JP":"JAPAN",
# "KP":"KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
# "PL":"POLAND",
# "BB":"BARBADOS",
# "CF":"CENTRAL AFRICAN REPUBLIC",
# "GI":"GIBRALTAR",
# "AE":"UNITED ARAB EMIRATES",
# "MY":"MALAYSIA",
# "KI":"KIRIBATI",
# "RU":"RUSSIAN FEDERATION",
# "MQ":"MARTINIQUE",
# "SB":"SOLOMON ISLANDS",
# "TL":"TIMOR-LESTE",
# "VI":"VIRGIN ISLANDS, U.S.",
# "FR":"FRANCE",
# "ZA":"SOUTH AFRICA",
# "NE":"NIGER",
# "IE":"IRELAND",
# "MG":"MADAGASCAR",
# "TC":"TURKS AND CAICOS ISLANDS",
# "BW":"BOTSWANA",
# "KY":"CAYMAN ISLANDS",
# "JO":"JORDAN",
# "MR":"MAURITANIA",
# "NI":"NICARAGUA",
# "KM":"COMOROS",
# "FK":"FALKLAND ISLANDS (MALVINAS)",
# "SH":"SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA",
# "PF":"FRENCH POLYNESIA",
# "DK":"DENMARK",
# "PT":"PORTUGAL",
# "NR":"NAURU",
# "DM":"DOMINICA",
# "GH":"GHANA",
# "GP":"GUADELOUPE",
# "CU":"CUBA",
# "GR":"GREECE",
# "AS":"AMERICAN SAMOA",
# "AI":"ANGUILLA",
# "LS":"LESOTHO",
# "TJ":"TAJIKISTAN",
# "AW":"ARUBA",
# "GY":"GUYANA",
# "LC":"SAINT LUCIA",
# "GG":"GUERNSEY",
# "TG":"TOGO",
# "OM":"OMAN",
# "NL":"NETHERLANDS",
# "MT":"MALTA",
# "MD":"MOLDOVA, REPUBLIC OF",
# "EC":"ECUADOR",
# "FM":"MICRONESIA, FEDERATED STATES OF",
# "CA":"CANADA",
# "TT":"TRINIDAD AND TOBAGO",
# "CN":"CHINA",
# "CM":"CAMEROON",
# "BD":"BANGLADESH",
# "LK":"SRI LANKA",
# "CO":"COLOMBIA",
# "LT":"LITHUANIA",
# "DJ":"DJIBOUTI",
# "CX":"CHRISTMAS ISLAND",
# "TF":"FRENCH SOUTHERN TERRITORIES",
# "TM":"TURKMENISTAN",
# "SC":"SEYCHELLES",
# "MK":"MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
# "TH":"THAILAND",
# "LA":"LAO PEOPLE'S DEMOCRATIC REPUBLIC",
# "BE":"BELGIUM",
# "UY":"URUGUAY",
# "MV":"MALDIVES",
# "SZ":"SWAZILAND",
# "MN":"MONGOLIA",
# "PK":"PAKISTAN",
# "BZ":"BELIZE",
# "AT":"AUSTRIA",
# "WF":"WALLIS AND FUTUNA",
# "GD":"GRENADA",
# "RO":"ROMANIA",
# "SJ":"SVALBARD AND JAN MAYEN",
# "CV":"CAPE VERDE",
# "UG":"UGANDA",
# "CR":"COSTA RICA",
# "HM":"HEARD ISLAND AND MCDONALD ISLANDS",
# "TN":"TUNISIA",
# "MC":"MONACO",
# "MP":"NORTHERN MARIANA ISLANDS",
# "SN":"SENEGAL",
# "PW":"PALAU",
# "VC":"SAINT VINCENT AND THE GRENADINES",
# "ST":"SAO TOME AND PRINCIPE",
# "DO":"DOMINICAN REPUBLIC",
# "EG":"EGYPT",
# "TZ":"TANZANIA, UNITED REPUBLIC OF",
# "SV":"EL SALVADOR",
# "TR":"TURKEY",
# "SG":"SINGAPORE",
# "UM":"UNITED STATES MINOR OUTLYING ISLANDS",
# "KR":"KOREA, REPUBLIC OF",
# "PG":"PAPUA NEW GUINEA",
# "GQ":"EQUATORIAL GUINEA",
# "US":"UNITED STATES",
# "BF":"BURKINA FASO",
# "AM":"ARMENIA",
# "TD":"CHAD",
# "NP":"NEPAL",
# "IT":"ITALY",
# "IO":"BRITISH INDIAN OCEAN TERRITORY",
# "ZW ":"ZIMBABWE",
# "HU":"HUNGARY",
# "BR":"BRAZIL",
# "IN":"INDIA",
# "PH":"PHILIPPINES",
# "TW":"TAIWAN, PROVINCE OF CHINA",
# "AO":"ANGOLA",
# "MH":"MARSHALL ISLANDS",
# "NO":"NORWAY",
# "JE":"JERSEY",
# "VU":"VANUATU",
# "EE":"ESTONIA",
# "AF":"AFGHANISTAN",
# "AX":"ALAND ISLANDS",
# "GN":"GUINEA",
# "FO":"FAROE ISLANDS",
# "SE":"SWEDEN",
# "SL":"SIERRA LEONE",
# "LB":"LEBANON",
# "MO":"MACAO",
# "IR":"IRAN, ISLAMIC REPUBLIC OF",
# "CG":"CONGO",
# "SM":"SAN MARINO",
# "NA":"NAMIBIA",
# "CI":"COTE D'IVOIRE",
# "GL":"GREENLAND",
# "VE":"VENEZUELA, BOLIVARIAN REPUBLIC OF",
# "VG":"VIRGIN ISLANDS, BRITISH",
# "BH":"BAHRAIN",
# "ZM":"ZAMBIA",
# "HR":"CROATIA",
# "MZ":"MOZAMBIQUE",
# "KW":"KUWAIT",
# "MA":"MOROCCO",
# "DZ":"ALGERIA",
# "AQ":"ANTARCTICA",
# "AU":"AUSTRALIA",
# "PN":"PITCAIRN",
# "QA":"QATAR",
# "AL":"ALBANIA",
# "BN":"BRUNEI DARUSSALAM",
# "NZ":"NEW ZEALAND",
# "SA":"SAUDI ARABIA",
# "RE":"REUNION",
# "HK":"HONG KONG",
# "CD":"CONGO, THE DEMOCRATIC REPUBLIC OF THE",
# "MW":"MALAWI",
# "CZ":"CZECH REPUBLIC",
# "DE":"GERMANY",
# "AD":"ANDORRA",
# "LU":"LUXEMBOURG",
# "CY":"CYPRUS",
# "TO":"TONGA",
# "FJ":"FIJI",
# "GT":"GUATEMALA",
# "LV":"LATVIA",
# "ES":"SPAIN",
# "SI":"SLOVENIA",
# "IM":"ISLE OF MAN",
# "BS":"BAHAMAS",
# "RS":"SERBIA",
# "WS":"SAMOA",
# "NC":"NEW CALEDONIA",
# "SY":"SYRIAN ARAB REPUBLIC",
# "MS":"MONTSERRAT",
# "GB":"UNITED KINGDOM",
# "PM":"SAINT PIERRE AND MIQUELON",
# "CL":"CHILE",
# "MF":"SAINT MARTIN",
# "SO":"SOMALIA",
# "BJ":"BENIN",
# "YE":"YEMEN",
# "TV":"TUVALU",
# "GE":"GEORGIA",
# "BM":"BERMUDA",
# "GS":"SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
# "AN":"NETHERLANDS ANTILLES",
# "BY":"BELARUS",
# "FI":"FINLAND",
# "BV":"BOUVET ISLAND",
# "LR":"LIBERIA",
# "KH":"CAMBODIA",
# "LY":"LIBYAN ARAB JAMAHIRIYA",
# "MU":"MAURITIUS",
# "GU":"GUAM",
# "ER":"ERITREA",
# "LI":"LIECHTENSTEIN",
# "SD":"SUDAN",
# "PA":"PANAMA",
# "IL":"ISRAEL",
# "EH":"WESTERN SAHARA",
# "KE":"KENYA",
# "CC":"COCOS (KEELING) ISLANDS",
# "IS":"ICELAND",
# "GF":"FRENCH GUIANA",
# "MM":"MYANMAR",
# "HT":"HAITI",
# "NF":"NORFOLK ISLAND",
# "ML":"MALI",
# "PY":"PARAGUAY",
# "KZ":"KAZAKHSTAN",
# "CH":"SWITZERLAND",
# "BA":"BOSNIA AND HERZEGOVINA",
# "BO":"BOLIVIA, PLURINATIONAL STATE OF",
# "UA":"UKRAINE",
# "BL":"SAINT BARTHELEMY",
# "AZ":"AZERBAIJAN",
# "BT":"BHUTAN",
# "VA":"HOLY SEE (VATICAN CITY STATE)",
# "PE":"PERU",
# "AR":"ARGENTINA",
# "TK":"TOKELAU",
# "AG":"ANTIGUA AND BARBUDA",
# "KN":"SAINT KITTS AND NEVIS",
# "PS":"PALESTINIAN TERRITORY, OCCUPIED",
# "ID":"INDONESIA",
# "GW":"GUINEA-BISSAU",
# "HN":"HONDURAS",
# "NG":"NIGERIA",
# "IQ":"IRAQ",
# "JM":"JAMAICA",
# "NU":"NIUE",
# "ET":"ETHIOPIA",
# "ME":"MONTENEGRO",
# "SK":"SLOVAKIA",
# "YT":"MAYOTTE"
# }
# # d1=sorted(country.items(),  key=lambda x:x[0])
# # print(d1)
#
# #CHALLENGE 8: Find the country which has the longest name.
# max_length = 0
# longest_country = ""
#
# for name in country.values():
#     if len(name) > max_length:
#         max_length = len(name)
#         longest_country = name
# print(f'Thus, the countries with longest name: {longest_country} with  char length of : {max_length}')

#CHALLENGE-9:
# Consider the following two Python Lists that save information about company sales for the last 6 years:
# years = [2015, 2016, 2017, 2018, 2019, 2020]
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# Create a new list that connects the year to the corresponding sales.
# The resulting list should be: [(2015, 350000), (2016, 400000), (2017, 410000), (2018, 439000), (2019, 500000), (2020, 290000)]
# years_sales=list(zip(years,sales))
# print(years_sales)


#CHALLENGE 10:  CREATE A DICT FOR THE SAME PROBLEM
# years_sales=dict(zip(years,sales))

#CHALLENGE 11: Consider the dictionary from the previous challenge.
# Create a new dictionary called profit that stores the profit of the company, if the profit margin is 25% of the sales.
# Use dictionary comprehension if possible.
# profit={k:v*0.25 for k,v in years_sales.items()}
# print(profit)

#CHALLENGE 12:
# Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].
# Create a set that contains the elements of the 2 lists in pairs.
# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}

# names = ["Dan", "John", "Diana"]
# phones = [11111, 2222, 3333]
# names_phones=zip(names,phones)
# result=set(names_phones)
# print(result)

#CHALLENGE- 13 : intersection

#CHALLENGE- 14:Write a Python script that validates an email address by writing "Valid email!" or "Invalid email!".
# If the email is not valid the script should display why it's not valid.
# We consider a valid email address if:
# it has at least 6 characters but no more than 16.
# it contains both . and @
# it does not contain any of the following characters:'[]{}()$*'
x=input('Enter email address: ')
special_chars='.@'
def valid():
        if len(x)<=6:
            print('YOUR ADDRESS IS SHORTER THAN MINIMUM REQUIRED CHARACTERS :6')
        if len(x)>=16:
            print('YOUR ADDRESS IS GREATER THAN MAX PERMISSIBLE CHARACTERS :16')


