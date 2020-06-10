from googletrans import Translator

sentence=raw_input("enter a phrase:")
trans=Translator()
sent=raw_input("enter a language:")
if sent =='english':
    sent ='en'
elif sent =='french':
    sent ='fr'    
translating=trans.translate(sentence,src='rw',dest=sent)
print(translating.text)