import pandas as pd
import difflib

class Faq:

    def __init__(self):
        
        self.faq = pd.read_csv("./data/faq.csv")

    #### SETTER and GETTER####

    def add_faq(self, faq):

        if len(faq) < 2:
            return "Error missing arguments"

        trigger = faq[0]; answer = faq[1]
        
        self.faq.loc[len(self.faq.index)] = [trigger, answer] 

        self.faq.to_csv("./data/faq.csv", index = False, mode='w+')


    def get_faq(self, pagination):
        start = pagination * 5
        end = start + 5
        data = "**Page " + str(pagination) + "**\n\n"

        if end < len(self.faq):
            page = self.faq[start:end]

        elif start < len(self.faq):
            page = self.faq[start:len(self.faq)]

        else:
            return data + "Page not found"
        
        for i in range(len(page)):
            data += "**Question:** " + page.trigger[start + i] + "\n**Answer:** " +  page.answer[start + i] + "\n"
        
        return data

    def remove(self, word):
        self.faq = self.faq[self.faq.trigger != word]
        self.faq.to_csv("./data/faq.csv", index = False, mode='w+')


    #### LISTENER ####
  
    def get_answer(self, question):

        
        question = question.replace("how", "").replace("what", "").replace("where", "").replace("?", "")
        
        answer = difflib.get_close_matches(question, self.faq.trigger.values.tolist())
        if len(answer) > 0:
            return "Here a possible answer:", self.faq.loc[self.faq.trigger == answer[0]].answer.item()
        
        
         
        

        
