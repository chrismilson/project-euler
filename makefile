# This is to serve as a general makefile for the end user to try out my
# solutions themselves.
PROBLEM = problems/problem-

.PHONY: empty new %
empty:
	# Please specify a problem to run.
	#
	# For example, problem 5 can be done by doing
	#
	#	make 5

tools: devtools
	@ $(MAKE) -s -C $<
	# You can now use ./new -n number -N name to initialise a new problem!

devtools:
	@ git add submodule https://github.com/chrismilson/project-euler-tools.git $@

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
	@ $(MAKE) -s -C devtools clean
