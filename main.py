import matplotlib.pyplot as plt
import json
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

FontPath = "/usr/share/fonts/truetype/BigBlueTerm437NerdFontMono-Regular.ttf"
BannedWords = ["nie", "jak", "ale", "bo", "kurwa", "tak", "na", "ja", "że", "ze", "z", "sie", "co", "mam", "jest", "mi", ]

def get_tg_msgs_str(searched_user = ""):
    total_str = ""
    with open("./result.json", 'r') as file:
        tg_data = json.load(file)
        chat_list = tg_data["chats"]["list"]
        for chat in chat_list:
            # If user was specified, check
            # Process the messages
            messages = chat["messages"]
            for msg in messages:
                # TODO only searches the from but not the other side
                if "from" in msg:
                    if searched_user != "":
                        if msg["from"] != searched_user:
                            continue
                if "text_entities" in msg and len(msg["text_entities"]):
                    # For now only takes in the first text entity
                    text_entity = msg["text_entities"][0]
                    if "text" in text_entity:
                        msg_split = text_entity["text"].split()
                        for word in msg_split:
                            if word not in BannedWords:
                                total_str += word + " "
    return total_str

def make_word_cloud_from_str(tg_str):
    cloud = WordCloud(width=1000, height=800).generate(tg_str)

    # Show the wordcloud
    plt.imshow(cloud,interpolation='bilinear')
    plt.axis("off")
    plt.show()  

tg_str = get_tg_msgs_str("Nyczu")
make_word_cloud_from_str(tg_str)
