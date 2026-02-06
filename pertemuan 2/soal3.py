tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL","NodeJS"}

keahlianBersama= tim_frontend.intersection(tim_backend)
print (keahlianBersama)

keahlianKhusus= tim_backend.difference(tim_frontend)
print(keahlianKhusus)

setbaru= tim_frontend | tim_backend
print (setbaru)