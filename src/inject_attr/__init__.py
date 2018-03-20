__all__ = [
    'inject_attrs',
    's'
]

from attr import attrs
from typing import get_type_hints

from injector import inject

def annotate_init(cls):
    init = cls.__init__
    init_arg_names = init.__code__.co_varnames
    hints = get_type_hints(cls)
    for name in init_arg_names:
        if name in hints:
            set_hint(init, name, hints[name])

    return cls

def set_hint(obj, name, val):
    obj.__annotations__[name] = val

def inject_init(cls):
    cls.__init__ = inject(cls.__init__)

    return cls

def inject_attrs(*args, **kwargs):
    """
    for dep injection into attrs classes

    NOTE(dmr, 2018-03-20): couldn't be bothered to figure out how to
    do flexible class decorators, so you hafta write

    @inject_attr.s()
    class Thing:
        ...

    even though if there are no args, it should be

    @inject_attr.s
    class Thing:
        ...
    """
    def wrap(cls):
        attrs_fn = attrs(auto_attribs=True, *args, **kwargs)

        attr_cls = attrs_fn(cls)
        anno_attr_cls = annotate_init(attr_cls)
        inj_cls = inject_init(anno_attr_cls)
        return inj_cls

    return wrap

s = inject_attrs
