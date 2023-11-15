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
    if group not in collision_pairs:
        collision_pairs[group] = [[], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


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


def collide_in(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    # 박스 안에 있는가?
    if la < lb and ba < bb and ra < rb and ta < tb:
        return False

    return True

def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide_in(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

    return None