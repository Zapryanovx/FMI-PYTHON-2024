
# HauntedMansion Class

This project defines the `HauntedMansion` class, which adds a Halloween-inspired twist to accessing attributes.

## Initialization

The `HauntedMansion` class is initialized with any number of named arguments, which are stored as attributes:

```python
haunted_mansion = HauntedMansion(butler="Alfred", rooms=10, basement=True)
```

## Accessing Attributes

The class restricts attribute access as follows:

1. **Spooky Prefix**: Each attribute can only be accessed with a `spooky_` prefix. For example, the `butler` attribute should be accessed as `spooky_butler`.

2. **Ghostly Message**: Attempting to access attributes without the `spooky_` prefix returns the string `"Booooo, only ghosts here!"`.

3. **Dynamic Attributes**: Dynamically added attributes also follow the same spooky access pattern.

4. **Dunder Attributes**: Double-underscore (dunder) attributes are accessible normally.

### Example Usage

```python
haunted_mansion = HauntedMansion(butler="Alfred", rooms=10, basement=True)

# Attempting to access without `spooky_` prefix
print(haunted_mansion.butler)  
# Output: "Booooo, only ghosts here!"

# Accessing with `spooky_` prefix
print(haunted_mansion.spooky_butler)  
# Output: "Alfred"

# Dynamically adding a new attribute
haunted_mansion.friendly_ghost = "Your favourite HP ghost - Nearly Headless Nick"
print(haunted_mansion.friendly_ghost)
# Output: "Booooo, only ghosts here!"

print(haunted_mansion.spooky_friendly_ghost)
# Output: "Your favourite HP ghost - Nearly Headless Nick"

# Accessing a dunder attribute
print(haunted_mansion.__class__)
# Output: <class '__main__.HauntedMansion'>
```

## Notes

This spooky attribute access is implemented to celebrate Halloween, adding a fun twist to object interaction.
