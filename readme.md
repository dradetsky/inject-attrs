inject_attrs: dep injection into attrs classes
==============================================

a quick hack around the problem that I want to do dependency injection
like

```python
class Thing:
    @inject
    def __init__(self, cfg: Config, some_dep: SomeClass):
        self.cfg = cfg
        self.some_dep = some_dep
```

But I'd also like to use `attrs` which allows you to write cool stuff
like

```python
@attr.s(auto_attribs=True)
class Thing:
    cfg: Config
    some_dep: SomeClass
```

Which works fine for manually constructing instances of `Thing`, but
breaks down when you attempt to do dependency injection with `Thing`,
since attrs does not annotate its auto-generated `__init__` method.

So now I just write

```python
@inject_attr.s()
class Thing:
    cfg: Config
    some_dep: SomeClass
    
inj = Injector()
t = inj.get(Thing)

t.cfg       # => <Config obj>
t.some_dep  # => <SomeClass obj>
```

\m/
