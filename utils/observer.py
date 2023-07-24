# Observer Design Pattern

suscribers = dict()

def suscribe(event_type: str, fn):
    if not event_type in suscribers:
        suscribers[event_type] = []
    suscribers[event_type].append(fn)

def post_event(event_type: str, data):
    if not event_type in suscribers:
        return
    for fn in suscribers[event_type]:
        fn(data)