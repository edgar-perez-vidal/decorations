# Decorations

**Utilities for setting up Matplotlib plots for Journal Articles.**

## Overview

The `decorations` package provides customizable settings for Matplotlib to create 
publication-ready plots. It includes options for font size, figure size, color 
palettes, and marker types that are particularly suitable for journals such as 
ApJ and MNRAS.

## Installation

To install the package, you can use `pip`. You have two options:

1. **Install directly from GitHub**:
   ```bash
   pip install git+https://github.com/edgar-perez-vidal/decorations.git
2. **Clone the repository and install locally** (Recommended for Personalization):
   ```bash  
   git clone https://github.com/edgar-perez-vidal/decorations.git
   cd decorations
   pip install -e .
To get started, check out the decorations_tutorial notebook!
If you make use of this package, please send over any figures so I can show case it here!


# Tutorial for the package decorations, based in Matplotlib

The `decorations` package was created to address a common challenge faced by many students and researchers: the need to generate numerous test plots using basic Matplotlib settings, only to return later to beautify them for submission or feedback. This often results in extra work and inconsistent presentation quality.

Decorations solves this problem by offering pre-configured plotting settings that produce aesthetically pleasing visuals right from the start. The package streamlines the plotting process, enabling users to create high-quality graphics immediately, without sacrificing the flexibility to further customize their plots as needed.

With Decorations, you can focus on your data while ensuring that your plots are ready for assignments, presentations, or feedback. Enjoy!


```python
from decorations import load_plot_settings, error_bar_settings
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
```

# Example Plot: Traditional Plotting Routine
Let's create a traditional plot with a sine wave and some noisy data.


```python
# Data for the plot with added noise
x = np.linspace(0, 2 * np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)

y1_noisy = y1 + 0.2 * np.random.normal(size=x.size)  # Add some noise

y1_err = 0.1 * np.ones_like(y1_noisy)  # Set the error bars

# Create the sine wave plot with error bars
plt.figure()
plt.scatter(x, y1_noisy, label='Data',)
plt.plot(x, y1, marker = '', label='Model',) # As of version='0.1.0', you will need to state marker = 'none' to get a line

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()
```


    
![png](decorations_tutorial_files/decorations_tutorial_4_0.png)
    


Pretty standard plot, don't hate it don't love it. Lets see what we can do to improve

## Using the `load_plot_settings` Function

In this example, we'll demonstrate how to use the **decorations** package to create a plot with error bars and residuals. 



```python
# Default parameters for load_plot_settings function
# Feel free to customize these values according to your specific plotting needs

load_plot_settings(
    fontsize=10,  # Font size for text in plots (default is 10, adjust as needed)
    figsize=(3.5, 3.5),  # Figure size (default is 3.5x3.5 for two-column figures)
    dpi=175,  # Dots per inch for plot resolution (higher values result in better quality)
    
    # Colors for cycling through data points
    # Use a custom list for your own palette, or leave as None to use the default color-blind friendly palette
    colors=None,  # default: ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377', '#BBBBBB']
    
    # Markers for plotting
    # Use a custom list for different marker shapes, or leave as None to use the default set
    markers=None,  # default: ['o', 's', '^', 'v', 'D', 'P', 'X']
    
    latex=False  # Set to True to enable LaTeX formatting for text; set to False for plain text
)

# load_plot_settings() # run on the default setting shown above
```

    Hi edgar839, you have imported plooting decorations. 
        Note: 
        Figsize = (3.5, 3.5) for coloumn figures
        Fontsize: 10
        Colorblind Pallet: ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377', '#BBBBBB']
        Marker: ['o', 's', '^', 'v', 'D', 'P', 'X']
        Cheers!


# Lets run the exact same code as before


```python
# Create the sine wave plot with error bars
plt.figure()
plt.scatter(x, y1_noisy, label='Data',)
plt.plot(x, y1, marker = '', label='Model',) # As of version='0.1.0', you will need to state marker = 'none' to get a line

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()
```


    
![png](decorations_tutorial_files/decorations_tutorial_9_0.png)
    


ahh much better! Lets try something a little cleaner, such as a fitting fake data and seeing the residuals. In this example, we'll use **gridspec** for a multi panel plot.


