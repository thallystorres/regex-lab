#Greedy vs non-greedy (or lazy)
import re

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div></div> 
'''

print(re.findall(r'<[dipv]*>.*<\/[dipv]*>', texto, flags=re.I)) #Greedy
print(re.findall(r'<[dipv]*>.+?<\/[dipv]*>', texto, flags=re.I)) #Non-greedy