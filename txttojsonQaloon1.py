import io
import re
import json

coranInJsonFormat= {}
coranInJsonFormat["السور"]=[]
surahsInJson=coranInJsonFormat["السور"]

filename='UthmanicQaloon1 Ver05'
surahSpliter='سُورَةُ'
sahSpliter='ۖ'

with io.open('./coran_txt/'+filename+'.txt','r',encoding='utf16') as f:
    text = f.read()
    surahs = text.split(surahSpliter)
    surahs = surahs[1:]
# process Unicode text
for index in range(len(surahs)):
#for surah in surahs [1:]:
    surah=surahs[index]
    lines=(surah).split('\n')
    surahName=lines[0]
    ayat=' '.join(lines[1:])
    ayatSplitedByNumbers=re.split(r'\d+', ayat)
    ayatSplitedBySah=ayat.split(sahSpliter)
   # coranInJsonFormat=coranInJsonFormat+'{ "رقم السورة":'+
    surahsInJson.append({
        
        "رقم السورة":index+1,
        "السورة": surahName,
        "الآيات بالترقيم":ayatSplitedByNumbers,
        "الآيات بالوقف ":ayatSplitedBySah })

with open('./coran_json/'+filename+'.json','w',encoding='utf16') as jsonFile:
    json.dump(coranInJsonFormat, jsonFile, sort_keys = True, indent = 4,ensure_ascii=False)


coranInJsonFormat= {}
coranInJsonFormat["السور"]=[]
surahsInJson=coranInJsonFormat["السور"]
filename='UthmanicWarsh1 Ver05'
surahSpliter='سُورَةُ'
sahSpliter='ۖ'

with io.open('./coran_txt/'+filename+'.txt','r',encoding='utf16') as f:
    text = f.read()
    surahs = text.split(surahSpliter)
    surahs = surahs[1:]
# process Unicode text
for index in range(len(surahs)):
#for surah in surahs [1:]:
    surah=surahs[index]
    lines=(surah).split('\n')
    surahName=lines[0]
    ayat=' '.join(lines[1:])
    ayatSplitedByNumbers=re.split(r'\d+', ayat)
    ayatSplitedBySah=ayat.split(sahSpliter)
   # coranInJsonFormat=coranInJsonFormat+'{ "رقم السورة":'+
    surahsInJson.append({
        
        "رقم السورة":index+1,
        "السورة": surahName,
        "الآيات بالترقيم":ayatSplitedByNumbers,
        "الآيات بالوقف ":ayatSplitedBySah })

with open('./coran_json/'+filename+'.json','w',encoding='utf16') as jsonFile:
    json.dump(coranInJsonFormat, jsonFile, sort_keys = True, indent = 4,ensure_ascii=False)


  