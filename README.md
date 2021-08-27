# osm-export

ref. https://github.com/linuxmahara/prettymaps

The export does only 3 cities. If we like running all, 
we should comment lines following "TODO: xxx" in the file "main.py".


## Format

File name format: [city]-[country].[png|svg]

Default radius is 1500. If need to change, go to the file "main.py" and change if before running.


## Install 

only support OSX/ Ubuntu


### spatialindex (OSX MAC)

ref. https://macappstore.org/spatialindex/

```shell script
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 2> /dev/null

brew update

brew install spatialindex
```


### Python 3.8 (MAC OS/ UBUNTU)

ref. https://www.python.org/ftp/python/3.8.5/python-3.8.5-macosx10.9.pkg 

```shell script
# python package download & install, then check version
python --version

pip --version

# upgrade pip
pip install -U pip

# install dependencies
pip install -U setuptools wheel attrs click rtree

pip install -r ./requirements.txt

# install vsketch
pip install git+https://github.com/abey79/vsketch#egg=vsketch 

# install prettymap
pip install git+https://github.com/marceloprates/prettymaps.git


```



