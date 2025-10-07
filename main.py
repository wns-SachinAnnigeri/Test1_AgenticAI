# ...existing code...

from abc import ABC, abstractmethod

# Task interface
class Task(ABC):
	@abstractmethod
	def execute(self, agent, environment):
		pass

# Calculator Environment
class CalculatorEnvironment:
	def __init__(self):
		self.last_result = 0

	def update_result(self, result):
		self.last_result = result

# Agent class
class CalculatorAgent:
	def __init__(self, name):
		self.name = name

	def perceive(self, environment):
		return environment.last_result

	def decide(self, task, environment):
		return task.execute(self, environment)

	def act(self, result, environment):
		environment.update_result(result)

# Concrete Tasks
class AddTask(Task):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def execute(self, agent, environment):
		return self.a + self.b

class SubtractTask(Task):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def execute(self, agent, environment):
		return self.a - self.b

class MultiplyTask(Task):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def execute(self, agent, environment):
		return self.a * self.b


class DivideTask(Task):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self, agent, environment):
        if self.b == 0:
            return 'Error: Division by zero'
        return self.a / self.b



if __name__ == "__main__":
    env = CalculatorEnvironment()
    agent = CalculatorAgent("CalcAgent")

    tasks = [
        AddTask(5, 3),
        SubtractTask(10, 4),
        MultiplyTask(2, 7),
        DivideTask(20, 5),
        DivideTask(10, 0),  # Division by zero test
    ]

    for i, task in enumerate(tasks, 1):
        print(f"\nTask {i}: {task.__class__.__name__}")
        last_result = agent.perceive(env)
        print(f"Agent perceives last result: {last_result}")
        result = agent.decide(task, env)
        print(f"Agent decides result: {result}")
        agent.act(result, env)
        print(f"Environment updated. New last result: {env.last_result}")

# ...existing code...
