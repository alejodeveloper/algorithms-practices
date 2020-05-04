class ComparisonList:
    def __init__(self, list_a: list, list_b: list):
        self.list_a = list_a
        self.list_b = list_b

    def compare_a_b(self):
        difference = list(set(self.list_a) - set(self.list_b))
        return not len(difference) == len(self.list_a)

    def compare_b_a(self):
        difference = list(set(self.list_b) - set(self.list_a))
        return not len(difference) == len(self.list_b)

    def compare(self):
        return self.compare_a_b() and self.compare_b_a()
