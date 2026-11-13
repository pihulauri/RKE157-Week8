from utils import clean_my_list
import random


def read_data(file_path):

    # file_path = "data/heroes.txt"#Copy Relative Path

    with open(file_path, 'r', encoding='utf-8') as f: #with open sulgeb faili automaatselt peale seda, kui andmed on kätte saadud
        data = clean_my_list(f.readlines())  # Loeb faili read ja puhastab need
        random_item = random.choice(data)  # Valib juhusliku elemendi puhastatud andmete hulgast
        return random_item

        # print(random_item)  # Trükib juhusliku elemendi välja

        # print(data)  # Kontrollime, kas andmed on õigesti loetud ja puhastatud


# read_data()