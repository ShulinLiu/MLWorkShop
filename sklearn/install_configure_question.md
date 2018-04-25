# install matplotlib and use in Mac
<!-- MarkdownTOC -->

- [Reference](#reference)
- [Error encounter](#error-encounter)
- [Reason](#reason)
- [Method](#method)
	- [Solution 1](#solution-1)
	- [Solution 2](#solution-2)

<!-- /MarkdownTOC -->


## Reference

[stackflow:cannot using"import matplotlib.pyplot as plt"](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python)

[what is a backend](https://matplotlib.org/faq/usage_faq.html#what-is-a-backend)

## Error encounter

After install matplotlib in mac, when using:

```python
import matplotlib.pyplot as plt
```

There will error pop out:

```
**RuntimeError**: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends.
```

## Reason

In mac os, image back end of matplotlib is Cocoa which rendering in OSX windows. Set the back end of macosx that is differ compare with other windows or linux os.

So to solve this problem, set the back end to "TkAgg" 

## Method

### Solution 1

In root dir ,there is folder: ~/.matplotlib

Create a file ~/.matplotlib/matplotlibrc there and add the following code: backend: TkAgg

### Solution 2

Include below codes before import matplotlib

```python
import matplotlib as mpl
mpl.use('TkAgg')
```