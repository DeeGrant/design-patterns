import copy


class SelfReferencingEntity:
    def __init__(self) -> None:
        self.parent = None

    def set_parent(self, parent) -> None:
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int: int, some_list_of_objects: list, some_circular_ref) -> None:
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo={}):
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    # Shallow Copy
    shallow_copied_component = copy.copy(component)

    # Test 1
    shallow_copied_component.some_list_of_objects.append("another object")
    if component.some_list_of_objects[-1] == "another object":
        print("Shallow list add shows up in Original's list")
    else:
        print("Shallow list add doesn't shows up in Original's list")

    # Test 2
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print("Original list add shows up in Shallow's list")
    else:
        print("Original list add doesn't shows up in Shallow's list")

    print(f"Shallow Parent ref: {shallow_copied_component.some_circular_ref.parent}")
    print(f"Parent of Shallow Parent ref: {shallow_copied_component.some_circular_ref.parent.some_circular_ref.parent}")
    print()

    # Deep Copy
    deep_copied_component = copy.deepcopy(component)

    # Test 3
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] == "one more object":
        print("Deep list add shows up in Original's list")
    else:
        print("Deep list add doesn't shows up in Original's list")

    # Test 4
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print("Original list add shows up in Deep's list")
    else:
        print("Original list add doesn't shows up in Deep's list")

    print(f"Deep Parent ref: {id(deep_copied_component.some_circular_ref.parent)}")
    print(f"Parent of Deep Parent ref: {id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}")
    print("^^ Deep contains the same reference; they are not cloned repeatedly.")
