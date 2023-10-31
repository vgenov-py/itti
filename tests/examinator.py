import json
from random import sample as spl, shuffle

class Examinator:
    def __init__(self, file_name:str, limit:int=15, filter_dict:dict=None) -> None:
        '''
        file_name:str=file_location
        limit:int= Limit should be an integer | None = 15
        filter:dict = {key_to_filter_with: value_to_filter} | None = None
        '''
        self.file_name = file_name
        self.limit = limit
        self.filter_dict = filter_dict

    @property
    def questions(self) -> list:
        with open(self.file_name) as file:
            data = json.load(file)
            if self.filter_dict:
                k,v = list(self.filter_dict.items())[0]
                return list(filter(lambda question: question[k] == v, data["questions"]))
            return data["questions"]

    @property    
    def sample(self) -> list:
        return spl(self.questions, self.limit)
        
    @property
    def exam(self) -> list[dict]:
        result = []
        for question in self.sample: # question = self.questions[0]
            shuffle(question["options"])
            result.append(question)
        return result


if __name__ == '__main__':
    import unittest

    class Test_test(unittest.TestCase):

        def setUp(self) -> None:
            self.test_1 = Examinator("test_questions.json", limit=2)

        def test_read_questions(self):
            self.assertEqual(type(self.test_1.questions), list)
            self.assertEqual(self.test_1.questions, [
            {
            "q": "q1",
            "a": "a",
            "options": ["1", "2", "3", "4"],
            "family": "pcap",
            "subject": "functions"
            },
            {
                "q": "q2",
                "a": "a2",
                "options": ["1", "2", "3", "4"],
                "family": "pcap",
                "subject": "functions"
            }
            ])
        
        def test_get_sample(self):
            self.assertEqual(type(self.test_1.sample), list)

        def test_exam(self):
            self.assertEqual(type(self.test_1.exam), list)

    unittest.main()