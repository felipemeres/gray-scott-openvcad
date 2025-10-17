# Gray-Scott Parameter Examples

This document provides specific parameter combinations that produce interesting and printable results.

## Beginner Examples

### Simple Coral Structure
```python
threshold = 0.3
time_param = 0.2
frequency_scale = 0.8
amplitude = 0.4
evolution_rate = 1.0
make_printable = True
```
**Result**: Dense, branching coral-like structure, good for first prints.

### Geometric Lattice
```python
threshold = 0.5
time_param = 0.8
frequency_scale = 1.5
amplitude = 0.5
evolution_rate = 0.8
make_printable = True
```
**Result**: Regular, geometric patterns with good structural integrity.

## Advanced Examples

### Organic Architecture
```python
threshold = 0.4
time_param = 0.6
frequency_scale = 1.2
amplitude = 0.6
evolution_rate = 1.5
make_printable = True
```
**Result**: Building-like structures with organic flow, suitable for architectural models.

### Jewelry Scale
```python
threshold = 0.45
time_param = 0.7
frequency_scale = 2.0
amplitude = 0.3
evolution_rate = 1.8
make_printable = True
```
**Result**: Fine, intricate patterns suitable for jewelry or small decorative objects.

### Vase-like Structures
```python
threshold = 0.35
time_param = 0.4
frequency_scale = 0.9
amplitude = 0.5
evolution_rate = 1.2
make_printable = True
```
**Result**: Hollow, vessel-like forms with organic walls.

## Artistic Exploration

### Abstract Sculpture
```python
threshold = 0.25
time_param = 0.9
frequency_scale = 0.6
amplitude = 0.7
evolution_rate = 2.0
make_printable = False  # For visualization only
```
**Result**: Complex, flowing forms for artistic exploration.

### Minimal Forms
```python
threshold = 0.6
time_param = 0.3
frequency_scale = 1.8
amplitude = 0.2
evolution_rate = 0.5
make_printable = True
```
**Result**: Clean, minimal structures with subtle detail.

## Troubleshooting

### Too Dense (Hard to Print)
- Increase `threshold` (0.4 → 0.5)
- Decrease `amplitude` (0.6 → 0.4)

### Too Sparse (No Geometry)
- Decrease `threshold` (0.5 → 0.3)
- Increase `amplitude` (0.3 → 0.5)

### Pattern Too Large
- Increase `frequency_scale` (1.0 → 1.5)

### Pattern Too Small
- Decrease `frequency_scale` (1.0 → 0.7)

### Not Printable
- Set `make_printable = True`
- Increase `min_wall_thickness` (2.0 → 3.0)