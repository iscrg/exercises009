class TrafficLight:
    permissible_values = [
        'красный',
        'желтый',
        'зеленый'
    ]

    def __init__(self):
        self.current_signal = self.permissible_values[0]

    def next_signal(self):
        """
        Turn on the next signal.
        :return: None
        """
        signal_index = self.permissible_values.index(self.current_signal)
        signal_index = (signal_index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[signal_index]


tl = TrafficLight()
print(tl.permissible_values)
print(tl.current_signal)
for _ in range(5):
    tl.next_signal()
    print(tl.current_signal)