```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Generate some test data (sine wave with noise)
x = np.linspace(0, 10, 100)
y_data = np.sin(x) + 0.1 * np.random.normal(size=x.size)  # Noisy sine wave
yerr = 0.2 * np.random.uniform(low=0, high = 1,size=x.size)
y_model = np.polyval(np.polyfit(x, y_data, 6), x)  # Polynomial fit as a model

# Calculate residuals
residuals = y_data - y_model

# Create the figure and grid spec
fig = plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1],hspace= 0)  # 3:1 ratio for top and bottom panels

# Top panel: data and model
ax1 = fig.add_subplot(gs[0])
ax1.errorbar(x, y_data, yerr = yerr, **error_bar_settings, label="Data")  # Plot data
ax1.plot(x, y_model, 'k-', label="Model")  # Plot model
ax1.legend()
ax1.set_ylabel("Y values")

# Remove tick labels from the upper x-axis
ax1.tick_params(axis='x', which='both', labelbottom=False)

# Bottom panel: residuals
ax2 = fig.add_subplot(gs[1])
ax2.errorbar(x, residuals,yerr =yerr, **error_bar_settings)  # Plot residuals
ax2.axhline(0, color='k', linestyle='--')  # Zero line for residuals
ax2.set_ylim(-.7,.7)

ax2.set_xlabel("X values")
ax2.set_ylabel("Residuals",fontsize = 10)

# Adjust layout
plt.tight_layout()

# Save Figure Defualt Params
    #  "savefig.bbox": 'tight',
    #  "savefig.pad_inches": 0.05,
    #  "savefig.dpi": 300
# plt.savefig('test.pdf',)

```


    
![png](decorations_tutorial_files/decorations_tutorial_11_0.png)
    


## A closer look at `error_bar_settings` in plots

In this example, we will generate fake data and visualize it with error bars using `error_bar_settings` dictionary. This showcases how to markers and colors are automatically cycled through. Note that `error_bar_settings` is a standard dictionary that can be costumized as needed



```python
error_bar_settings

# error_bar_settings['ms'] = 5 # example of changing marker size
```




    {'ms': 3.0,
     'mec': 'black',
     'ecolor': 'black',
     'capsize': 1.25,
     'capthick': 0.2,
     'mew': 0.2,
     'elinewidth': 0.2,
     'alpha': 0.9,
     'zorder': 2,
     'linestyle': 'none'}




```python
import numpy as np

# Generate fake data
np.random.seed(42)
x = np.linspace(1, 10, 10)
y1 = np.random.normal(5, 0.5, size=len(x))
# Errors
yerr1 = np.random.uniform(0.1, 0.5, size=len(x))

fig, ax = plt.subplots(dpi = 175)
# Plot the data with error bars and cycle marker shapes
for i in np.arange(10):
    ax.errorbar(x, y1+i, yerr=yerr1,**error_bar_settings)


# Add labels and legend
ax.set_xlabel('X values')
ax.set_ylabel('Y values')

# Show the plot
plt.tight_layout()
plt.show()
```


    
![png](decorations_tutorial_files/decorations_tutorial_14_0.png)
    


To see the matplotlib parameters run the following


