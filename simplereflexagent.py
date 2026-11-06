class SimpleReflexAgent:
    def __init__(self):
        self.c_t = None
        self.occupied = False
        self.previous_mode = None  # Task 3 addition

    def sensor(self, current_temp, occupied):
        self.c_t = current_temp
        self.occupied = occupied

    def act(self):
        # 1. Determine the target mode.
        if not self.occupied:
            target_mode = "ECO"
        elif self.c_t > 26:
            target_mode = "COOL"
        elif self.c_t < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        # 2. Avoid repeating an identical command.
        if target_mode == self.previous_mode:
            command_sent = False
        else:
            command_sent = True
            self.previous_mode = target_mode

        return target_mode, command_sent


agent = SimpleReflexAgent()

percepts = [(29, True), (29, True), (20, True),
            (26, True), (19, True), (29, False)]

print("Percept | Previous Mode | Target Mode | Send Command?")
print("-" * 58)

for temp, occupied in percepts:
    previous_mode = agent.previous_mode
    agent.sensor(temp, occupied)
    target_mode, command_sent = agent.act()

    print(f"{(temp, occupied)} | {previous_mode} | "
          f"{target_mode} | {command_sent}")
