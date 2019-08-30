import argparse
import pickle
import random


class Generator():
    def __init__(self, model_filename, output_filename, text_len):
        self.model_filename = model_filename
        self.output_filename = output_filename
        self.text_len = text_len
        self.result = ''
    
    def load_model(self):
        with open(self.model_filename, 'rb') as f:
            self.dict = pickle.load(f)
    
    def generate(self):
        cur_key = random.choice(list(self.dict.keys()))
        self.result += cur_key
        while len(self.result) < self.text_len:
            if not self.dict[cur_key]:
                break

            cur_key = random.choice(self.dict[cur_key])
            self.result += ' ' + cur_key

    def save(self):
        output_file = open(self.output_filename, 'w', encoding = 'utf-8')
        output_file.write(self.result)
        output_file.close()
        
        
if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('model_filename', type=str)
    parser.add_argument('output_filename', type=str)
    parser.add_argument('text_len', type=int)
    args = parser.parse_args()
    
    generator = Generator(args.model_filename, args.output_filename, args.text_len)
    generator.load_model()
    generator.generate()
    generator.save()