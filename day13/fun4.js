const person = {
    name : "Meenakshi",
    age : 20,
    isStudent : true,
    city : "Amalapuram",
};
person.city = "Hyderabad",
console.log(person)
delete person.age;
console.log(person)