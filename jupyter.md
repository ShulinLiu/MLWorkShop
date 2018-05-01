# using jupyter notebook with virtual environment
<!-- MarkdownTOC -->

- Reference
- Summary
- Do it Step by Step
    - Create virtual environment in your project folder
    - install ipykernel

<!-- /MarkdownTOC -->


## Reference

[using jupyter with virtual environment](http://anbasile.github.io/programming/2017/06/25/jupyter-venv/)

## Summary

How to do it?

```
install a custom kernel
```

## Do it Step by Step

### Create virtual environment in your project folder

find out and change folder to your project folder

```
$ ls
$ cd projectname

~/projectname $
```

create virtual environment with your specific configure

```
% binding virtual env with python3
~/projectname $ mkvirtualenv venvname -p python3
```

then, activate it

```
~/projectname $ workon venvname 
(venvname) ~/projectname $ 
```

### install ipykernel

inside virtual environment install ipykernerl using pip

```
(venvname) ~/projectname $ pip3 install ipykernel
```

then install a new kernel

```
(venvname) ~/projectname $ ipython kernel install --user --name=projectname
```

