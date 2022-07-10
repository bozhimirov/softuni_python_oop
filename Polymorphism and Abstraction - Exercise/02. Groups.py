from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f'{self.name} {other.name}'
        merged_members = self.people + other.people
        return Group(new_name, merged_members)

    def __str__(self):
        people_str = ', '.join([str(x) for x in self.people])
        return f'Group {self.name} with members {people_str}'

    def __getitem__(self, idx):
        return f'Person {idx}: {str(self.people[idx])}'
