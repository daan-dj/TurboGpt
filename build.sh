rm -r dist
rm -r turbogpt.egg-info
python setup.py sdist
python -m build
twine upload dist/*