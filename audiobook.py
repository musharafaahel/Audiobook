#Importing python text to speech version 3
import pyttsx3
#Importing python PDF to reader
import PyPDF2
#Give location 
book = open('oop_java.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
Pages = pdfReader.numPages
print('Number of Pages in this document :', Pages)
speaker = pyttsx3.init()
#for num in range(1, Pages):
page = pdfReader.getPage(10)
text = page.extractText()
speaker.say("Welcome to Musharaf Aahel's Audiobook" )
speaker.say(text)
speaker.say("Thanks for using Musharaf Aahel's Audiobook" )
speaker.runAndWait()