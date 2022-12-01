class DayFactory:

    @staticmethod
    def my_import(day):
        path = f'solution.day{day}.Day{day}'

        parts = path.split('.')
        module_name = ".".join(parts[:-1])
        module = __import__(module_name)

        for component in parts[1:]:
            module = getattr(module, component)
        return module

    def __init__(self, day, *args):
        module = self.my_import(day)
        print(f'Day {day}')
        module(args).solution()
