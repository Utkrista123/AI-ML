documents = [''' No person shall be deprived of his 
or her personal liberty except in accordance with law. ''',

'''(2) Every citizen shall have the following 
freedoms: - 
(a) 
Freedom of opinion and expression; 
(b) Freedom to assemble peaceably and without 
arms; 
(c) 
Freedom to form political parties; 
(d) Freedom to form unions and associations; 
(e) 
Freedom to move and reside in any part of 
Nepal; 
(f) 
Freedom to practise any profession, carry on 
any occupation and establish and operate any 
industry, trade and business in any part of 
Nepal.''',

'''Nothing in sub-clause (a) shall be deemed to 
prevent the making of an Act to impose 
reasonable restrictions on any act which may 
undermine 
the 
sovereignty, 
territorial 
integrity, nationality and independence of 
Nepal or the harmonious relations between 
the Federal Units or the people of various 
castes, tribes, religions or communities or 
(9) 
incite 
caste-based 
discrimination 
or 
untouchability or on any act of disrespect of 
labour, defamation, contempt of court, 
incitement to an offence or on any act which 
may be contrary to public decency or 
morality.''']

metadata = []

for i in range(1, len(documents) + 1):
    dict = {
        "source": "Constiution",
        "article": f"Paragraph: {i}",
        "language": "en"
    }

    metadata.append(dict)

print(metadata)