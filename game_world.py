objects = [[] for _ in range(4)]

collision_pairs = {}

def add_object(o, depth = 0):
    objects[depth].append(o)


def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def add_collision_pair(group, a, b):
    pass


def remove_collision_objects(o):
    pass


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_objects(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()


def collide(a, b):
    pass