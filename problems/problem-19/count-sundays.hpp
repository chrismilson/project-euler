#ifndef COUNT_SUNDAYS_H
#define COUNT_SUNDAYS_H

#include <iostream>
#include <string>

enum Day {
  SUNDAY,
  MONDAY,
  TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY
};

enum Month {
  JANUARY,
  FEBRUARY,
  MARCH,
  APRIL,
  MAY,
  JUNE,
  JULY,
  AUGUST,
  SEPTEMBER,
  OCTOBER,
  NOVEMBER,
  DECEMBER
};

class Date {
public:
  Date(int, int, int);
  ~Date(){};
  void nextDay();
  Day getDay();
  int mday();
  int operator<(const Date&);
private:
  int day, month, year;
};

#endif
