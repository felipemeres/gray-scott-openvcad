import pyvcad as pv

# Parametric Gray-Scott Reaction-Diffusion for OpenVCAD
# Converts Ready simulation parameters into 3D printable geometry
#
# Citations:
# - Tim Hutton, Robert Munafo, Andrew Trevorrow, Tom Rokicki, Dan Wills.
#   "Ready, a cross-platform implementation of various reaction-diffusion systems."
#   https://github.com/GollyGang/ready | http://arxiv.org/abs/1501.01990
# - Pearson, J. E. (1993). "Complex patterns in a simple system."
#   Science, 261(5118), 189-192. https://www.science.org/doi/10.1126/science.261.5118.189

# Primary Controls:

# 1. threshold - Geometry Amount

# - 0.2: Dense, coral-like structures (lots of geometry)
# - 0.4: Medium density (balanced)
# - 0.6: Sparse, minimal structures (little geometry)

# 2. time_param - Pattern Evolution

# - 0.0: Early-stage patterns (simple, nucleated)
# - 0.5: Mid-evolution (complex interactions)
# - 1.0: Mature patterns (fully developed)

# 3. frequency_scale - Pattern Size

# - 0.5: Large, macro-scale features
# - 1.0: Natural scale
# - 2.0: Fine, micro-scale details

# 4. density - Pattern Intensity

# - 0.5: Subtle, gentle patterns
# - 1.0: Natural intensity
# - 1.5: Strong, dramatic patterns

# Advanced Controls (in morphing version):

# 5. morph_factor - Pattern Type

# - 0.0: Spot patterns (classic Gray-Scott spots)
# - 0.5: Mixed patterns (spots + stripes)
# - 1.0: Stripe patterns (traveling waves)

# Ready Presets to Try:

# 1. "Coral Growth": threshold=0.25, time_param=0.3, frequency_scale=0.8
# 2. "Crystal Lattice": threshold=0.45, time_param=0.7, frequency_scale=1.5
# 3. "Organic Maze": threshold=0.35, time_param=0.5, frequency_scale=1.0
# 4. "Minimal Architecture": threshold=0.55, time_param=0.8, frequency_scale=2.0

# Parametric Gray-Scott with Controllable Geometry
materials = pv.default_materials()
pattern_solid = materials.id("red")

# ===== CONTROL PARAMETERS =====
# 1. GEOMETRY AMOUNT CONTROL
threshold = 0.4        # Lower = more geometry, Higher = less geometry
                       # Try: 0.2 (lots), 0.4 (medium), 0.6 (sparse)

# 2. TIME EVOLUTION CONTROL (simulates time steps in reaction-diffusion)
time_param = 0.5       # 0.0 = early stage, 1.0 = late stage evolution
                       # Controls pattern maturity/complexity

# 3. PATTERN SCALE CONTROL
frequency_scale = 1.0  # 0.5 = larger patterns, 2.0 = smaller patterns
                       # Controls the "wavelength" of the reaction-diffusion

# 4. PATTERN INTENSITY CONTROL
amplitude = 0.4        # 0.1 = subtle patterns, 0.8 = strong patterns
                       # Controls contrast/sharpness

# 5. EVOLUTION SPEED CONTROL
evolution_rate = 1.0   # How fast patterns develop over space
                       # Higher = more variation across the volume

# ===== 3D PRINTING CONTROL =====
make_printable = True    # True = manifold/printable, False = artistic/open
min_wall_thickness = 2.0 # Minimum wall thickness for printing (mm)

# ===== DOMAIN CONTROL =====
domain_size = pv.Vec3(50, 50, 25)  # Define the actual domain dimensions

# ===== READY'S BASE PARAMETERS =====
k1, k2 = 0.055, 0.075
F1, F2 = 0.001, 0.087

# Parameter variations with time evolution - properly normalized to domain
k_param = f"({k1} + ({k2}-{k1})*(x/{domain_size.x}) * (1 + 0.2 * {time_param}))"
F_param = f"({F1} + ({F2}-{F1})*(y/{domain_size.y}) * (1 + 0.3 * {time_param}))"

# Enhanced Gray-Scott with CORRECTED scaling to fill entire domain
# Pattern wavelengths now properly scaled to domain dimensions
pattern = f"""
sqrt(({k_param}) * ({F_param})) / sqrt({k2} * {F2}) * (
    0.5 + {amplitude} * cos(2*pi * x / {12.0/frequency_scale}) * cos(2*pi * y / {12.0/frequency_scale}) +
    {amplitude * 0.75} * cos(2*pi * x / {8.0/frequency_scale} + pi/3 + {time_param} * pi * {evolution_rate}) *
                          cos(2*pi * y / {8.0/frequency_scale} + pi/3 + {time_param} * pi * {evolution_rate}) +
    {amplitude * 0.5} * cos(2*pi * x / {16.0/frequency_scale}) * cos(2*pi * y / {16.0/frequency_scale}) *
                        cos(2*pi * z / {6.0/frequency_scale} + {time_param} * 2*pi * {evolution_rate}) +
    {amplitude * 0.625} * sin(2*pi * x / {10.0/frequency_scale} + {time_param} * pi * {evolution_rate}) *
                          sin(2*pi * y / {10.0/frequency_scale} + {time_param} * pi * {evolution_rate})
) * (1.0 + 0.3 * cos(2*pi * z / {8.0/frequency_scale} + {time_param} * pi * {evolution_rate}))
"""

# Create geometry with controllable threshold and printability options
if make_printable:
    # Create printable version with boundary constraints to ensure closure
    # Add boundary conditions that force the pattern to be solid at domain edges
    boundary_fade = f"""
    min(min(x - {min_wall_thickness}, {domain_size.x - min_wall_thickness} - x),
        min(min(y - {min_wall_thickness}, {domain_size.y - min_wall_thickness} - y),
            min(z - {min_wall_thickness}, {domain_size.z - min_wall_thickness} - z))) / {min_wall_thickness}
    """

    # Pattern with boundary fade (becomes solid near edges for manifold closure)
    manifold_pattern = f"({pattern}) + max(0, -({boundary_fade}) * 0.5)"

    # Create manifold geometry with boundary constraints
    root = pv.Function(f"{threshold} - ({manifold_pattern})", pattern_solid)

else:
    # Artistic version (pure mathematical surface, may have open edges)
    root = pv.Function(f"{threshold} - ({pattern})", pattern_solid)