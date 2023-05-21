rm -r dist
rm -r turbogpt.egg-info
python3 setup.py sdist
python3 -m build
twine upload dist/*