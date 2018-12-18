from dan_almog_project import *

print(index_of_text)
print(new_text)
def micro_service_bolt(text,list_of_indexses):
    new_list_text = text.split()
    print(new_text)
    for i in range(0, len(list_of_indexses)):
        word = new_list_text[list_of_indexses[i]]
        tmp_word = list(word)
        print tmp_word
        for w in tmp_word:
            if w == 'o':
                index = tmp_word.index(w)
                tmp_word[index] = color.BLUE + w + color.END

    str2 = ''.join(tmp_word)
    return str2


print(micro_service_bolt(new_text,index_of_text))