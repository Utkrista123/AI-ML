import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.api.types import EmbeddingFunction

model = SentenceTransformer("intfloat/multilingual-e5-base")

class E5EmbeddingFunction(EmbeddingFunction):
    def __inti__(self, model):
        self.model = model

    def __call__(self, input):
        inputs = ["passage: " + text for text in input]
        return model.encode(inputs).tolist()
    
    def name(self):
        return "e5-custom"
        
client = chromadb.PersistentClient(path="./chroma_multi_db")

collection = client.get_or_create_collection(
    name = "law",
    embedding_function = E5EmbeddingFunction(model)
)

documents = [
    '''1. Constitution as Fundamental Law: (1) This Constitution
    is the fundamental law of Nepal. Any law inconsistent
    with this Constitution shall, to the extent of such
    inconsistency, be void.
    (2) It shall be the duty of every person to uphold
    this Constitution.''',

    '''2. Sovereignty and State Power: The sovereignty and State
    power of Nepal shall be vested in the Nepali people. It
    shall be exercised in accordance with the provisions set
    forth in this Constitution.''',

    '''Nation: All the Nepali people, with multi-ethnic, multilingual, multi-religious, multi-cultural characteristics and
    in geographical diversities, and having common
    aspirations and being united by a bond of allegiance to
    national independence, territorial integrity, national
    interest and prosperity of Nepal, collectively constitute
    the nation.''',

    '''4. State of Nepal: (1) Nepal is an independent, indivisible,
    sovereign, secular, inclusive, democratic, socialismoriented, federal democratic republican State.
    Explanation: For the purposes of this Article,
    "secular" means religious, cultural freedoms, including
    protection of religion and culture handed down from
    time immemorial.
    (2) The territory of Nepal shall comprise the
    following:-
    (a) The territory existing at the time of
    commencement of this Constitution, and
    (4)
    (b) Such other territory as may be acquired
    after the commencement of this
    Constitution.''',

    '''5. National Interest: (1) Safeguarding of the freedom,
    sovereignty, territorial integrity, nationality,
    independence and dignity of Nepal, the rights of the
    Nepali people, border security, economic wellbeing and
    prosperity shall be the basic elements of the national
    interest of Nepal.
    (2) Any conduct and act contrary to the national
    interest shall be punishable in accordance with the
    federal law.''',

    '''6. Languages of Nation: All languages spoken as the mother
    tongues in Nepal are the languages of the nation.''',

    '''7. Official Language: (1) The Nepali language in the
    Devnagari script shall be the official language of Nepal.
    (2) A Province may, by a provincial law,
    determine one or more than one languages of the nation
    spoken by a majority of people within the Province as its
    official language or languages, in addition to the Nepali
    language.
    (3) Other matters relating to language shall be as
    decided by the Government of Nepal on recommendation
    of the Language Commission.''',

    '''8. National Flag: (1) The national flag of Nepal consists of
    two juxtaposed triangular figures with a crimsoncoloured base and deep blue borders, there being a white
    emblem of the crescent moon with eight rays visible out
    of sixteen in the upper part and a white emblem of a
    twelve rayed sun in the lower part.
    (5)
    (2) The method of drawing out the flag and other
    particulars relating thereto shall be as provided for in
    Schedule-1.''',

    '''9. National Anthem and so on: (1) The national anthem of
    Nepal shall be as set forth in Schedule-2.
    (2) The coat-of-arms of Nepal shall be as set
    forth in Schedule-3.
    (3) The Rhododendron Arboreum shall be the
    national flower, Crimson Colour shall be the national
    colour, Cow shall be the national animal and
    Lophophorus shall be the national bird of Nepal.''',

]

metadatas = [
    {"source": "constitution", "article_number": "1", "language": "en"},
    {"source": "constitution", "article_number": "2", "language": "en"},
    {"source": "constitution", "article_number": "3", "language": "en"},
    {"source": "constitution", "article_number": "4", "language": "en"},
    {"source": "constitution", "article_number": "5", "language": "en"},
    {"source": "constitution", "article_number": "6", "language": "en"},
    {"source": "constitution", "article_number": "7", "language": "en"},
    {"source": "constitution", "article_number": "8", "language": "en"},
    {"source": "constitution", "article_number": "9", "language": "en"},
]

ids = [str(i) for i in range(1, len(documents) + 1)]

collection.add(
    documents = documents,
    metadatas = metadatas,
    ids = ids
)

query_result = collection.query(
    query_texts=["query: what is the offical language of nepal"],
    n_results=1
)

for doc, meta in zip(query_result["documents"][0], query_result["metadatas"][0]):
    print(f"{doc} article_number: {meta ["article_number"]}, language: {meta ["language"]}")
