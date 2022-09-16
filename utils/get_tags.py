def tag_list(obj):
    return u", ".join(o.name for o in obj.tags.all())