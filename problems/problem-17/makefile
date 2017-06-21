.PHONY : all
all :
	echo "Getting the Inflect Library..."
	@ pip -q install --user -e git+https://github.com/pwdyson/inflect.py#egg=inflect
	echo "Done"
	@ python number-letters.py
	@ rm -rf src
