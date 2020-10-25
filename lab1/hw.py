leaving_hour= 6.52 
easy_pace= 8
at_tempo= 6
whole_time=((easy_pace*(1+2))+(at_tempo*3))
hour_calculate=((whole_time+52)%60)
exact_hour=((whole_time+52)//60)
last_hour= exact_hour+6
print("I get home at", last_hour,":",hour_calculate)