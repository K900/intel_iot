def combine(base, *others):
    result = base.copy()
    for d in others:
        result.update(d)
    return result
