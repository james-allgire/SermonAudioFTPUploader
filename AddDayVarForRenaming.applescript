set myTime to time of (current date)

set myDate to weekday of (current date)

if (myDate = Sunday and myTime > 50400) then
	return "-Sunday PM"
else if (myDate = Sunday and myTime < 50400) then
	return "-Sunday AM"
else if (myDate = Wednesday) then
	return "-Midweek Service"
else
	return "-Special Event"
end if
