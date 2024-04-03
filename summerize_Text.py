import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text = '''The goal is to develop a language translator tool tailored for government organizations,providing the capability to translate English content into a specifi c language. 
          This tool is designed to enhance accessibility and usability for a wider audience. 
          The key focus is on creating a language translator for offi cial government websites, eliminating language barriers and ensuring effective communication
          Key Features:
1. **Translation Accuracy:** - The tool should off er precise translations, maintaining the context and meaning of the original content.
- It should handle nuances, idiomatic expressions, and technical terms relevant to government documents.
2. **User-Friendly Interface:**
- Ensure a simple and intuitive interface for both website administrators and end-users.
- Seamless integration into government websites, allowing users to translate content eff ortlessly.
3. **Website Integration:**
- Compatibility with various website architectures and frameworks commonly used by government organizations
- Provide developers with an API or plugin for easy integration into existing websites without extensive code modifi cations.
PROBLEM STATEMENT 3
4. **Language Preservation:**
- Design the tool to preserve cultural and linguistic nuances.
- Account for regional variations and dialects to ensure accurate translations resonating with the target audience.
5. **Security and Privacy:**
- Adhere to high-security and privacy standards, particularly considering the sensitive nature of government information.
- Ensure data protection, prevent unauthorized access, and comply with relevant privacy regulations.
6. **Scalability:**
- Build a scalable solution capable of handling a large volume of translation requests.
- Ensure smooth performance during peak usage periods and support concurrent translations across multiple websites.
Participants are encouraged to explore innovative approaches, utilizing natural language processing (NLP) techniques, machine learning algorithms, and relevant technologies to achieve accurate translations. 
The resulting language translator tool aims to signifi cantly improve the accessibility and usability of government websites, facilitating eff ective communication with a diverse audience.'''
# @app.route("/process_string", methods=["POST"])
# def process_string():
#     data = request.get_json()
#     input_string = data["string"]
    
#     # Call your Python function with the input string
#     result = summarizer(input_string)
    
#     # You can return a response to the client if needed
#     return result


def summarizer(input_string):
    stopwords = list(STOP_WORDS)
# print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(input_string)
# print(doc)
    tokens = [token.text for token in doc]
# print(tokens)
    word_frequency = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in  punctuation:
            if word.text not in word_frequency.keys():
                word_frequency[word.text] = 1
            else:
                word_frequency[word.text] += 1
# print(word_frequency)
    max_freq = max(word_frequency.values())
    for word in word_frequency.keys():
        word_frequency[word] = word_frequency[word]/max_freq
# print(word_frequency)
    sent_tokens = [sent for sent in doc.sents]
# print(sent_tokens)
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_frequency.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_frequency[word.text]
                else:
                    sent_scores[sent] += word_frequency[word.text]
# print(sent_scores)
    select_len = int(len(sent_tokens)*0.3) 
# print(select_len)
    summary = nlargest(select_len,sent_scores,key = sent_scores.get)
# print(summary) 
    final_summary = [word.text for  word in summary]
    summary = ' '.join(final_summary)
    # print(summary)
    # print(text)
    # print("Length of Original text",len(text.split(' ')))
    # print("Length of Summary text",len(summary.split(" ")))

    return summary,doc,len(input_string.split(" ")) , len(summary.split(" "))
 

result = summarizer(text)
print(result)