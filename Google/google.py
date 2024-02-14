from deep_translator import GoogleTranslator

t=GoogleTranslator(source='vi', target='en')
a=t.translate("em đẹp quá")

print(a.type())
