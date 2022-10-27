from multiprocessing import Process
import multiprocessing
import os
import random
from typing import List
from RandomWordGenerator import RandomWord
from file_analytics_class import FileAnalytics

def create_file(process_index):
    word_count = random.randint(100_000, 5_000_000)
    file_name = f"Process-{process_index + 1}-{os.getpid()}.txt"
    
    with open(file_name, 'w') as file:
        for i in range(word_count):
            word :RandomWord = RandomWord(constant_word_size=False)
            file.write(word.generate() + '\n')
    
    analytics = FileAnalytics(file_name)
    analytics.get_analytics()

if __name__ == '__main__':
    list_process :List[Process] = []

    for i in range(multiprocessing.cpu_count()):
        p :Process = Process(target=create_file, args = (i,))
        p.start()
        list_process.append(p)

    [process.join() for process in list_process]