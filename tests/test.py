import json

class Exam:
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name

    @property
    def questions(self):
        with open(self.file_name) as file:
            data = json.load(file)
            return data["questions"]
        
if __name__ == '__main__':
    import unittest

    class Test_test(unittest.TestCase):

        def setUp(self) -> None:
            self.test_1 = Exam("test_questions.json")

        def test_read_questions(self):
            self.assertEqual(self.test_1.questions, [
            {
                "q": "kwargs?",
                "a": "kwargs",
                "options": [],
                "family": "pcap",
                "subject": "functions"
            },
            {
                "q": "kwargs?",
                "a": "kwargs",
                "options": ["kwargs", "args", "algo más"],
                "family": "pcap",
                "subject": "functions"
            }
            ])
        
        def test_get_sample(self):
            self.assertEqual(self.test_1.get_sample(), "")

    unittest.main()