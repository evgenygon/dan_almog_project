

x = "ariel a hamniak kol  ose balagan kol hazman"
print(x)
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   GREY = '\033[37m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# color.PURPLE + word + color.END
def under(text, *args):
     tmp = text.split()
     index_list = []
     connect_word = []
     for word in tmp:
        if word in args:
            index = tmp.index(word)
            each_char = []
            each_char = list(word)
            for each in each_char:
                connect_word.append(color.PURPLE + each + color.END)
            connect_back_all_word = ''.join(connect_word)
            tmp[index] = connect_back_all_word
            index_list.append(index)
        connect_word = [] # its empty
     connect_back_all_text = ' '.join(tmp)
     return connect_back_all_text, index_list


word_to_change = 'kol'

new_text,index_of_text = under(x,word_to_change)
print (new_text)