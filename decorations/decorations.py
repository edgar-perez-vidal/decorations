# Created by Edgar P. Vidal
# Github https://github.com/edgar-perez-vidal
import matplotlib.pyplot as plt
from cycler import cycler
import getpass

username = getpass.getuser()  # Get the current username
fontsize = 10 #latex ApJ, MNRAS ect
figsize = 3.5,3.5 # For two column paper figure size should be (3.5, any) (base x height)
colors = ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377', '#BBBBBB']  # Colorblind-friendly palette
markers = ['o', 's', '^', 'v', 'D', 'P', 'X']  # Different marker shapes to cycle through
linestyles = ['-', '-.', '--', ':', '-', '-.', '--', ':'] 

def load_plot_settings(
    fontsize=10, 
    figsize=(3.5, 3.5), 
    major_tick_size = 5,
    dpi=175, 
    colors=None,
    use_tex = True 
):
    """
    Load global Matplotlib settings for plots.
    
    Parameters:
    - fontsize: Font size for text in plots.
    - figsize: Tuple for figure size, e.g., (3.5, 3.5) for two-column figures.
    - dpi: Dots per inch for plot resolution in Jupyter.
    - colors: List of colors for cycling, default is color-blind friendly palette.
    - markers: List of marker shapes for cycling.
    - latex: Whether to enable LaTeX formatting for text.
    """
    
    if colors is None:
        # Default color-blind friendly palette
        colors = ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377', '#BBBBBB']  # Colorblind-friendly palette
        
    # Global Matplotlib settings
    if use_tex:
        # Configure matplotlib for LaTeX text rendering
        plt.rcParams.update({
            "text.usetex": True,  # Enable LaTeX formatting
            "font.family": "serif",  # Use serif font for LaTeX
            "text.latex.preamble": r'\usepackage{textgreek} \usepackage{amsmath}',  # Include LaTeX packages
        })
    else:
        # Configure matplotlib without LaTeX dependency
        plt.rcParams['mathtext.fontset'] = 'stix'
        plt.rcParams['font.family'] = 'STIXGeneral'
        plt.rcParams['font.size'] = fontsize

    plt.rcParams.update({
        "font.size": fontsize,  # Set global font size
        "mathtext.fontset": 'stix',  # Use STIX fonts for math text
        "text.latex.preamble": r'\usepackage{textgreek} \usepackage{amsmath}',  # Include LaTeX packages
        
        # Set color cycle: Color blind friendly! Highly encourage taking a look at Paul Tol's Notes, provides some good color theory for data visualization
        # Reference:  https://personal.sron.nl/~pault 
        "axes.prop_cycle": cycler('color', colors),

        # Set default figure size
        "figure.figsize": figsize,
        "figure.dpi": dpi, # this is mainly to make figure bigger in jupyternotebook, save at 300+,dpi

        # Ticks settings for x axis
        "xtick.direction": 'in',
        "xtick.major.size": major_tick_size,
        "xtick.major.width": 0.5,
        "xtick.minor.size": major_tick_size/2,
        "xtick.minor.width": 0.5,
        "xtick.minor.visible": True,
        "xtick.top": True,
        
        # Ticks settings for y axis
        "ytick.direction": 'in',
        "ytick.major.size": major_tick_size,
        "ytick.major.width": 0.5,
        "ytick.minor.size": major_tick_size/2,
        "ytick.minor.width": 0.5,
        "ytick.minor.visible": True,
        "ytick.right": True,
        
        # Line and grid widths
        "axes.linewidth": 0.5,
        "grid.linewidth": 0.5,
        "lines.linewidth": .75,

        # Legend settings
        "legend.frameon": False, # No box
        "legend.handlelength": 1.25, # Distance the line length in legend
        "legend.handletextpad": 0.5, # Distance between marker/line and lable
        
        # Always save figures tightly
        "savefig.bbox": 'tight',
        "savefig.pad_inches": 0.05,
        "savefig.dpi": 300
    })

    # Optional for Jupyter Notebook or IPython to improve image quality
    try:
        get_ipython().run_line_magic('config', 'InlineBackend.figure_format = "retina"')
    except NameError:
        pass  # Not running in Jupyter Notebook or IPython

    print(f'''Hi {username}, you have imported plotting decorations. 
    Note: 
    Figsize = {figsize} for coloumn figures
    dpi = {dpi}
    Fontsize: {fontsize}
    Colorblind Pallet: {colors}
    Marker: {markers}
    linestyles: {linestyles}
    Use tex? {use_tex}
    Cheers!'''
    )

# Come back to this, I will cycle marker types, though not sure if its best to cycle shapes or colors...
error_bar_settings = {
    # 'fmt': 'o',          # Format of the marker  
    'ms': 3.5,              # Marker size (adjusted for a 3.5x3.5 figure)
    # 'mfc': 'color',      # Marker face color (cycle color blind)
    'mec': 'black',        # Marker edge color
    'ecolor': 'black',     # Error bar color
    'capsize': 1.3,       # Size of the cap on the error bars
    'capthick': 0.25,       # Thickness of the caps
    'mew': 0.25,            # Marker edge width
    'elinewidth': 0.25,     # Error bar line width (slightly thicker for clarity)
    'alpha': 0.9,          # Slight transparency for better layering
    'zorder': 2,           # Control layering so error bars are on top
}