```python
plt.rcParams
```




    RcParams({'_internal.classic_mode': False,
              'agg.path.chunksize': 0,
              'animation.bitrate': -1,
              'animation.codec': 'h264',
              'animation.convert_args': ['-layers', 'OptimizePlus'],
              'animation.convert_path': 'convert',
              'animation.embed_limit': 20.0,
              'animation.ffmpeg_args': [],
              'animation.ffmpeg_path': 'ffmpeg',
              'animation.frame_format': 'png',
              'animation.html': 'none',
              'animation.writer': 'ffmpeg',
              'axes.autolimit_mode': 'data',
              'axes.axisbelow': 'line',
              'axes.edgecolor': 'black',
              'axes.facecolor': 'white',
              'axes.formatter.limits': [-5, 6],
              'axes.formatter.min_exponent': 0,
              'axes.formatter.offset_threshold': 4,
              'axes.formatter.use_locale': False,
              'axes.formatter.use_mathtext': False,
              'axes.formatter.useoffset': True,
              'axes.grid': False,
              'axes.grid.axis': 'both',
              'axes.grid.which': 'major',
              'axes.labelcolor': 'black',
              'axes.labelpad': 4.0,
              'axes.labelsize': 'medium',
              'axes.labelweight': 'normal',
              'axes.linewidth': 0.5,
              'axes.prop_cycle': (cycler('color', ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377', '#BBBBBB']) + cycler('marker', ['o', 's', '^', 'v', 'D', 'P', 'X'])),
              'axes.spines.bottom': True,
              'axes.spines.left': True,
              'axes.spines.right': True,
              'axes.spines.top': True,
              'axes.titlecolor': 'auto',
              'axes.titlelocation': 'center',
              'axes.titlepad': 6.0,
              'axes.titlesize': 'large',
              'axes.titleweight': 'normal',
              'axes.titley': None,
              'axes.unicode_minus': True,
              'axes.xmargin': 0.05,
              'axes.ymargin': 0.05,
              'axes.zmargin': 0.05,
              'axes3d.grid': True,
              'axes3d.xaxis.panecolor': (0.95, 0.95, 0.95, 0.5),
              'axes3d.yaxis.panecolor': (0.9, 0.9, 0.9, 0.5),
              'axes3d.zaxis.panecolor': (0.925, 0.925, 0.925, 0.5),
              'backend': 'module://matplotlib_inline.backend_inline',
              'backend_fallback': True,
              'boxplot.bootstrap': None,
              'boxplot.boxprops.color': 'black',
              'boxplot.boxprops.linestyle': '-',
              'boxplot.boxprops.linewidth': 1.0,
              'boxplot.capprops.color': 'black',
              'boxplot.capprops.linestyle': '-',
              'boxplot.capprops.linewidth': 1.0,
              'boxplot.flierprops.color': 'black',
              'boxplot.flierprops.linestyle': 'none',
              'boxplot.flierprops.linewidth': 1.0,
              'boxplot.flierprops.marker': 'o',
              'boxplot.flierprops.markeredgecolor': 'black',
              'boxplot.flierprops.markeredgewidth': 1.0,
              'boxplot.flierprops.markerfacecolor': 'none',
              'boxplot.flierprops.markersize': 6.0,
              'boxplot.meanline': False,
              'boxplot.meanprops.color': 'C2',
              'boxplot.meanprops.linestyle': '--',
              'boxplot.meanprops.linewidth': 1.0,
              'boxplot.meanprops.marker': '^',
              'boxplot.meanprops.markeredgecolor': 'C2',
              'boxplot.meanprops.markerfacecolor': 'C2',
              'boxplot.meanprops.markersize': 6.0,
              'boxplot.medianprops.color': 'C1',
              'boxplot.medianprops.linestyle': '-',
              'boxplot.medianprops.linewidth': 1.0,
              'boxplot.notch': False,
              'boxplot.patchartist': False,
              'boxplot.showbox': True,
              'boxplot.showcaps': True,
              'boxplot.showfliers': True,
              'boxplot.showmeans': False,
              'boxplot.vertical': True,
              'boxplot.whiskerprops.color': 'black',
              'boxplot.whiskerprops.linestyle': '-',
              'boxplot.whiskerprops.linewidth': 1.0,
              'boxplot.whiskers': 1.5,
              'contour.algorithm': 'mpl2014',
              'contour.corner_mask': True,
              'contour.linewidth': None,
              'contour.negative_linestyle': 'dashed',
              'date.autoformatter.day': '%Y-%m-%d',
              'date.autoformatter.hour': '%m-%d %H',
              'date.autoformatter.microsecond': '%M:%S.%f',
              'date.autoformatter.minute': '%d %H:%M',
              'date.autoformatter.month': '%Y-%m',
              'date.autoformatter.second': '%H:%M:%S',
              'date.autoformatter.year': '%Y',
              'date.converter': 'auto',
              'date.epoch': '1970-01-01T00:00:00',
              'date.interval_multiples': True,
              'docstring.hardcopy': False,
              'errorbar.capsize': 0.0,
              'figure.autolayout': False,
              'figure.constrained_layout.h_pad': 0.04167,
              'figure.constrained_layout.hspace': 0.02,
              'figure.constrained_layout.use': False,
              'figure.constrained_layout.w_pad': 0.04167,
              'figure.constrained_layout.wspace': 0.02,
              'figure.dpi': 175.0,
              'figure.edgecolor': 'white',
              'figure.facecolor': 'white',
              'figure.figsize': [3.5, 3.5],
              'figure.frameon': True,
              'figure.hooks': [],
              'figure.labelsize': 'large',
              'figure.labelweight': 'normal',
              'figure.max_open_warning': 20,
              'figure.raise_window': True,
              'figure.subplot.bottom': 0.11,
              'figure.subplot.hspace': 0.2,
              'figure.subplot.left': 0.125,
              'figure.subplot.right': 0.9,
              'figure.subplot.top': 0.88,
              'figure.subplot.wspace': 0.2,
              'figure.titlesize': 'large',
              'figure.titleweight': 'normal',
              'font.cursive': ['Apple Chancery',
                               'Textile',
                               'Zapf Chancery',
                               'Sand',
                               'Script MT',
                               'Felipa',
                               'Comic Neue',
                               'Comic Sans MS',
                               'cursive'],
              'font.family': ['serif'],
              'font.fantasy': ['Chicago',
                               'Charcoal',
                               'Impact',
                               'Western',
                               'xkcd script',
                               'fantasy'],
              'font.monospace': ['DejaVu Sans Mono',
                                 'Bitstream Vera Sans Mono',
                                 'Computer Modern Typewriter',
                                 'Andale Mono',
                                 'Nimbus Mono L',
                                 'Courier New',
                                 'Courier',
                                 'Fixed',
                                 'Terminal',
                                 'monospace'],
              'font.sans-serif': ['DejaVu Sans',
                                  'Bitstream Vera Sans',
                                  'Computer Modern Sans Serif',
                                  'Lucida Grande',
                                  'Verdana',
                                  'Geneva',
                                  'Lucid',
                                  'Arial',
                                  'Helvetica',
                                  'Avant Garde',
                                  'sans-serif'],
              'font.serif': ['DejaVu Serif',
                             'Bitstream Vera Serif',
                             'Computer Modern Roman',
                             'New Century Schoolbook',
                             'Century Schoolbook L',
                             'Utopia',
                             'ITC Bookman',
                             'Bookman',
                             'Nimbus Roman No9 L',
                             'Times New Roman',
                             'Times',
                             'Palatino',
                             'Charter',
                             'serif'],
              'font.size': 10.0,
              'font.stretch': 'normal',
              'font.style': 'normal',
              'font.variant': 'normal',
              'font.weight': 'normal',
              'grid.alpha': 1.0,
              'grid.color': '#b0b0b0',
              'grid.linestyle': '-',
              'grid.linewidth': 0.5,
              'hatch.color': 'black',
              'hatch.linewidth': 1.0,
              'hist.bins': 10,
              'image.aspect': 'equal',
              'image.cmap': 'viridis',
              'image.composite_image': True,
              'image.interpolation': 'antialiased',
              'image.lut': 256,
              'image.origin': 'upper',
              'image.resample': True,
              'interactive': True,
              'keymap.back': ['left', 'c', 'backspace', 'MouseButton.BACK'],
              'keymap.copy': ['ctrl+c', 'cmd+c'],
              'keymap.forward': ['right', 'v', 'MouseButton.FORWARD'],
              'keymap.fullscreen': ['f', 'ctrl+f'],
              'keymap.grid': ['g'],
              'keymap.grid_minor': ['G'],
              'keymap.help': ['f1'],
              'keymap.home': ['h', 'r', 'home'],
              'keymap.pan': ['p'],
              'keymap.quit': ['ctrl+w', 'cmd+w', 'q'],
              'keymap.quit_all': [],
              'keymap.save': ['s', 'ctrl+s'],
              'keymap.xscale': ['k', 'L'],
              'keymap.yscale': ['l'],
              'keymap.zoom': ['o'],
              'legend.borderaxespad': 0.5,
              'legend.borderpad': 0.4,
              'legend.columnspacing': 2.0,
              'legend.edgecolor': '0.8',
              'legend.facecolor': 'inherit',
              'legend.fancybox': True,
              'legend.fontsize': 'medium',
              'legend.framealpha': 0.8,
              'legend.frameon': False,
              'legend.handleheight': 0.7,
              'legend.handlelength': 1.25,
              'legend.handletextpad': 0.5,
              'legend.labelcolor': 'None',
              'legend.labelspacing': 0.5,
              'legend.loc': 'best',
              'legend.markerscale': 1.0,
              'legend.numpoints': 1,
              'legend.scatterpoints': 1,
              'legend.shadow': False,
              'legend.title_fontsize': None,
              'lines.antialiased': True,
              'lines.color': 'C0',
              'lines.dash_capstyle': <CapStyle.butt: 'butt'>,
              'lines.dash_joinstyle': <JoinStyle.round: 'round'>,
              'lines.dashdot_pattern': [6.4, 1.6, 1.0, 1.6],
              'lines.dashed_pattern': [3.7, 1.6],
              'lines.dotted_pattern': [1.0, 1.65],
              'lines.linestyle': '-',
              'lines.linewidth': 0.75,
              'lines.marker': 'None',
              'lines.markeredgecolor': 'auto',
              'lines.markeredgewidth': 1.0,
              'lines.markerfacecolor': 'auto',
              'lines.markersize': 6.0,
              'lines.scale_dashes': True,
              'lines.solid_capstyle': <CapStyle.projecting: 'projecting'>,
              'lines.solid_joinstyle': <JoinStyle.round: 'round'>,
              'macosx.window_mode': 'system',
              'markers.fillstyle': 'full',
              'mathtext.bf': 'sans:bold',
              'mathtext.bfit': 'sans:italic:bold',
              'mathtext.cal': 'cursive',
              'mathtext.default': 'it',
              'mathtext.fallback': 'cm',
              'mathtext.fontset': 'stix',
              'mathtext.it': 'sans:italic',
              'mathtext.rm': 'sans',
              'mathtext.sf': 'sans',
              'mathtext.tt': 'monospace',
              'patch.antialiased': True,
              'patch.edgecolor': 'black',
              'patch.facecolor': 'C0',
              'patch.force_edgecolor': False,
              'patch.linewidth': 1.0,
              'path.effects': [],
              'path.simplify': True,
              'path.simplify_threshold': 0.111111111111,
              'path.sketch': None,
              'path.snap': True,
              'pcolor.shading': 'auto',
              'pcolormesh.snap': True,
              'pdf.compression': 6,
              'pdf.fonttype': 3,
              'pdf.inheritcolor': False,
              'pdf.use14corefonts': False,
              'pgf.preamble': '',
              'pgf.rcfonts': True,
              'pgf.texsystem': 'xelatex',
              'polaraxes.grid': True,
              'ps.distiller.res': 6000,
              'ps.fonttype': 3,
              'ps.papersize': 'letter',
              'ps.useafm': False,
              'ps.usedistiller': None,
              'savefig.bbox': 'tight',
              'savefig.directory': '~',
              'savefig.dpi': 300.0,
              'savefig.edgecolor': 'auto',
              'savefig.facecolor': 'auto',
              'savefig.format': 'png',
              'savefig.orientation': 'portrait',
              'savefig.pad_inches': 0.05,
              'savefig.transparent': False,
              'scatter.edgecolors': 'face',
              'scatter.marker': 'o',
              'svg.fonttype': 'path',
              'svg.hashsalt': None,
              'svg.image_inline': True,
              'text.antialiased': True,
              'text.color': 'black',
              'text.hinting': 'force_autohint',
              'text.hinting_factor': 8,
              'text.kerning_factor': 0,
              'text.latex.preamble': '\\usepackage{textgreek} '
                                     '\\usepackage{amsmath}',
              'text.parse_math': True,
              'text.usetex': True,
              'timezone': 'UTC',
              'tk.window_focus': False,
              'toolbar': 'toolbar2',
              'webagg.address': '127.0.0.1',
              'webagg.open_in_browser': True,
              'webagg.port': 8988,
              'webagg.port_retries': 50,
              'xaxis.labellocation': 'center',
              'xtick.alignment': 'center',
              'xtick.bottom': True,
              'xtick.color': 'black',
              'xtick.direction': 'in',
              'xtick.labelbottom': True,
              'xtick.labelcolor': 'inherit',
              'xtick.labelsize': 'medium',
              'xtick.labeltop': False,
              'xtick.major.bottom': True,
              'xtick.major.pad': 3.5,
              'xtick.major.size': 5.0,
              'xtick.major.top': True,
              'xtick.major.width': 0.5,
              'xtick.minor.bottom': True,
              'xtick.minor.ndivs': 'auto',
              'xtick.minor.pad': 3.4,
              'xtick.minor.size': 2.5,
              'xtick.minor.top': True,
              'xtick.minor.visible': True,
              'xtick.minor.width': 0.5,
              'xtick.top': True,
              'yaxis.labellocation': 'center',
              'ytick.alignment': 'center_baseline',
              'ytick.color': 'black',
              'ytick.direction': 'in',
              'ytick.labelcolor': 'inherit',
              'ytick.labelleft': True,
              'ytick.labelright': False,
              'ytick.labelsize': 'medium',
              'ytick.left': True,
              'ytick.major.left': True,
              'ytick.major.pad': 3.5,
              'ytick.major.right': True,
              'ytick.major.size': 5.0,
              'ytick.major.width': 0.5,
              'ytick.minor.left': True,
              'ytick.minor.ndivs': 'auto',
              'ytick.minor.pad': 3.4,
              'ytick.minor.right': True,
              'ytick.minor.size': 2.5,
              'ytick.minor.visible': True,
              'ytick.minor.width': 0.5,
              'ytick.right': True})


