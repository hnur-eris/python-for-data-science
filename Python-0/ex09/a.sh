python3 -m pip uninstall ft_package -y
rm -rf ./dist
python3 -m build
python3 -m pip install dist/ft_package-0.0.1-py3-none-any.whl
python3 -m pip show -v ft_package