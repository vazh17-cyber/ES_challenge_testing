import unicodedata
import re

def clean_ascii(text: str) -> str:
    #N = Normalization
    #F = Compatibility
    #K = Compatibility decomposition
    #D = Decomposition
    if text:
        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ascii", "ignore").decode("ascii")
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[...]+", ".", text)
        return text.strip()
    else:
        return ""

if __name__=="__main__":
    descrpts = [
        "Slagar the fox hated Redwall Abbey - its peaceable creatures, its fearless mouse warrior Matthias. He blamed Matthias for the injuries he'd suffered ... but his quest for vengeance would have to be a cunning one, for the knew the power of the legendary Redwall sword.\r\n\r\nAbove all, he know the Redwallers cherished their young. So Slagar would steal them from under their very noses - and the greatest prize of all would be Matthias's headstrong son, Mattimeo.",
        "“The Voyage Out”? by Virginia Woolf.\r\n\r\nThis is a story about a young English woman, Rachel, on a sea voyage from London, to a South American   coastal city of Santa Marina. As I read the story,  the title of the story became  a metaphor for Rachel's inner journey. \r\nThe inner journey within this story is perhaps best summarized in the author's words:  \r\n“The next few months passed away, as many years can pass away, without definite events, and yet, if suddenly disturbed, it would be seen that such months or years had a character unlike others.”\r\n Rachel's mother has passed away many years ago. The sea voyage and the subsequent months in Santa Marina show that Rachel is also on an inner journey, to understand herself better.  She seeks advice from Helen, her aunt,  and Helen and Rachel become close friends.\r\n“…................The vision of her own personality, of herself as a real everlasting thing, different from anything else, unmergeable, like the sea or the wind, flashed into Rachel's mind, and she became profoundly excited at the thought of living...................”\r\n\r\nRachel falls in love with a young Englishman, Terence, in Santa Marina.  But tragically, she falls ill and dies.  Yet, in the brief time that Helen and Terence have known her, her journey has also made them reflect about their own lives."
    ]
    r01 = clean_ascii(descrpts[1])
    print(r01)
