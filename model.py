import argparse
import pickle

class Model():
   
    def __init__(self, input_filename, model_filename):
        self.input_filename = input_filename
        self.model_filename = model_filename
        self.dict = dict()
        self.prepared_input = ''

    def load(self):
        input_file = open(self.input_filename, 'r', encoding = 'utf-8')
        self.input_data = input_file.read()
        input_file.close()

# Очистить тексты: выкидывать неалфавитные символы, приводить к lowercase.
    def prepare_input_data(self):
        for character in self.input_data:
            if character.isalpha() or character == ' ' or character == '\n':
                self.prepared_input += character
        self.prepared_input = self.prepared_input.lower()            

# Разбить тексты на слова (в ML это называется токенизацией).
    def tokenize(self):
        self.tokens = self.prepared_input.split()

# Приводит модель к формату
    def format(self):
        for i in range(len(self.tokens) - 1):
            if self.tokens[i] not in self.dict:
                self.dict[self.tokens[i]] = [self.tokens[i + 1]]
            else:
                self.dict[self.tokens[i]].append(self.tokens[i + 1])
        self.dict[self.tokens[-1]] = []

# Сохранить модель
    def save(self):
        with open(self.model_filename, 'wb') as f:
            pickle.dump(self.dict, f)
        


if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename', type=str)
    parser.add_argument('model_filename', type=str)
    args = parser.parse_args()

    model = Model(args.input_filename, args.model_filename)
    model.load()
    model.prepare_input_data()
    model.tokenize()
    model.format()
    model.save()