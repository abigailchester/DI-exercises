var array1 = ["Banana", "Apples", "Oranges", "Blueberries"]

console.log(array1)

array1.shift()

console.log(array1)

array1.sort()

console.log(array1)

array1.push("Kiwi")

console.log(array1)

array1.shift()

console.log(array1)

array1.reverse()

console.log(array1)

var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]

console.log(array2)

//to access oranges, have to go within arrays

console.log(array2[1][1][0])