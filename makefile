# This is to serve as a general makefile for the end user to try out my
# solutions themselves.

.PHONY: empty new %
empty:
	# Please specify a problem to run.
	#
	# For example, problem 5 can be done by doing
	#
	#	make 5

new:
override MAKE_NEW = 1
# Note that if the problem already exists then the first rule will be run and
# no remake of the problem will occur
	@:

%: problem-% problem-%/makefile
	# Making problem $@.
	@ $(MAKE) -s -C $<
	# Done.

%: problem-%
	# Problem not equipped with a makefile; try manual installation.

%:
ifdef MAKE_NEW
	mkdir problem-$@/
	touch problem-$@/makefile
else
	# I have not done problem $@ yet.
	# It may not exist!
endif
