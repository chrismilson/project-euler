# This is to serve as a general makefile for the end user to try out my
# solutions themselves.
PROBLEM = problems/problem-

.PHONY: empty tools new %
empty:
	# Please specify a problem to run.
	#
	# For example, problem 5 can be done by doing
	#
	#	make 5

tools:
<<<<<<< HEAD
	@ python devtools/install-tools.py
=======
	python devtools/install-tools.py
>>>>>>> bb284bede79922025796765a920263d0acebfc78

%: $(PROBLEM)% $(PROBLEM)%/makefile
	# Making problem $@.
	@ $(MAKE) -s -C $< $(FLAGS)
	# Done.

%: $(PROBLEM)%
	# Problem not equipped with a makefile; try manual installation.

%:
	# I have not done problem $@ yet.
	# It may not exist!

clean:
	@ rm -f new problems/*.o *app
