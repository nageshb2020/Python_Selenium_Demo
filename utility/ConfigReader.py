from jproperties import Properties

config= Properties()
with open('configuration.properties', 'rb') as read_prop:
    config.load(read_prop)

print(config.get('URL'))
