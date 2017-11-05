# Dummy module to prevent import in Transcrypt of its CPython
# counterpart, that depends on several standard lib modules
class Any:
    def __init__ (self):
        pass


def ClassVar (arg):
    return arg

class Generic:
    def __init__ (self):
        pass

    @classmethod
    def __getitem__(cls):
        return cls

class Callable(Generic):
    def __init__ (self):
        pass

class Optional(Generic):
    def __init__ (self):
        pass

class Tuple(Generic):
    def __init__ (self):
        pass

class Type:
    def __init__ (self):
        pass

class TypeVar:
    def __init__ (self):
        pass

class Union(Generic):
    def __init__ (self):
        pass

class AbstractSet:
    def __init__ (self):
        pass

class GenericMeta:
    def __init__ (self):
        pass

class ByteString(Generic):
    def __init__ (self):
        pass

class Container:
    def __init__ (self):
        pass

class ContextManager:
    def __init__ (self):
        pass

class Hashable:
    def __init__ (self):
        pass

class ItemsView:
    def __init__ (self):
        pass

class Iterable(Generic):
    def __init__ (self):
        pass

class Iterator(Generic):
    def __init__ (self):
        pass

class KeysView(Generic):
    def __init__ (self):
        pass

class Mapping(Generic):
    def __init__ (self):
        pass

class MappingView(Generic):
    def __init__ (self):
        pass

class MutableMapping(Generic):
    def __init__ (self):
        pass

class MutableSequence(Generic):
    def __init__ (self):
        pass

class MutableSet(Generic):
    def __init__ (self):
        pass

class Sequence(Generic):
    def __init__ (self):
        pass

class Sized:
    def __init__ (self):
        pass

class valuesview:
    def __init__ (self):
        pass

class Reversible:
    def __init__ (self):
        pass

class SupportsAbs:
    def __init__ (self):
        pass

class SupportsBytes:
    def __init__ (self):
        pass

class SupportsComplex:
    def __init__ (self):
        pass

class SupportsFloat:
    def __init__ (self):
        pass

class SupportsInt:
    def __init__ (self):
        pass

class SupportsRound:
    def __init__ (self):
        pass

class Counter(Generic):
    def __init__ (self):
        pass

class Deque(Generic):
    def __init__ (self):
        pass

class Dict(Generic):
    def __init__ (self):
        pass

class DefaultDict(Generic):
    def __init__ (self):
        pass

class List(Generic):
    def __init__ (self):
        pass

class Set(Generic):
    def __init__ (self):
        pass

class FrozenSet(Generic):
    def __init__ (self):
        pass

class NamedTuple(Generic):
    def __init__ (self):
        pass

class Generator(Generic):
    def __init__ (self):
        pass

class AnyStr:
    def __init__ (self):
        pass

def cast (typ, val):
    return val

def get_type_hints (obj):
    return {}

def NewType (name, tp):
    def new_type (x):
        return x
    return new_type

def no_type_check (arg):
    return arg

def no_type_check_decorator (decorator):
    return decorator

def _overload_dummy ():
    raise NotImplementedError ("overloaded function called")

def overload (func):
    return _overload_dummy ()

Text = str
TYPE_CHECKING = False
