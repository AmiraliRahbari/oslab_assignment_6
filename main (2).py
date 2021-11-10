import pickle


class Translate:
    def __init__(self):
        try:
            self.data = Translate.read()
        except:
            self.data = dict()
    def add(self, new_data):
        self.data.update(new_data)

    def en_to_fa(self, word):
        for key in self.data:
             if word == key:
                 return self.data[key]
        return "not found"

    def fa_to_en(self, word):
        key_list = list(self.data.keys())
        val_list = list(self.data.values())
        try:
            position = val_list.index(word)
            return key_list[position]
        except:
            return "not found"

    def get_en_word(self, words):
        words = words.split()
        print("in persian : ", end=" ")
        if len(words) != 1:
            for word in words:
                print(self.en_to_fa(word), end=" ")


    def get_fa_word(self, words):
        words = words.split()
        print("in english : ", end=" ")
        for word in words:
            print(self.fa_to_en(word), end=" ")


    def save(self):
        try:
            geeky_file = open('data', 'wb')
            pickle.dump(self.data, geeky_file)
            geeky_file.close()

        except:
            print("Something went wrong")

    @classmethod
    def read(cls):
        with open('data', 'rb') as handle:
            data = handle.read()
        d = pickle.loads(data)

        return d



if __name__ == "__main__":
    translate = Translate()
    print("\t\t\twelcome to my Translator\n")
    while True:
        switch = int(input("\n1.add new word\n2.translation english2persian\n"
                           "3.translation persian2english\n4.exit\n\n"
                           "**********************\n"))

        if switch == 1:
            en_word = input("Enter a english word : ")
            fa_word = input(f"Enter the meaning of {en_word} in Persian : ")
            translate.add({en_word: fa_word})

        elif switch == 2:
            en_word = input("Enter your word(words) : ")
            translate.get_en_word(en_word)

        elif switch == 3:
            fa_word = input("Enter your word(words) : ")
            translate.get_fa_word(fa_word)

        elif switch == 4:
            translate.save()
            break
