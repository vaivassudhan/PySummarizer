from gensim.summarization.summarizer import summarize 
from gensim.summarization import keywords 
import wikipedia 

# Get wiki content. 
wikisearch = wikipedia.page("A R Rahman") 
wikicontent = wikisearch.content 
# nlp = en_core_web_sm.load() 
# doc = nlp(wikicontent) 
# wikicontent="""
# There are times when the night sky glows with bands of color. The bands may begin as cloud shapes and then spread into a great arc across the entire sky.
# They may fall in folds like a curtain drawn across the heavens. The lights usually grow brighter, then suddenly dim. During this time the sky glows with pale yellow, pink, green, violet, blue, and red. 
# These lights are called the Aurora Borealis. Some people call them the Northern Lights. Scientists have been watching them for hundreds of years. They are not quite sure what causes them. In ancient times
# people were afraid of the Lights. They imagined that they saw fiery dragons in the sky. Some even concluded that the heavens were on fire.
# """
# Save the wiki content to a file 
# (for reference). 
# f = open("wikicontent.txt", "w") 
# f.write(wikicontent) 
# f.close() 

# Summary (0.5% of the original content). 
summ_per = summarize(wikicontent, ratio = 0.05) 
print("Percent summary") 
print(summ_per) 

# Summary (200 words) 
summ_words = summarize(wikicontent, word_count = 200) 
print("Word count summary") 
print(summ_words) 

