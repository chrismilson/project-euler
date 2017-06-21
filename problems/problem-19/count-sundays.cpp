/* Chris Milson June 2017
** Problem 19
*
* You are given the following information, but you may prefer to do some
* research for yourself.
*
* 	1 Jan 1900 was a Monday.
* 	Thirty days has September,
* 	April, June and November.
* 	All the rest have thirty-one,
* 	Saving February alone,
* 	Which has twenty-eight, rain or shine.
* 	And on leap years, twenty-nine.
*
* 	A leap year occurs on any year evenly divisible by 4, but not on a century
* 	unless it is divisible by 400.
*
* Answer :
*/

/*
** I will make a date class and give it an increment function to let an instance
* become the next day. Then I will iterate through dates from 1 Jan 1901
* and increment a counter for the sundays.
*
* The logic used to work out the day of the week given a date is from
* https://plus.maths.org/content/what-day-week-were-you-born
*
*/

#include "count-sundays.hpp"

Date::Date(int day, int month, int year) {
	this->day = day;
	this->month = month;
	this->year = year;
}

void Date::nextDay() {
	int daysInFeb = 28;
	/* year is 0 mod 4 and if it is 0 mod 100 then it is 0 mod 400. */
	if (this->year % 4 == 0 && (!(this->year % 100 == 0) || (this->year % 400 == 0))) {
			daysInFeb++;
	}
	int daysIn[] = {31, daysInFeb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	if (this->day < daysIn[this->month]) {
		this->day += 1;
	} else {
		this->day = 0;
		if (this->month < DECEMBER) {
			this->month += 1;
		} else {
			this->month = JANUARY;
			this->year += 1;
		}
	}
}

Day Date::getDay() {
	int monthOffset[] = {6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
	int decadeOffset[] = {1, 6, 5, 3, 2, 0, 6, 4, 3, 1, 0, 5};
	int day = this->day;

	day += monthOffset[this->month];
	day += decadeOffset[(this->year/ 10) % 10];
	day += year % 10;

	if (this->year % 20 < 10) {
		day += (this->year % 10 > 3);
		day += (this->year % 10 > 7);
	} else {
			day += (this->year % 10 > 1);
			day += (this->year % 10 > 5);
	}

	return Day(day % 7);
}

int Date::mday() {
	return this->day;
}

int Date::operator<(const Date& rhs) {
	if (this->year != rhs.year) {
		return this->year < rhs.year;
	}
	if (this->month != rhs.month) {
		return this->month < rhs.month;
	}
	return this->day < rhs.day;
}

int main(int argc, char **argv) {
	Date start(1, JANUARY, 1901);
	Date end(31, DECEMBER, 2000);

	int counter = 0;

	for (;start < end; start.nextDay()) {
		counter += (start.getDay() == SUNDAY && start.mday() == 0);
	}

	std::cout << "There were " << counter << " Sundays between ";
	std::cout << "1st January 1901 and 31st December 2000 that fell ";
	std::cout << "on the first of the month.\n";
	return 0;
}
