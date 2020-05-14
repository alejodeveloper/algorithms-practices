#!/bin/python3

class Car:
    def __init__(self, max_speed: int, speed_notation: str):
        self.max_speed = max_speed
        self.speed_notation = speed_notation

    def __str__(self):
        return f'Car with the maximum speed of {self.max_speed}' \
               f' {self.speed_notation}'
class Boat:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def __str__(self):
        return f'Boat with the maximum speed of {self.max_speed} knots'

