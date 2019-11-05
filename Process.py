import re
from pyvi import ViTokenizer

def remove_special_text(text):
    tokens = re.sub(r'(http\S+)|(@\S+)|RT|\#|\?|:|\.|[0-9]|[!@#$%^&*()-+<>{}]|,', ' ', text)
    return tokens

#viet tat
def acronym_text(text):
    text = text.replace("ko", "không")
    text = text.replace("k0", "không")
    text = text.replace("bt", "bình thường")
    text = text.replace("ng0n", "ngon")
    text = text.replace("vn", "việt nam")
    text = text.replace("lsau", "lần sau")
    return text
#lay am
#...

input_file = './data/rate0_data.csv'
output_file = "./data/rate0_data_output.csv"

def process_dataset(input_file, output_file):
    data = open(input_file,encoding="utf8").read().split('\n')
    print("input length:", len(data))
    str_file = "Rate,Review,Label\n"
    check = True
    for line in data:
        if check == True:
            check = False
            continue
        item = line.split(",")
        #print(item[1])
        tokens = pre_process(item[1])
        #print(tokens)
        str_file += item[0] + "," + tokens + "," + item[2] + "\n"
        print(str_file)

    # write data
    text_file = open(output_file, "w", encoding="utf-8")
    text_file.write(str_file)
    text_file.close()
comment = "Hôm quan đi siêu set hơn chưa mang đc mang đc Ăn lâu ngang ngang ăn lâu đi lsau quay"

def pre_process(comment):
    comment = remove_special_text(comment).lower()
    comment = acronym_text(comment)
    #tach tu
    comment = ViTokenizer.tokenize(comment)
    return comment

#print(pre_process(comment))
#process_dataset(input_file, output_file)