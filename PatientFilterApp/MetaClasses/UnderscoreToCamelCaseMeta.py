class UnderscoreToCamelCaseMeta(type):
    def __new__(cls, name, bases, dct):
        modified_items = {}

        for key, value in dct.items():
            if key.startswith('__') and key.endswith('__'):
                modified_items[key] = value
            elif ('_' in key and (callable(value) or isinstance(value, (classmethod, staticmethod)))):
                parts = key.split('_')
                camel_case_name = parts[0] + ''.join(word.capitalize() for word in parts[1:])
                modified_items[camel_case_name] = value
            else:
                modified_items[key] = value

        return super().__new__(cls, name, bases, modified_items)