_MATERIALS_DENSITIES = {
    'Concrete': 2500,
    'Brick': 2000,
    'Stone': 1600,
    'Wood': 600,
    'Steel': 7700,
}

class Material:
    """Base class for materials with mass and density."""

    _DENSITY = 1

    def __init__(self, mass):
        """Initialize the material with a given mass."""
        self.mass = mass
        self._is_valid = True

    @property
    def volume(self):
        """Calculate the volume of the material."""
        return self.mass / self._DENSITY

    def validate(self):
        """Check if the material is still valid for use."""
        if not self._is_valid:
            raise AssertionError('Not valid material found.')
        
    def invalidate(self):
        """Mark the material as invalid."""
        self._is_valid = False
        
    def get_base_materials(self):
        return [type(self).__name__]


class Concrete(Material):
    """Concrete material with predefined density."""
    _DENSITY = _MATERIALS_DENSITIES['Concrete']


class Brick(Material):
    """Brick material with predefined density."""
    _DENSITY = _MATERIALS_DENSITIES['Brick']


class Stone(Material):
    """Stone material with predefined density."""
    _DENSITY = _MATERIALS_DENSITIES['Stone']


class Wood(Material):
    """Wood material with predefined density."""
    _DENSITY = _MATERIALS_DENSITIES['Wood']


class Steel(Material):
    """Steel material with predefined density."""
    _DENSITY = _MATERIALS_DENSITIES['Steel']


class Factory:
    """Create and manage materials and alloys."""

    _MATERIALS_CREATED = {
        'Concrete': Concrete,
        'Brick': Brick,
        'Stone': Stone,
        'Wood': Wood,
        'Steel': Steel,
    }

    all_created_materials = []

    def __init__(self):
        self.materials_created_by_instance = []

    def __call__(self, *args, **kwargs):
        """Enable the factory instance to be called."""
        if args and kwargs:
            raise ValueError('One type of arguments are allowed.')
        elif (len(args), len(kwargs)) == (0, 0):
            raise ValueError('No arguments found.')

        if len(args) > 0:
            return self.positional_call(*args)
        return self.keyword_call(**kwargs)

    def positional_call(self, *args):
        """Handle creation of alloys from positional arguments."""

        for material in args:
            material.validate()
    
        for material in args:
            material.invalidate()

        base_materials = []
        for material in args:
                base_materials.extend(material.get_base_materials())

        unique_base_materials = sorted(set(base_materials))

        alloy_name = '_'.join(unique_base_materials)
        alloy_density = sum(_MATERIALS_DENSITIES[material] for material in unique_base_materials) / len(unique_base_materials)
        alloy_mass = sum(material.mass for material in args)

        if alloy_name in self._MATERIALS_CREATED:
            alloy_class = self._MATERIALS_CREATED[alloy_name]
        else:
            alloy_class = self.create_alloy_class(alloy_name, alloy_density, unique_base_materials)
            
        alloy_instance = alloy_class(alloy_mass)
        self.materials_created_by_instance.append(alloy_instance)
        Factory.all_created_materials.append(alloy_instance)

        return alloy_instance

    def create_alloy_class(self, alloy_name, alloy_density, base_materials):
        """Dynamically create a class for an alloy."""
        
        alloy_class = type(
            alloy_name,
            (Material,),
            {
                '_DENSITY': alloy_density,
                '_base_materials': base_materials,
                'get_base_materials': lambda self: base_materials,
            }
        )

        self._MATERIALS_CREATED[alloy_name] = alloy_class
        _MATERIALS_DENSITIES[alloy_name] = alloy_density
        return alloy_class

    def keyword_call(self, **kwargs):
        """Handle creation of materials from keyword arguments."""
        material_instances = []
        for material, mass in kwargs.items():
            if material not in self._MATERIALS_CREATED:
                raise ValueError('Not valid material found.')

            material_instance = self._MATERIALS_CREATED[material](mass)
            material_instances.append(material_instance)
            self.materials_created_by_instance.append(material_instance) 
            self.all_created_materials.append(material_instance)

        return tuple(material_instances)

    def can_build(self, target):
        """Check if the factory's materials can build a wall of target volume."""
        valid_materials = [
            material for material in self.materials_created_by_instance if material._is_valid
        ]
        
        volume_sum = sum(material.volume for material in valid_materials)
        return volume_sum >= target

    @classmethod
    def can_build_together(cls, target):
        """Check if all factories together can build a wall of target volume."""
        valid_materials = [
            material for material in cls.all_created_materials if material._is_valid
        ]
        
        used_materials = set(
            material for material in cls.all_created_materials if not material._is_valid
        )
       
        final_valid_materials = [material for material in valid_materials if material not in used_materials]
        total_volume = sum(material.volume for material in final_valid_materials)
        return total_volume >= target
